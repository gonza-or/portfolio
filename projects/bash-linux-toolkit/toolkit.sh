#!/usr/bin/env bash
set -u
set -o pipefail

usage() {
    printf '%s\n' 'Uso: bash toolkit.sh {system|disk|memory|processes|network|ping HOST|service UNIDAD|logs [UNIDAD]}'
}

require() {
    if ! command -v "$1" >/dev/null 2>&1; then
        printf 'Falta el comando: %s\n' "$1" >&2
        exit 1
    fi
}

valid_target() {
    if [[ ! "$1" =~ ^[a-zA-Z0-9][a-zA-Z0-9._:%-]*$ ]]; then
        printf '%s\n' 'Destino inválido: indicar un hostname o una IP, sin opciones ni espacios.' >&2
        exit 2
    fi
}

action="${1:---help}"
case "$action" in
    system)
        require uname
        uname -srmo
        printf 'Hostname: %s\n' "$(hostname)"
        if [[ -r /etc/os-release ]]; then
            sed -n 's/^PRETTY_NAME=//p' /etc/os-release
        fi
        uptime
        ;;
    disk)
        require df
        df -hT
        ;;
    memory)
        require free
        free -h
        ;;
    processes)
        require ps
        ps -eo pid,comm,%cpu,%mem --sort=-%mem | sed -n '1,16p'
        ;;
    network)
        require ip
        ip -brief address
        ip route show
        ;;
    ping)
        if [[ $# -ne 2 ]]; then usage >&2; exit 2; fi
        valid_target "$2"
        require ping
        ping -c 4 -W 2 "$2"
        ;;
    service)
        if [[ $# -ne 2 ]]; then usage >&2; exit 2; fi
        valid_target "$2"
        require systemctl
        SYSTEMD_COLORS=0 systemctl --no-pager --full status "$2"
        ;;
    logs)
        if [[ $# -gt 2 ]]; then usage >&2; exit 2; fi
        require journalctl
        if [[ $# -eq 2 ]]; then
            valid_target "$2"
            journalctl --no-pager -n 30 -u "$2"
        else
            journalctl --no-pager -n 30 -p warning
        fi
        ;;
    -h|--help) usage ;;
    *) usage >&2; exit 2 ;;
esac
