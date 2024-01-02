import os
import subprocess

gif_folder = input("Input file path where gifs are located: ")

for filename in os.listdir(gif_folder):
    if filename.endswith('.gif'):
        gif_path = os.path.join(gif_folder, filename)
        new_filename = os.path.splitext(filename)[0] + '.mp4'
        new_file_path = os.path.join(gif_folder, new_filename)
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', gif_path, '-movflags', 'faststart', '-pix_fmt', 'yuv420p', '-vf', 'scale=trunc(iw/2)*2:trunc(ih/2)*2', new_file_path])

print("Finished!")