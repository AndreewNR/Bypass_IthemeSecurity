from rich.console import Console
from rich.panel import Panel
import shutil
from pyfiglet import Figlet

def mostrar_banner():
    console = Console()
    terminal_width = shutil.get_terminal_size().columns

    # Banner ASCII - centrado con estilo
    figlet = Figlet(font="slant", width=terminal_width)
    titulo_ascii = figlet.renderText("Bypass Ithemes Sec")
    for linea in titulo_ascii.splitlines():
        console.print(linea.center(terminal_width), style="bold red")

    # Descripción informativa, no como menú
    descripcion = (
        "[bold red]Bypass_iThemesSec[/bold red] - Herramienta para eludir el módulo [bold yellow]'Hide Backend'[/bold yellow] de iThemes Security\n\n"
        "- 🔍 Detecta el slug personalizado del login oculto\n"
        "- 🛡️  Verifica redirección 403 personalizada\n"
        "- 📊 Analiza el comportamiento de respuestas\n"
        "- 🚀 Realiza fuerza bruta inteligente sobre slugs"
    )

    panel = Panel(
        descripcion,
        title="🔥 Funcionalidades principales 🔥",
        border_style="red",
        width=terminal_width
    )
    console.print(panel)

    # Instrucción final para el usuario
    console.print("[bold yellow]👉 Introduce la URL o dominio objetivo (ej. https://victima.com):[/bold yellow]\n")
