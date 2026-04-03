# 🎥 Instagram & TikTok Downloader

Script en Python para descargar **reels de Instagram (públicos y privados)** y videos de TikTok utilizando `yt-dlp`.

---

## 🚀 Características

* 📥 Descarga reels de Instagram
* 🔒 Soporte para cuentas privadas (si tenés acceso)
* 🎵 Soporte para TikTok
* 📂 Organización automática por fecha y usuario
* 🍪 Uso de cookies del navegador (Firefox)
* ⚡ Descarga rápida y simple desde terminal

---

## 📁 Estructura de archivos

Las descargas se guardan automáticamente en:

```
descargas/
 └── YYYY-MM-DD/
      └── usuario/
           └── video.mp4
```

---

## 🛠 Requisitos

* Python 3.10+
* Navegador Firefox instalado
* Cuenta de Instagram logueada en Firefox

---

## 📦 Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/instagram-downloader.git
cd instagram-downloader
```

2. Instalar dependencias:

```bash
pip install yt-dlp
```

---

## ▶️ Uso

Ejecutar el script:

```bash
python instagram_downloader.py
```

Luego pegar la URL cuando lo solicite:

```
🔗 Pegá la URL:
```

Ejemplo:

```
https://www.instagram.com/reel/XXXXXXXXX/
```

---

## 🔐 Descarga de cuentas privadas

Para descargar contenido privado:

* ✔ Debés estar logueado en Instagram en Firefox
* ✔ Debés seguir la cuenta privada
* ✔ Cerrá Firefox antes de ejecutar el script

---

## ⚠️ Limitaciones

* Instagram cambia constantemente su sistema → puede fallar
* No funciona si no tenés acceso al contenido
* Algunos reels pueden estar protegidos o restringidos

---

## 🧠 Cómo funciona

El script utiliza:

* `yt-dlp` para la descarga
* Cookies del navegador (`--cookies-from-browser firefox`)
* Organización automática de archivos por fecha

---

## 📌 Notas

Si tenés problemas:

1. Actualizá yt-dlp:

   ```bash
   pip install -U yt-dlp
   ```

2. Verificá que estás logueado en Instagram

3. Probá con otro reel

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Podés abrir issues o pull requests.

---

## 📄 Licencia

MIT License
