from moviepy.editor import *

def compress_video(input_file, output_file):
    # Carrega o vídeo de entrada
    video = VideoFileClip(input_file)

    # Reduz o tamanho do vídeo para 480p
    video_resized = video.resize(height=480)

    # Define a taxa de quadros para 30 fps
    video_fps = video_resized.set_fps(30)

    # Comprime o vídeo usando o codec h.264
    video_compressed = video_fps.write_videofile(output_file, codec='libx264')

    # Fecha o arquivo de entrada e saída
    video.close()
    video_compressed.close()

# Exemplo de uso
input_file = 'meu_video.mp4'
output_file = 'meu_video_comprimido.mp4'
compress_video(input_file, output_file)
