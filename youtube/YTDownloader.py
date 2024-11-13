import yt_dlp

def downloadAudio(url):
    ydl_opts = {
        'outtmpl': '/home/victor/YTDowns/%(title)s.%(ext)s',
        'format': 'bestaudio/best',         # Select quality
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',    # Using FFmpeg to extract audio
            'preferredcodec': 'mp3',        # convert to .mp3
            'preferredquality': '192',      # This is the Bitrate
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def downloadVideo(url):
    # I want to ask for path to save
    ydl_opts = {
    'outtmpl': '/home/victor/YTDowns/%(title)s.%(ext)s',
    'format': 'best' # This gets a .mp4 instead of .mkv
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Metadata
# with yt_dlp.YoutubeDL(ydl_ops) as ydl:
#    info_dict = ydl.extract_info(url, download=False)
#    print("Title: "+info_dict['title'])
#    # Print all available metadata with keys to call it
#    #for key, value in info_dict.items():
#    #    print(f'{key}') # Not calling value as it complicates readability

def main():
    while (True):
        print("Random Youtube downloader")        
        print("1. Download video")
        print("2. Download music")
        print("3. Exit")
        try:            
            choice = int(input("Make a choice\n"))
            if choice == 1:
                url = input("Enter full URL:\n")
                downloadVideo(url)
            elif choice == 2:
                url = input("Enter full URL:\n ")
                downloadAudio(url)
            elif choice == 3:
                print("Bye")
                break
            else:
                print("Option not available")
        except ValueError:
            print("Enter a number.")


if __name__ == "__main__":
    main()