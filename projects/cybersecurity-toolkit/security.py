#!/usr/bin/env python3
"""Consultas defensivas locales y utilidades de integridad."""

import argparse
import hashlib
import hmac
import json
import platform
import re
import secrets
import socket
import string
from collections import Counter
from pathlib import Path

import psutil


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def make_password(length):
    groups = (string.ascii_lowercase, string.ascii_uppercase, string.digits, "!@#$%+-_=?.")
    alphabet = "".join(groups)
    while True:
        password = "".join(secrets.choice(alphabet) for _ in range(length))
        if all(any(char in group for char in password) for group in groups):
            return password


def inspect_log(path):
    counts = Counter()
    total = 0
    with open(path, encoding="utf-8", errors="replace") as source:
        for line in source:
            total += 1
            for word in ("error", "warning", "failed", "denied"):
                if re.search(r"\b" + word + r"\b", line, re.IGNORECASE):
                    counts[word] += 1
    return {"lines": total, "matching_lines": dict(counts)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="action", required=True)
    for name in ("hash", "verify", "logs"):
        command = commands.add_parser(name)
        command.add_argument("file", type=Path)
        if name == "verify":
            command.add_argument("expected", help="SHA-256 esperado (64 caracteres hexadecimales)")
    password = commands.add_parser("password")
    password.add_argument("--length", type=int, default=20)
    ports = commands.add_parser("ports", help="Comprueba sólo puertos explícitos en loopback local")
    ports.add_argument("ports", type=int, nargs="+")
    for name in ("connections", "processes", "system"):
        commands.add_parser(name)
    args = parser.parse_args()
    try:
        if args.action == "hash":
            print(sha256_file(args.file))
        elif args.action == "verify":
            if not re.fullmatch(r"[0-9a-fA-F]{64}", args.expected):
                parser.error("El hash esperado debe tener 64 caracteres hexadecimales")
            matches = hmac.compare_digest(sha256_file(args.file), args.expected.lower())
            print("Integridad verificada" if matches else "El hash NO coincide")
            return 0 if matches else 1
        elif args.action == "password":
            if not 12 <= args.length <= 128:
                parser.error("La longitud debe estar entre 12 y 128")
            print(make_password(args.length))
        elif args.action == "ports":
            if len(args.ports) > 20 or any(port < 1 or port > 65535 for port in args.ports):
                parser.error("Indicar entre 1 y 20 puertos, cada uno entre 1 y 65535")
            for port in dict.fromkeys(args.ports):
                for host in ("127.0.0.1", "::1"):
                    try:
                        with socket.create_connection((host, port), timeout=1):
                            print(f"[{host}]:{port} acepta TCP")
                    except OSError:
                        print(f"[{host}]:{port} sin conexión TCP")
        elif args.action == "connections":
            for connection in psutil.net_connections(kind="inet"):
                local = f"{connection.laddr.ip}:{connection.laddr.port}" if connection.laddr else "-"
                remote = f"{connection.raddr.ip}:{connection.raddr.port}" if connection.raddr else "-"
                print(f"PID {connection.pid} | {local} -> {remote} | {connection.status}")
            print("La visibilidad depende de permisos; la lista puede ser parcial.")
        elif args.action == "processes":
            for process in psutil.process_iter(["pid", "name", "status"], ad_value="Sin permiso"):
                print(f"{process.info['pid']} | {process.info['name']} | {process.info['status']}")
        elif args.action == "system":
            print(f"Hostname: {socket.gethostname()}\nSistema: {platform.platform()}")
            print(f"CPU lógicas: {psutil.cpu_count()}\nRAM: {psutil.virtual_memory().total / 1024**3:.2f} GiB")
        elif args.action == "logs":
            print(json.dumps(inspect_log(args.file), ensure_ascii=False, indent=2))
    except (OSError, psutil.Error) as error:
        print(f"No se pudo completar la consulta: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
