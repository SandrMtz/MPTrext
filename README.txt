# Descargador de Canciones y Letras

Este proyecto es una aplicación de escritorio en Python que permite descargar el audio y la letra de una canción 
ingresando el título y el artista. Utiliza la biblioteca `tkinter` para la interfaz gráfica y se ejecuta de manera 
asíncrona para mantener la interfaz responsiva durante las descargas.

## Funcionalidades

- **Interfaz Gráfica**: Una ventana fácil de usar para ingresar el título de la canción y el artista.
- **Descargas Asíncronas**: Utiliza hilos para descargar el audio y la letra sin bloquear la interfaz de usuario.
- **Barra de Progreso**: Muestra el progreso de las descargas, permitiendo al usuario visualizar el estado de la operación.
- **Limpieza de Campos**: Los campos de entrada se limpian automáticamente después de una descarga exitosa.
- **Botón de Salir**: Permite cerrar la aplicación fácilmente.

## Requisitos

- Python 3.x
- Bibliotecas: 
  - `tkinter`
  - `ttk`
  - `threading`
  - `yt_dlp` (para descargar audio de YouTube)
  - `lyricsgenius` (para obtener letras de canciones)

Asegúrate de que las funciones `download_audio` y `download_lyrics` estén correctamente implementadas en el módulo `Funciones`.

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener Python instalado en tu sistema.
3. Abre una terminal y navega al directorio del proyecto.
4. Instala las bibliotecas necesarias usando pip:

   ```bash
   pip install yt-dlp lyricsgenius
