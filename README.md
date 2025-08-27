# 🔓 Bypass_iThemesSecurity

Herramienta de detección y explotación de slugs ocultos generados por el plugin **iThemes Security** en instalaciones WordPress mal configuradas o desactualizadas.

> ⚠️ Basada en la vulnerabilidad documentada en:  
> [WPScan Advisory - iThemes Security <= 8.1.2](https://wpscan.com/vulnerability/42fdb534-3aef-4ed7-94a8-4cfe8ff977e1)

---

## 🧠 ¿Qué hace esta herramienta?

`Bypass_iThemesSecurity` automatiza la detección de tokens (`slugs`) ocultos usados por iThemes Security para mover el acceso al panel de login de WordPress (`wp-login.php`). Si el sitio está desactualizado o mal configurado, esta herramienta puede encontrar ese slug y permitir el **bypass completo** del ocultamiento.

---

## 🎯 Casos de uso

- Red Teams y Pentesters que necesiten evadir plugins de ocultamiento de login.
- Auditores de seguridad en entornos WordPress.
- Investigadores de seguridad interesados en fingerprinting de instalaciones WordPress.
- Cazadores de bugs que validan configuraciones erróneas.

---

## 🚀 Requisitos

- Python 3.7+
- Conexión a internet
- Librerías:
  - `requests`
  - `beautifulsoup4`
  - `rich`
  - `pyfiglet`

Instálalas con:

```bash
pip install -r requirements.txt
