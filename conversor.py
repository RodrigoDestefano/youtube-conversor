import os
import sys
import glob
import socket
from pydub import AudioSegment
from pytube import YouTube
import warnings
import SimpleHTTPServer
import SocketServer

# Remove some warnings
warnings.filterwarnings("ignore")

PORT = "choose a port"

# Catch the IP of your own computer
IP = socket.gethostbyname(socket.gethostname())

def main():

	# Getting the video's url on YouTube
	url = raw_input("URL:")
	yt = YouTube(url)

	# Path where the videos are located
	video_dir = os.path.dirname(os.path.abspath(__file__))

	# Path to where the final file will be placed
	final_path = "choose your path like: /home/user/musics"
	video = yt.title

	# Catch just the video's audio in mp4 format
	aux = yt.streams.filter(only_audio = True).all()

	print("Downloading...")
	aux[0].download(final_path)

	print("Converting the video to mp3 form...")
	os.chdir(final_path)
	extension = ('./*.mp4')

	# Convert the mp4 file to a mp3 file
	for video in glob.glob(extension):
		mp3_filename = os.path.splitext(os.path.basename(video))[0] + '.mp3'
		AudioSegment.from_file(video).export(mp3_filename, format = 'mp3')

	# Delete the format mp4
	cutter = os.listdir(final_path)

	for item in cutter:
		if item.endswith(".mp4"):
			os.remove(item)

	print("Successful Conversion")

	# Just used to write for the user
	ip = socket.gethostbyname(socket.gethostname())
	port = "choose a port"
	print ("Connect your phone to this address " + ip + ":" + port)
	
	# Condition to stop
	print("PRESS Ctrl + c TO EXIT...")

if __name__ == "__main__":
	try:
		main()
		
		# Running a simple server to connect your phone at this HTTP address
		Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
		httpd = SocketServer.TCPServer((IP, PORT), Handler)
		httpd.serve_forever()
		
	except (KeyboardInterrupt):
		print("\nFinished...")
		httpd.socket.close()
		pass
