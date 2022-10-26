#
from tkinter import *
import moviepy.editor
import pytube
import pygame

window = Tk()
window.geometry("720x600")
window.title("Skyflix Vault")
window.configure(bg="#212121")

code1,code2,code3 = "2 5 4".split()
file_name = "New Skyflix"

get_number1 = StringVar()
get_number2 = StringVar()
get_number3 = StringVar()
passI = StringVar()

#functions
def clear(window):
    for widgets in window.winfo_children():
        widgets.destroy()

def Vault_pass1_screen():
    def clicked1():
        def clear(window):
            for widgets in window.winfo_children():
                widgets.destroy()

        get_get_number1 = get_number1.get()
        get_get_number2 = get_number2.get()
        get_get_number3 = get_number3.get()

        if get_get_number1 == code1 and get_get_number2 == code2 and get_get_number3 == code3:
            clear(window)
            window.destroy()
            window_root = Tk()
            window_root.title("Skyflix")
            window_root.geometry("720x600")
            window_root.configure(background="#212121")

            spacing = 250
            icon=PhotoImage(file=f"C:\\Users\\Gianclarence Solas\\Desktop\\\{file_name}\\image\\logo.png")
   
            window_root.iconphoto(False,icon)
            page1 = open(f"C:\\Users\\Gianclarence Solas\\Desktop\\{file_name}\\settings\\page1.txt", "r")
            page2 = open(f"C:\\Users\\Gianclarence Solas\\Desktop\\{file_name}\\settings\\page2.txt", "r")
            page3 = open(f"C:\\Users\\Gianclarence Solas\\Desktop\\{file_name}\\settings\\page3.txt", "r")
            page4 = open(f"C:\\Users\\Gianclarence Solas\\Desktop\\{file_name}\\settings\\page4.txt", "r")
            page5 = open(f"C:\\Users\\Gianclarence Solas\\Desktop\\{file_name}\\settings\\page5.txt", "r")
            page6 = open(f"C:\\Users\\Gianclarence Solas\\Desktop\\{file_name}\\settings\\page6.txt", "r")
            page7 = open(f"C:\\Users\\Gianclarence Solas\\Desktop\\{file_name}\\settings\\page7.txt", "r")
            page8 = open(f"C:\\Users\\Gianclarence Solas\\Desktop\\{file_name}\\settings\\page8.txt", "r")

            read = page1.readlines()
            read1 = page2.readlines()
            read2 = page3.readlines()
            read3 = page4.readlines()
            read4 = page5.readlines()
            read5 = page6.readlines()
            read6 = page7.readlines()
            read7 = page8.readlines()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
            catagore1 = "Gumball cat 1"
            catagore2 = "Craig of the Creek"
            catagore3 = "Teen Tians"
            catagore4 = "We Bare Bears"
            catagore5 = "Adventure time 1"
            catagore6 = "Random stuff"
            catagore7 = "Gumball cat 2"
            catagore8 = "Adventure time 2"
            
            #functions
            def a12():
                add_page(catagore1,read)
            def a13():
                add_page(catagore2,read1)
            def a14():
                add_page(catagore3,read2)
            def a15():
                add_page(catagore4,read3)
            def a16():
                add_page(catagore5,read4)
            def a17():
                add_page(catagore6,read5)
            def a18():
                add_page(catagore7,read6)
            def a19():
                add_page(catagore8,read7)
                
            #show channel
            def show_chanel():
                clear(window_root)
                window_root.title("Skyflix")
                Lbl = Label(text="Skyflix", font=("BebasNeue",30), fg="#0091ea", bg="#212121")
                btn = Button(text="⬅️", font=("Bold", 10), command=start_page, width=10)
                Lbl.place(x=300,y=0)
                btn.place(x=0,y=50)
                add_catagore(catagore1, 0, 500, a12)
                add_catagore(catagore2, spacing, 500, a13)
                add_catagore(catagore3, spacing + spacing, 500, a14)
                add_catagore(catagore4, 0, 470, a15)
                add_catagore(catagore5, 250, 470, a16)
                add_catagore(catagore6, 0, 440, a17)
                add_catagore(catagore7, 500, 470, a18)
                add_catagore(catagore8, 250, 440, a19)
                
            #functions
            def add_catagore(text, x, y, cmd):
                lbl = Button(text=text, width=30, height=-30, command=cmd)
                lbl.place(x=x, y=y)
                
            def clear(window):
                for widgets in window.winfo_children():
                    widgets.destroy()
                    
            def add_video(text, x, y, command):
                btn = Button(text=text, command=command, width=70, height=2, foreground="#eeeeee", background="#242424")
                btn.place(x=x,y=y)
                
            def download_video(link):
                video_url = link   
                youtube = pytube.YouTube(video_url)
                video = youtube.streams.get_highest_resolution()
                video.download(f"C:\\Users\\Gianclarence Solas\\Desktop\\{file_name}\\videos")
                
                    
            def get_title(link):
                yt = pytube.YouTube(link)
                return yt.title
            
            def show_video(link):
                pygame.init()
                pygame.display.set_caption("Skyflix")
                video = moviepy.editor.VideoFileClip(link)
                video.preview()
                pygame.quit()
                    
            def start_page():
                clear(window_root)
                Lbl = Label(text="Skyflix", font=("BebasNeue",40), fg="#0091ea", bg="#242424")
                btn = Button(window_root, text="Shows", command=show_chanel, font=("Arial", 30), width="10", height="1")
                btn1 = Button(text="Log out", font=("BebasNeue",20), fg="#eeeeee", bg="#212121", command=window_root.destroy)
                btn1.place(x=600,y=0)
                btn.place(x=240,y=100)
                Lbl.place(x=280,y=0)
            
            def add_page(Channel_name, catagore):
                def add_act(cat):
                    link123 = catagore[cat]
                    download_video(link123)
                    title = get_title(link123)
                    title = title.replace("|","")
                    title = title.replace("'","")
                    title = title.replace("?","")
                    title = title.replace(",","")
                    title = title.replace(":","")
                    path = f"C:\\Users\\Gianclarence Solas\\Desktop\\{file_name}\\videos\\{title}.mp4"
                    window_root.title("Skyflix")
                    show_video(path)
                
                render_act = lambda num: add_act(num)
                
                def act1():
                    add_act(0)
                    
                def act2():
                    add_act(1)
                    
                def act3():
                    add_act(2)
                    
                def act4():
                    add_act(3)
                    
                def act5():
                    add_act(4)
                    
                def act6():
                    add_act(5)
    
                def act7():
                    add_act(6)

                clear(window_root)
                window_root.title(Channel_name + " Category")
                lbl = Label(text=Channel_name + " Category", fg="white", bg="#212121", font=("bold", 20))

                #bindings
                lbl.place(x=0,y=0)
                add_video(get_title(catagore[0]), 0,50, act1)
                add_video(get_title(catagore[1]), 0,50*2, act2)
                add_video(get_title(catagore[2]), 0,50*3, act3)
                add_video(get_title(catagore[3]), 0,50*4, act4)
                add_video(get_title(catagore[4]), 0,50*5, act5)
                add_video(get_title(catagore[5]), 0,50*6, act6)
                add_video(get_title(catagore[6]), 0,50*7, act7)
                add_video("Back to homepage", 0,400, show_chanel)
 
            #pages_cortis1
            print("Started Version 3.0 origenal")
            start_page()
            window_root.mainloop()      

    clear(window)
    btn = Button(text="Enter", command=clicked1, font=("Bold"), width=10)
    sp1 = Spinbox(window, from_= 0, to = 20,width=2,textvariable=get_number1, font=(40))
    sp2 = Spinbox(window, from_= 0, to = 20,width=2,textvariable=get_number2, font=(40))
    sp3 = Spinbox(window, from_= 0, to = 20,width=2,textvariable=get_number3, font=(40))
    sp1.place(x=300,y=200)
    sp2.place(x=300+30,y=200)
    sp3.place(x=300+30*2,y=200)
    btn.place(x=300, y=250)

if __name__ == "__main__":
    Vault_pass1_screen()
    window.mainloop()