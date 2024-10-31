import yt_dlp as youtube_dl
import lyricsgenius

# Reemplaza con tu token de acceso de Genius
genius = lyricsgenius.Genius("_Es-9GximERNodiEX5zBhWOsfmoe5tdn1800vZurm3HdMECm4Y3ijA3aRr2djphS")

def download_audio(title, artist):
    search_query = f"{title} {artist}"
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(title)s.%(ext)s',
        'default_search': 'ytsearch',
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([search_query])
    except Exception as e:
        print(f"Error al descargar el audio: {e}")

def download_lyrics(title, artist):
    try:
        song = genius.search_song(title, artist)
        if song:
            lyrics = song.lyrics
            with open(f"{title} - {artist}.txt", "w", encoding="utf-8") as f:
                f.write(lyrics)
        else:
            print("No se encontró la letra.")
    except Exception as e:
        print(f"Error al descargar la letra: {e}")
