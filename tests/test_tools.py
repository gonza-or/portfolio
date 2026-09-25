"""Pruebas locales; no necesitan destinos externos ni privilegios."""

import hashlib
import importlib.util
import json
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MONITOR = ROOT / "projects/system-monitor/monitor.py"
NETWORK = ROOT / "projects/network-toolkit/network.py"
SECURITY = ROOT / "projects/cybersecurity-toolkit/security.py"


def run(script, *args):
    return subprocess.run([sys.executable, str(script), *map(str, args)],
                          capture_output=True, text=True, timeout=15)


class MonitorTests(unittest.TestCase):
    def test_real_report(self):
        result = run(MONITOR, "--json", "--path", ROOT)
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertTrue(report["hostname"])
        self.assertGreater(report["ram_total_gib"], 0)
        self.assertGreaterEqual(report["cpu_percent"], 0)
        self.assertLessEqual(report["cpu_percent"], 100)
        self.assertIsInstance(report["interfaces"], dict)

    def test_missing_path(self):
        with tempfile.TemporaryDirectory() as directory:
            result = run(MONITOR, "--path", Path(directory) / "missing")
        self.assertEqual(result.returncode, 1)
        self.assertIn("No se pudo consultar", result.stderr)
        self.assertNotIn("Traceback", result.stderr)


class NetworkTests(unittest.TestCase):
    def test_ipv6_loopback_input(self):
        result = run(NETWORK, "dns", "::1")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("::1", result.stdout)

    def test_local_dns(self):
        result = run(NETWORK, "dns", "localhost")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertTrue("127.0.0.1" in result.stdout or "::1" in result.stdout)

    def test_tcp_listener_and_closed_port(self):
        with socket.socket() as server:
            server.bind(("127.0.0.1", 0))
            port = server.getsockname()[1]
            server.listen(1)
            result = run(NETWORK, "tcp", "127.0.0.1", port)
            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertIn("TCP conectado", result.stdout)
        with socket.socket() as closed:
            closed.bind(("127.0.0.1", 0))
            result = run(NETWORK, "tcp", "127.0.0.1", closed.getsockname()[1])
            self.assertEqual(result.returncode, 1)

    def test_invalid_ports(self):
        for port in ("0", "65536", "abc"):
            with self.subTest(port=port):
                result = run(NETWORK, "tcp", "localhost", port)
                self.assertEqual(result.returncode, 2)

    def test_option_injection_rejected(self):
        result = run(NETWORK, "ping", "--", "-help")
        self.assertEqual(result.returncode, 2)

    def test_missing_traceroute(self):
        spec = importlib.util.spec_from_file_location("network", NETWORK)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with self.assertRaisesRegex(RuntimeError, "No está disponible"):
            module.run_command(["portfolio-command-that-does-not-exist"])


class SecurityTests(unittest.TestCase):
    def test_hash_and_integrity(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "fixture.bin"
            content = b"abc\x00" * 300000
            file.write_bytes(content)
            expected = hashlib.sha256(content).hexdigest()
            self.assertEqual(run(SECURITY, "hash", file).stdout.strip(), expected)
            self.assertEqual(run(SECURITY, "verify", file, expected.upper()).returncode, 0)
            file.write_bytes(content + b"changed")
            self.assertEqual(run(SECURITY, "verify", file, expected).returncode, 1)
            self.assertEqual(run(SECURITY, "verify", file, "not-a-hash").returncode, 2)

    def test_password_constraints(self):
        for length in (12, 24, 128):
            result = run(SECURITY, "password", "--length", length)
            password = result.stdout.strip()
            self.assertEqual(result.returncode, 0)
            self.assertEqual(len(password), length)
            self.assertTrue(any(c.islower() for c in password))
            self.assertTrue(any(c.isupper() for c in password))
            self.assertTrue(any(c.isdigit() for c in password))
            self.assertTrue(any(not c.isalnum() for c in password))
        for length in (0, 11, 129):
            self.assertEqual(run(SECURITY, "password", "--length", length).returncode, 2)

    def test_local_ports_only(self):
        with socket.socket() as server:
            server.bind(("127.0.0.1", 0))
            server.listen(1)
            port = server.getsockname()[1]
            result = run(SECURITY, "ports", port)
            self.assertEqual(result.returncode, 0)
            self.assertIn(f"[127.0.0.1]:{port} acepta TCP", result.stdout)
        self.assertEqual(run(SECURITY, "ports", 0).returncode, 2)
        self.assertEqual(run(SECURITY, "ports", *range(1, 22)).returncode, 2)
        self.assertEqual(run(SECURITY, "ports", "1-100").returncode, 2)
        self.assertEqual(run(SECURITY, "ports", "--host", "example.com", 80).returncode, 2)

    def test_log_counting(self):
        result = run(SECURITY, "logs", ROOT / "projects/cybersecurity-toolkit/sample.txt")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout), {
            "lines": 4,
            "matching_lines": {"warning": 1, "error": 1, "failed": 1, "denied": 1},
        })

    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            result = run(SECURITY, "hash", Path(directory) / "missing")
        self.assertEqual(result.returncode, 1)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
