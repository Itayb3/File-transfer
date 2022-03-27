from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os


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
                x=55,
                y=30)
            Label(frame_login, text="transfer type", font=("Goudy old style", 15, "bold"), fg="#1d1d1d",
                  bg="white").place(x=190, y=100)
            Button(frame_login, cursor="hand2", text="Even", bd=0,command=to_even,
                   font=("Goudy old style", 15), bg="#6162FF", fg="white").place(x=50, y=150, width=180,
                                                                                 height=40)
            Button(frame_login, cursor="hand2", text="IDK", bd=0,command=to_idk,
                   font=("Goudy old style", 15), bg="#6162FF", fg="white").place(x=255, y=150, width=180,
                                                                                 height=40)
            Button(frame_login, cursor="hand2", text="Both", bd=0, command=to_both,
                   font=("Goudy old style", 15), bg="#6162FF", fg="white").place(x=255, y=200, width=180,
                                                                                 height=40)
            Label(frame_login, text="this system was made by:", font=("Goudy old style", 15, "bold"),
                  fg="#1d1d1d",
                  bg="white").place(x=100, y=350)

        def both_t_page():
            Register = Frame(self.root, bg="white", )
            Register.place(x=330, y=150, width=500, height=400)
            Label(text="Both", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=500, y=180)
            Button(cursor="hand2", text="Return", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=600, y=475, width=100, height=40)
            Button(cursor="hand2", text="Confirm", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=450, y=475, width=100, height=40)
            Label(text="Drag Files here", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=480, y=250)

        def even_t_page():
            Register = Frame(self.root, bg="white", )
            Register.place(x=330, y=150, width=500, height=400)
            Label(text="Even", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=550, y=180)
            Button(cursor="hand2", text="Return", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=600, y=475, width=100, height=40)
            Button(cursor="hand2", text="Confirm", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=450, y=475, width=100, height=40)
            Label(text="Drag Files here", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=500, y=250)

        def idk_t_page():
            Register = Frame(self.root, bg="white", )
            Register.place(x=330, y=150, width=500, height=400)
            Label(text="IDK", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=500, y=180)
            Button(cursor="hand2", text="Return", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=600, y=475, width=100, height=40)
            Button(cursor="hand2", text="Confirm", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=450, y=475, width=100, height=40)
            Label(text="Drag Files here", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=480, y=250)



        def to_both():
            Register = Frame(self.root, bg="white", )
            Register.place(x=330, y=150, width=500, height=400)
            self.whoto = Entry(font=("Goudy old style", 15), bg="#E7E6E6").place(x=470, y=390)
            self.name = Entry(font=("Goudy old style", 15), bg="#E7E6E6").place(x=470, y=310)
            print(self.name)
            print(self.whoto)

            def create_folder():
                parent_dir = rf"\\\\TestDomain\\nonword\\"
                directory_name = self.name.get()
                path = os.path.join(parent_dir, directory_name)
                os.mkdir(path)
                directory_whoto = self.whoto.get()

                parent_dir2 = rf"\\\\TestDomain\\nonword\\{directory_name}\\"
                path1 = os.path.join(parent_dir2, directory_whoto)
                os.mkdir(path1)
                both_t_page()


            Button(cursor="hand2", text="Confirm", bd=0, command=create_folder, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=450, y=475, width=100, height=40)

            Label(text="Even & IDK", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=450, y=180)
            Button(cursor="hand2", text="Return", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=600, y=475, width=100, height=40)
            Label(text="Your name: ", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=530, y=280)

            Label(text="Who receives: ", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=530, y=350)


        def to_even():
            Register = Frame(self.root, bg="white", )
            Register.place(x=330, y=150, width=500, height=400)
            self.whoto = Entry(font=("Goudy old style", 15), bg="#E7E6E6").place(x=470, y=390)
            self.name = Entry(font=("Goudy old style", 15), bg="#E7E6E6").place(x=470, y=310)

            def create_folder():
                parent_dir = rf"\\\\TestDomain\\nonword\\"
                directory_name = self.name.get()
                path = os.path.join(parent_dir, directory_name)
                os.mkdir(path)
                directory_whoto = self.whoto.get()

                parent_dir2 = rf"\\\\TestDomain\\nonword\\{directory_name}\\"
                path1 = os.path.join(parent_dir2, directory_whoto)
                os.mkdir(path1)
                both_t_page()

            Label(text="Even", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=550, y=180)
            Button(cursor="hand2", text="Return", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=600, y=475, width=100, height=40)
            Button(cursor="hand2", text="Confirm", bd=0, command=create_folder, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=450, y=475, width=100, height=40)
            Label(text="Your name: ", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=530, y=280)
            Label(text="Who receives: ", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=530, y=350)

        def to_idk():
            Register = Frame(self.root, bg="white")
            Register.place(x=330, y=150, width=500, height=400)
            self.whoto= Entry(font=("Goudy old style", 15), bg="#E7E6E6").place(x=470, y=310)
            self.name = Entry(font=("Goudy old style", 15), bg="#E7E6E6").place(x=470, y=390)
            Label(text="IDK", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=500, y=180)
            Button(cursor="hand2", text="Return", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=600, y=475, width=100, height=40)
            Button(cursor="hand2", text="Confirm", bd=0, command=to_idk, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=450, y=475, width=100, height=40)
            Label(text="Your name: ", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=530, y=280)
            Label(text="Who receives: ", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=530, y=350)






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
