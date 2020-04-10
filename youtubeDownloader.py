import pytube
import tkinter as tk
from tkinter import filedialog
import time

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

root = tk.Tk()
root.withdraw()

input("Please Select a Location To Save The Downloaded Videos To\nPress Enter to continue...")
videoPath =filedialog.askdirectory()

input("Please Select The Location Of Your Youtube Video Link List Separated By New Lines After Each Link\nPress Enter to continue...")
listPath = filedialog.askopenfilename()
videos = open(listPath, 'r');

count = sum(1 for line in open(listPath))

progressCounter = 0;
printProgressBar(0,count, prefix = 'Progress:', suffix = 'Complete', length = 50)

for line in videos.readlines():
	print("Please Wait While Your Video Is Downloaded")
	video_url = line
	youtube = pytube.YouTube(video_url)
	video = youtube.streams.first()
	video.download(videoPath)
	print(video.title + " downloaded succesfully")
	time.sleep(0.1)
	progressCounter = progressCounter + 1
	printProgressBar(progressCounter,count, prefix = 'Progress:', suffix = 'Complete', length = 50, fill = '█', printEnd = "\n")
	

