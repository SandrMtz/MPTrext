# Código sin interfaz gráfica
 
# from Funciones import download_audio, download_lyrics

# if __name__ == "__main__":
#     title = input("Introduce el título de la canción: ")
#     artist = input("Introduce el artista: ")
#     download_audio(title, artist)
#     download_lyrics(title, artist)

#------------------------------

# Código con interfaz gráfica

import tkinter as tk
from tkinter import messagebox, ttk
from threading import Thread
from time import sleep  # Simulación de tiempo de descarga
from Funciones import download_audio, download_lyrics

def download():
    title = title_entry.get()
    artist = artist_entry.get()
    
    if title and artist:
        download_thread = Thread(target=perform_download, args=(title, artist))
        download_thread.start()
    else:
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")

def perform_download(title, artist):
    progress_bar.start()
    
    try:
        # Simulación de la descarga
        download_audio(title, artist)  # Aquí llamas a tu función de descarga
        for _ in range(5):  # Simula el progreso de la descarga
            sleep(1)  # Simula el tiempo que toma descargar
            progress_bar['value'] += 20  # Incrementa el progreso

        download_lyrics(title, artist)  # Aquí llamas a tu función de descarga
        for _ in range(5):  # Simula el progreso de la letra
            sleep(1)  # Simula el tiempo que toma descargar
            progress_bar['value'] += 20  # Incrementa el progreso
            
        messagebox.showinfo("Éxito", "La canción y la letra han sido descargadas.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")
    finally:
        progress_bar.stop()
        progress_bar['value'] = 0  # Reinicia la barra de progreso
        title_entry.delete(0, tk.END)  # Limpia el campo del título
        artist_entry.delete(0, tk.END)  # Limpia el campo del artista

def exit_app():
    root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Descargar Canción y Letra")

# Crear etiquetas y entradas
tk.Label(root, text="Título de la Canción:").pack(pady=5)
title_entry = tk.Entry(root, width=50)
title_entry.pack(pady=5)

tk.Label(root, text="Artista:").pack(pady=5)
artist_entry = tk.Entry(root, width=50)
artist_entry.pack(pady=5)

# Crear barra de progreso
progress_bar = ttk.Progressbar(root, length=300, mode='determinate')
progress_bar.pack(pady=20)

# Crear botón para descargar
download_button = tk.Button(root, text="Descargar", command=download)
download_button.pack(pady=20)

# Crear botón para salir
exit_button = tk.Button(root, text="Salir", command=exit_app)
exit_button.pack(pady=5)

# Iniciar el bucle principal
root.mainloop()
