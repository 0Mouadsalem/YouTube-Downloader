from tkinter import *
import pytube

#Main screen
master = Tk()
master.configure(bg="white")
master.title("Mouad YouTube Downloader")
img = PhotoImage(file="logo.PNG")

#function
def download():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        Video   = youtube.streams.first()
        Video.download("C:/Users/Utilisateur/Desktop/Mouad_YT_Downloader")
        notif.config(fg="darkgreen", bg="white",text="Download Complete")
    except Exception as e:
        print(e)    
        notif.config(fg="darkred", bg="white",text="video could not be fond / download")

#labels
Label(master, image=img).grid(sticky=N,padx=100,row=0)
Label(master, text="YouTube Converter", fg="Black", bg="white", font=("calibri",25)).grid(sticky=N,padx=100,row=1)
Label(master, text="Please enter the LINK : ", fg="Gray8", bg="white", font=("calibri",16)).grid(sticky=N,row=2,pady=15)

notif = Label(master, bg="white", font=("calibri",14))
notif.grid(sticky=N,padx=100,row=5)

#variables
url = StringVar()

#entry
Entry(master,width=50,textvariable=url, fg="Black", bg="gray86").grid(sticky=N,row=3)

#Button
Button(master,width=20,text="Download", fg="black", bg="lightcyan3",font=("calibri",14,),command=download).grid(sticky=N,row=4,pady=15)

master.mainloop()
