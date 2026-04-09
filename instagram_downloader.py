import os
import subprocess
from datetime import datetime

BASE_DIR = os.getcwd()
CARPETA_BASE = os.path.join(BASE_DIR, "descargas")


def limpiar_url(url: str) -> str:
    return url.strip().split("?")[0].rstrip("/")


def ejecutar(comando):
    print("\n🛠 Ejecutando:", " ".join(comando))
    
    try:
        resultado = subprocess.run(comando, text=True)
        return resultado.returncode == 0
    except Exception as e:
        print("Error ejecutando comando:", e)
        return False


def descargar_con_yt_dlp(url, carpeta):
    print("Usando cookies de Firefox")

    comando = [
        "python", "-m", "yt_dlp",
        "--cookies-from-browser", "firefox",

        # compatibilidad TikTok
        "--user-agent", "Mozilla/5.0",
        "--referer", "https://www.tiktok.com/",

        "--no-playlist",
        "--no-warnings",
        "--retries", "3",

        # 📹 Formato más compatible
        "-f", "mp4/bv*+ba/b",

        "--merge-output-format", "mp4",

        # 🧹 Evitar nombres raros
        "--restrict-filenames",

        "-o", f"{carpeta}/%(uploader)s/%(title).80s.%(ext)s",
        url
    ]

    ok = ejecutar(comando)

    if ok:
        print("Descarga exitosa")
    else:
        print("Error al descargar")


def preparar_carpeta():
    fecha = datetime.now().strftime("%Y-%m-%d")
    ruta = os.path.join(CARPETA_BASE, fecha)
    os.makedirs(ruta, exist_ok=True)
    return ruta


def descargar(url):
    url = limpiar_url(url)
    carpeta = preparar_carpeta()

    print("Guardando en:", carpeta)

    if "tiktok.com" in url:
        print("Detectado TikTok")
        descargar_con_yt_dlp(url, carpeta)

    elif "instagram.com" in url:
        print("Detectado Instagram")
        descargar_con_yt_dlp(url, carpeta)

    else:
        print("URL no soportada")


if __name__ == "__main__":
    url = input("Coloca la URL del video: ")
    descargar(url)