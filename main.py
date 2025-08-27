from core.scanner import detect_hidden_login
from utils.banner import mostrar_banner

def main():
    mostrar_banner()
    target = input("[+] Ingresa la URL objetivo (sin / al final): ").strip()
    detect_hidden_login(target)

if __name__ == "__main__":
    main()
