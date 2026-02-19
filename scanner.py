import socket
import json
import logging
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configuração de logging
logging.basicConfig(
    filename="scan.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

TIMEOUT = 1
MAX_THREADS = 50

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}


def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(TIMEOUT)
            result = sock.connect_ex((ip, port))
            return port if result == 0 else None
    except Exception as e:
        logging.error(f"Erro ao escanear porta {port}: {e}")
        return None


def run_scan(ip, start_port=1, end_port=1024):
    print(f"\n🔎 Iniciando varredura no IP: {ip}")
    print(f"📡 Range de portas: {start_port}-{end_port}\n")

    logging.info(f"Iniciando varredura no IP {ip} portas {start_port}-{end_port}")

    open_ports = []

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = [
            executor.submit(scan_port, ip, port)
            for port in range(start_port, end_port + 1)
        ]

        for future in as_completed(futures):
            port = future.result()
            if port:
                service = COMMON_PORTS.get(port, "Serviço desconhecido")
                print(f"[+] Porta {port} ({service}) está ABERTA")
                logging.info(f"Porta {port} ({service}) aberta")
                open_ports.append({
                    "port": port,
                    "service": service
                })

    report = {
        "target": ip,
        "scan_range": f"{start_port}-{end_port}",
        "scan_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_open_ports": len(open_ports),
        "open_ports": sorted(open_ports, key=lambda x: x["port"])
    }

    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("\n✅ Varredura finalizada!")
    print(f"🔓 Total de portas abertas: {len(open_ports)}")
    print("📄 Relatório salvo em report.json")

    logging.info("Varredura finalizada com sucesso")

    return report


if __name__ == "__main__":
    target_ip = input("Digite o IP alvo: ")
    start = int(input("Porta inicial (padrão 1): ") or 1)
    end = int(input("Porta final (padrão 1024): ") or 1024)

    run_scan(target_ip, start, end)
