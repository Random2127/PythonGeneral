import yt_dlp

url = "https://www.youtube.com/watch?v=igKXRrb5_ts"


# Learning to download ".mp3"


ydl_opts = {
    'outtmpl': '/home/victor/YTDowns/%(title)s.%(ext)s',
    'format': 'bestaudio/best',         # Select quality
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',    # Using FFmpeg to extract audio
        'preferredcodec': 'mp3',        # convert to .mp3
        'preferredquality': '192',      # This is the Bitrate
    }],
    
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])




# Learning to download ".mp4" videos 

## Path to save the video
#ydl_opts = {
#    'outtmpl': '/home/victor/YTDowns/%(title)s.%(ext)s',
#    'format': 'best' # This gets a .mp4 instead of .mkv
#}
## Create the object to interact with YT's video
#with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#    ydl.download([url])


#Figuring out how to get metadata

#with yt_dlp.YoutubeDL(ydl_ops) as ydl:
#	# This line indicates only to download metadata
#    info_dict = ydl.extract_info(url, download=False)
#    print("Title: "+info_dict['title'])
#    # Print all available metadata with keys to call it
#    #for key, value in info_dict.items():
#    #    print(f'{key}: {value}') # Not calling value as it complicates readability
    

