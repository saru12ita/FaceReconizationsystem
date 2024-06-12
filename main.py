import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

class Face_Reconization_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First image
        img = Image.open(r"C:\Users\dell\Downloads\projectimages\harvard.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Second image
        img1 = Image.open(r"C:\Users\dell\Downloads\projectimages\facereco2.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=500, height=130)

        # Third image
        img2 = Image.open(r"C:\Users\dell\Downloads\projectimages\facereco3.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1000, y=0, width=550, height=130)

        # Background image
        img3 = Image.open(r"C:\Users\dell\Downloads\projectimages\bgimage.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)  # Corrected to self.photoimg3
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("arial", 35, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Student button
        img4 = Image.open(r"C:\Users\dell\Downloads\projectimages\student.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", cursor="hand2", font=("arial", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        # Detect Face button
        img5 = Image.open(r"C:\Users\dell\Downloads\projectimages\facereco1.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b2.place(x=500, y=100, width=220, height=220)

        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2", font=("arial", 15, "bold"), bg="red", fg="white")
        b2_1.place(x=500, y=300, width=220, height=40)

        # Attendance button
        img6 = Image.open(r"C:\Users\dell\Downloads\projectimages\attendance.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b3.place(x=800, y=100, width=220, height=220)

        b3_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("arial", 15, "bold"), bg="red", fg="white")
        b3_1.place(x=800, y=300, width=220, height=40)

        # Help Desk button
        img7 = Image.open(r"C:\Users\dell\Downloads\projectimages\helpdesk.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b4.place(x=1100, y=100, width=220, height=220)

        b4_1 = Button(bg_img, text="Help Desk", cursor="hand2", font=("arial", 15, "bold"), bg="red", fg="white")
        b4_1.place(x=1100, y=300, width=220, height=40)

        # Train Data button
        img8 = Image.open(r"C:\Users\dell\Downloads\projectimages\traindata.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        b5.place(x=200, y=380, width=220, height=220)

        b5_1 = Button(bg_img, text="Train Data", cursor="hand2", font=("arial", 15, "bold"), bg="red", fg="white")
        b5_1.place(x=200, y=580, width=220, height=40)

        # Photos button
        img9 = Image.open(r"C:\Users\dell\Downloads\projectimages\photo.jpg")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2")
        b6.place(x=500, y=380, width=220, height=220)

        b6_1 = Button(bg_img, text="Photos", cursor="hand2", font=("arial", 15, "bold"), bg="red", fg="white")
        b6_1.place(x=500, y=580, width=220, height=40)

        # Developer button
        img10 = Image.open(r"C:\Users\dell\Downloads\projectimages\developer.jpg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b7.place(x=800, y=380, width=220, height=220)

        b7_1 = Button(bg_img, text="Developer", cursor="hand2", font=("arial", 15, "bold"), bg="red", fg="white")
        b7_1.place(x=800, y=580, width=220, height=40)

        # Exit button
        img11 = Image.open(r"C:\Users\dell\Downloads\projectimages\exit.jpg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b8.place(x=1100, y=380, width=220, height=220)

        b8_1 = Button(bg_img, text="EXIT", cursor="hand2", font=("arial", 15, "bold"), bg="red", fg="white")
        b8_1.place(x=1100, y=580, width=220, height=40)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Reconization_System(root)
    root.mainloop()
