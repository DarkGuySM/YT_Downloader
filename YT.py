import os
from pytube import YouTube
url=input("Enter Video\'s URL>>  ")
print("   ")
print("Fetching video details...")
video=YouTube(url)
print("   ")
print("Enter 1, if you want to download video.    \nEnter 2, if you want to download only audio.     \nEnter 3, if you want to see list of all streams [this includes videos which don\'t have audio]")
print("   ")
chk=int(input("Enter>>  "))
if chk==1:
	print("----------------- Video Title ---------------------")
	print(video.title)
	print("   ")
	print("----------------- Available Qualities --------")
	print(video.streams.filter(progressive=True))
	print("---------------------------------------------")
	print("---------------------------------------------")
	print("   ")
	print("Above are the qualities the video is available to download. There is an itag value for each quality. Enter the itag of the video you want to download.")
	print("   ")
	itag=input("Enter itag>  ")
	video=video.streams.get_by_itag(itag)
	print(f"Downloading \"{video.title}\"")
	video.download()
	print("   ")
	print("Download Completed!")
	print("Video Downloaded at Current Directory.")
elif chk==2:
	print("----------------- Video Title ---------------------")
	print(video.title)
	print("   ")
	print("----------------- Available Qualities --------")
	print(video.streams.filter(only_audio=True))
	print("---------------------------------------------")
	print("---------------------------------------------")
	print("   ")
	print("Above are the qualities the audio is available to download. There is an itag value for each quality. Enter the itag of the audio you want to download.")
	print("   ")
	itag=input("Enter itag>  ")
	video=video.streams.get_by_itag(itag)
	print(f"Downloading \"{video.title}\"")
	video.download()
	print("   ")
	print("Download Completed!")
	print("Audio Downloaded at Current Directory.")
	try:
		a=(video.title+".webm")
		b=(video.title+".mp3")
		os.rename(a,b)
	except:
		try:
			a=(video.title+".mp4")
			b=(video.title+".mp3")
			os.rename(a,b)
		except:
			print("   ")
			print("Error renaming the file!\nThe audio file was downloaded successfully, but it couldn\'nt be renamed.  Please manually change file extension to \".mp3\"")
	print("   ")
elif chk==3:
	print("----------------- Video Title ---------------------")
	print(video.title)
	print("   ")
	print("----------------- Available Qualities --------")
	print(video.streams)
	print("---------------------------------------------")
	print("---------------------------------------------")
	print("   ")
	print("Above are the qualities the video is available to download. There is an itag value for each quality. Enter the itag of the video you want to download.")
	print("   ")
	itag=input("Enter itag>  ")
	video=video.streams.get_by_itag(itag)
	print(f"Downloading \"{video.title}\"")
	video.download()
	print("   ")
	try:
		a=(video.title+".webm")
		b=(video.title+".mp3")
		os.rename(a,b)
		print("Download Completed!")
		print("Video/Audio Downloaded at Current Directory.")
	except:
		print("   ")
		print("Error! The stream you chose seems to be an mp4 audio stream. Please manually change file extension to \".mp3\" if it\'s unplayable.")
else:
	print("You entered invalid option, please restart the program and enter a valid option")
