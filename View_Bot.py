from tkinter import *
import time
import webbrowser
import ttkbootstrap as ttk

while True:
    def main():
        def Run_button():
            url=urlbox.get()
            duration=timebox.get()
            for i in range(5):
                webbrowser.open(url)
                time.sleep(int(duration))
                


        #Window setup
        root=ttk.Window(themename="cyborg")
        root.geometry("600x400")
        root.resizable(FALSE,FALSE)
        root.title("Youtube Bot")
        #Interaction
        intro_text=Label(root,text="YOUTUBE BOT",font="calibri 20 bold")
        intro_text.pack()
        #url
        url_info=Label(root,text="Input the url link below",font="calibri 12 bold")
        url_info.pack()
        urlbox=Entry(root,width="50")
        urlbox.pack()
        #time
        time_info=Label(root,text="Input the seconds to be run",font="calibri 12 bold")
        time_info.pack()
        timebox_str=IntVar()
        timebox=Entry(root,width="50",textvariable=timebox_str)
        timebox.pack()
        timebox.delete(0,END)
        #run
        run_button=Button(root,text="Start",width=10,height=2,command=Run_button)
        run_button.pack(pady=20)

        root.mainloop()
    main()