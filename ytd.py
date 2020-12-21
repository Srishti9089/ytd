from  pytube import *
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
#linksample=https://www.youtube.com/watch?v=5yYYFEhvBU8
path_to_save_video = ""
fileSizeInBytes = 0
MaxFileSize = 0
def progress(stream=None, chunk=None,file_handle=None,bytes_remaining=None):
    #percent = (100 * (fileSizeInBytes - bytes_remaining)) / fileSizeInBytes

    #dBtn.config(text="{:00.0f} % Downloaded".format(percent))
    pass


def complete():
    loadingLabel.config(text=("Download Complete"))
    loadingLabel.config(text="Developed by || Srishti Verma",font=("Agency FB", 15))
    loadingLabel.config(state=NORMAL)




def startDownload():
    global file_size, MaxFileSize, fileSizeInBytes
    try:
        choice = youtubeChoices.get()
        url = urlField.get()
        print(url)

        # changing button text while downloading
        dBtn.config(text='downloading...')
        dBtn.config(state=DISABLED)
        path_to_save_video = askdirectory()
        print(path_to_save_video)
        if (len(path_to_save_video) > 1):
            fileLocationLabelError.config(text=path_to_save_video,
                                          fg="green")

        else:
            fileLocationLabelError.config(text="Please choose folder!",
                                          fg="red")
            dBtn.config(text="Start download")
            dBtn.config(state=NORMAL)


        # creating youtube object with url....
        ob = YouTube(url, on_progress_callback=progress)
        ob.register_on_complete_callback(complete)
        ob.register_on_progress_callback(progress)

        # strms=ob.streams.all()
        # for s in strms:
        # print(s)
        if (len(url) > 1):
            youtubeEntryError.config(text="")
            print(url, "at", path_to_save_video)
            ob = YouTube(url, on_progress_callback=progress)
            # on_complete_callback=complete
            print("Video Title:\n\n", ob.title)
            if (choice == downloadChoices[0]):
                print("720p Video file downloading...")
                dBtn.config(text="720p Video file downloading...")

                selectedVideo = ob.streams.filter(progressive=True).first()

            elif (choice == downloadChoices[1]):
                print("144p video file downloading...")
                dBtn.config(text="144p Video file downloading...")
                selectedVideo = ob.streams.filter(progressive=True,
                                                  file_extension='mp4').last()

            elif (choice == downloadChoices[2]):
                print("3gp file downloading...")
                dBtn.config(text="3gp Video file downloading...")
                selectedVideo = ob.streams.filter(file_extension='3gp').first()

            elif (choice == downloadChoices[3]):
                print("Audio file downloading...")
                dBtn.config(text="Audio  file downloading...")
                selectedVideo = ob.streams.filter(only_audio=True).first()

            fileSizeInBytes = selectedVideo.filesize
            MaxFileSize = fileSizeInBytes / 1024000
            MB = str(MaxFileSize) + " MB"
            vmsg.config(text=("File Size = {:00.00f} MB".format(MaxFileSize)))
            vtitle.config(text=(selectedVideo.title))

            # now Download ------->
            selectedVideo.download(path_to_save_video)
            # ==========>
            print("Downloaded on:  {}".format(path_to_save_video))
            # loadingLabel.config(text=("Download Complete ",MB))
            complete()

        else:
            youtubeEntryError.config(text="Please paste youtube link",fg="red")
        #strms = ob.streams.first()
        file_size = selectedVideo.filesize
        print(file_size)


        print("video downloaded")
        dBtn.config(text="Start download")
        dBtn.config(state=NORMAL)
        showinfo("Download Finished", " Downloaded Successfully")
        urlField.delete(0, END)
        vmsg.pack_forget()
        vtitle.pack_forget()

    except Exception as e:
        print(e)
        print("Error...!! ")
def startDownloadThread():
    #create thread
    thread=Thread(target=startDownload)
    thread.start()




#gui making
root=Tk()
root.title("MY YTD")
# set icon
root.iconbitmap('download.ico')
root.geometry("500x540")
file=PhotoImage(file='images.png',)
headingIcon=Label(root,image=file)
headingIcon.pack(side=TOP)
#.............
eLabel = Label(root,text="Patse link here: ",font=("verdana", 15))
eLabel.pack()
#url text fiels
urlField=Entry(root,font=("verdana",18),justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=5,pady=5)

#what to download choice
youtubeChooseLabel = Label(root,text="Please Choose Download Quality: ",font=("verdana", 15))
youtubeChooseLabel.pack()
# Combobox with four choices:
downloadChoices = ["MP4_720p",
                   "Mp4_144p",
                   "Video_3gp",
                   "Song_MP3"]

youtubeChoices = ttk.Combobox(root, values=downloadChoices)
youtubeChoices.pack(pady=10)
#button
dBtn=Button(root,text="Start Download",font=("Agency FB",18),relief='ridge',command=startDownloadThread,bg="red")
dBtn.pack(side=TOP,pady=10)
# Entry label if user don`t choose directory
fileLocationLabelError = Label(root,
                               text="", font=("Agency FB", 20))
fileLocationLabelError.pack(pady=(0, 0))
# Progressbar ======>
#progressbar = ttk.Progressbar(root, orient="horizontal",
                              #length=300, mode='indeterminate')
#progressbar.pack(pady=(2, 0))
# =========when link is wrong print this label
youtubeEntryError = Label(root, fg="red",text="", font=("Agency FB", 20))
youtubeEntryError.pack()
#title
vmsg=Label(root,text="")
vmsg.pack()
vtitle=Label(root,text="")
vtitle.pack()
loadingLabel = ttk.Label(root, text="Developed by || Srishti Verma",font=("Agency FB", 15))
loadingLabel.pack()



root.mainloop()