from tkinter import *
from tkinter.ttk import Progressbar
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import os
import time
import shutil
global a , b


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x700+100+50")
        self.root.resizable(False, False)

        def main_page():
            frame_login = Frame(self.root, bg="white")
            frame_login.place(x=330, y=150, width=500, height=400)

            Label(frame_login, text="file transfer system", font=("Impact", 30, "bold"), fg="#6162FF",
                  bg="white").place(
                x=75,
                y=30)
            Label(frame_login, text="transfer type", font=("Goudy old style", 15, "bold"), fg="#1d1d1d",
                  bg="white").place(x=190, y=100)
            Button(frame_login, cursor="hand2", text="Even", bd=0, command=to_even,
                   font=("Goudy old style", 15), bg="#6162FF", fg="white").place(x=50, y=150, width=180,
                                                                                 height=40)
            Button(frame_login, cursor="hand2", text="IDF", bd=0, command=to_idf,
                   font=("Goudy old style", 15), bg="#6162FF", fg="white").place(x=255, y=150, width=180,
                                                                                 height=40)
            Button(frame_login, cursor="hand2", text="Both", bd=0, command=to_both,
                   font=("Goudy old style", 15), bg="#6162FF", fg="white").place(x=255, y=200, width=180,
                                                                                 height=40)

        def both_t_page():
            Register = Frame(root, bg="white", )
            Register.place(x=330, y=150, width=500, height=400)


            def prog():
                def start():
                    GB = 100
                    download = 0
                    speed = 1
                    while (download < GB):
                        time.sleep(0.09)
                        bar['value'] += (speed / GB) * 100
                        download += speed
                        percent.set(str(int((download / GB) * 100)) + "%" + "Uploading files")
                        text.set(str(download) + "/" + str(GB) + " Uploading files")
                        root.update_idletasks()



                percent = StringVar()
                text = StringVar()
                bar = Progressbar(root, orient=HORIZONTAL, length=220)
                bar.place(x= 450, y=340)
                Label(self.root, textvariable=percent, bg="white").place(x=700, y=340)
                #Label(self.root, textvariable=text, bg="white").place(x=500, y=370)
                start()
                messagebox.showinfo(title=None, message="files uploaded successfully")
                main_page()

            def files():
                root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                                           filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
                print(root.filename)
                #shutil.copyfile(root.filename, rf"\\mnhazfs\nonword\halbanot\Both\{directory_name}\{directory_whoto}" )






            Label(text="Both", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=500, y=180)
            Button(cursor="hand2", text="Return", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=600, y=475, width=100, height=40)
            Button(cursor="hand2", text="Upload files", bd=0, command=files, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=600, y=400, width=100, height=40)
            Button(cursor="hand2", text="Confirm", bd=0, command=prog, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=450, y=475, width=100, height=40)
            Label(text="Drag Files here", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=480, y=250)

        def even_t_page():
            Register = Frame(self.root, bg="white", )
            Register.place(x=330, y=150, width=500, height=400)
            Label(text="Both", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=500, y=180)
            Button(cursor="hand2", text="Return", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=600, y=475, width=100, height=40)
            Button(cursor="hand2", text="Confirm", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=450, y=475, width=100, height=40)
            Label(text="Drag Files here", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=480, y=250)

        def idf_t_page():
            Register = Frame(self.root, bg="white", )
            Register.place(x=330, y=150, width=500, height=400)
            Label(text="Both", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=500, y=180)
            Button(cursor="hand2", text="Return", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=600, y=475, width=100, height=40)
            Button(cursor="hand2", text="Confirm", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=450, y=475, width=100, height=40)
            Label(text="Drag Files here", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=480, y=250)

        def to_both():
            Register = Frame(self.root, bg="white", )
            Register.place(x=330, y=150, width=500, height=400)
            self.whoto = Entry(font=("Goudy old style", 15), bg="#E7E6E6")
            self.whoto.place(x=470, y=390)
            self.name = Entry(font=("Goudy old style", 15), bg="#E7E6E6")
            self.name.place(x=470, y=310)

            def create_folder():
                parent_dir = rf"\\mnhazfs\nonword\halbanot\Both"
                directory_name = self.name.get()
                final = os.path.isdir(rf"\\mnhazfs\nonword\halbanot\Both\{directory_name}")
                if not final:
                    os.mkdir(rf"\\mnhazfs\nonword\halbanot\Both\{directory_name}")
                directory_whoto = self.whoto.get()
                parent_dir2 = rf"\\mnhazfs\nonword\halbanot\Both\{directory_name}"
                final2 = os.path.isdir(rf"\\mnhazfs\nonword\halbanot\Both\{directory_name}\{directory_whoto}")
                if not final2:
                    os.mkdir(rf"\\mnhazfs\nonword\halbanot\Both\{directory_name}\{directory_whoto}")
                both_t_page()

            Button(cursor="hand2", text="Confirm", bd=0, command=create_folder, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=450, y=475, width=100, height=40)

            Label(text="Even & IDF", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=470, y=180)
            Button(cursor="hand2", text="Return", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=630, y=475, width=100, height=40)
            Label(text="Your name: ", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=520, y=280)

            Label(text="Who receives: ", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=520, y=350)

        def to_even():
            Register = Frame(self.root, bg="white", )
            Register.place(x=330, y=150, width=500, height=400)
            self.whoto = Entry(font=("Goudy old style", 15), bg="#E7E6E6")
            self.whoto.place(x=470, y=390)
            self.name = Entry(font=("Goudy old style", 15), bg="#E7E6E6")
            self.name.place(x=470, y=310)

            def create_folder():
                parent_dir = rf"\\mnhazfs\nonword\halbanot\Even"
                directory_name = self.name.get()
                final = os.path.isdir(rf"\\mnhazfs\nonword\halbanot\Even\{directory_name}")
                if not final:
                    os.mkdir(rf"\\mnhazfs\nonword\halbanot\Even\{directory_name}")
                directory_whoto = self.whoto.get()
                parent_dir2 = rf"\\mnhazfs\nonword\halbanot\Even\{directory_name}"
                final2 = os.path.isdir(rf"\\mnhazfs\nonword\halbanot\Even\{directory_name}\{directory_whoto}")
                if not final2:
                    os.mkdir(rf"\\mnhazfs\nonword\halbanot\Even\{directory_name}\{directory_whoto}")
                even_t_page()

            Label(text="Even", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=529, y=180)
            Button(cursor="hand2", text="Return", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=600, y=475, width=100, height=40)
            Button(cursor="hand2", text="Confirm", bd=0, command=create_folder, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=450, y=475, width=100, height=40)
            Label(text="Your name: ", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=530, y=280)
            Label(text="Who receives: ", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=530, y=350)

        def to_idf():
            Register = Frame(self.root, bg="white", )
            Register.place(x=330, y=150, width=500, height=400)
            self.whoto = Entry(font=("Goudy old style", 15), bg="#E7E6E6")
            self.whoto.place(x=470, y=390)
            self.name = Entry(font=("Goudy old style", 15), bg="#E7E6E6")
            self.name.place(x=470, y=310)

            def create_folder():
                parent_dir = rf"\\mnhazfs\nonword\halbanot\IDF"
                directory_name = self.name.get()
                final = os.path.isdir(rf"\\mnhazfs\nonword\halbanot\IDF\{directory_name}")
                if not final:
                    os.mkdir(rf"\\mnhazfs\nonword\halbanot\IDF\{directory_name}")
                directory_whoto = self.whoto.get()
                parent_dir2 = rf"\\mnhazfs\nonword\halbanot\IDF\{directory_name}"
                final2 = os.path.isdir(rf"\\mnhazfs\nonword\halbanot\IDF\{directory_name}\{directory_whoto}")
                if not final2:
                    os.mkdir(rf"\\mnhazfs\nonword\halbanot\IDF\{directory_name}\{directory_whoto}")
                idf_t_page()

            Button(cursor="hand2", text="Confirm", bd=0, command=create_folder, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=450, y=475, width=100, height=40)

            Label(text="IDF", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=540, y=180)
            Button(cursor="hand2", text="Return", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=600, y=475, width=100, height=40)
            Label(text="Your name: ", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=520, y=280)

            Label(text="Who receives: ", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=510, y=350)
        main_page()


root = Tk()

# Open Image
bg_pic = Image.open("idk.jpg")
# Resized Image
resized = bg_pic.resize((1199, 850), Image.ANTIALIAS)

bg = ImageTk.PhotoImage(resized)
label_bgImage = Label(root, image=bg)
label_bgImage.place(x=0, y=0)
obj = Login(root)
root.mainloop()
