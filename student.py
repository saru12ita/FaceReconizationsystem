import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First image
        img = Image.open(r"C:\Users\dell\Downloads\projectimages\students1.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Second image
        img1 = Image.open(r"C:\Users\dell\Downloads\projectimages\student3.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=500, height=130)

        # Third image
        img2 = Image.open(r"C:\Users\dell\Downloads\projectimages\student2.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1000, y=0, width=550, height=130)

        # Background image
        img3 = Image.open(r"C:\Users\dell\Downloads\projectimages\faceo.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("arial", 35, "bold"), bg="red", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=12, y=55, width=1500, height=600)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("arial", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"C:\Users\dell\Downloads\projectimages\student4.jpg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl2 = Label(Left_frame, image=self.photoimg_left)
        f_lbl2.place(x=5, y=0, width=720, height=130)

        # current  course Information
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                          text="Current Course Information", font=("arial", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=150)

        # Department
        dep_label = Label(current_course_frame, text="Department", font=("arial", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(current_course_frame, font=("arial", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "Software", "Computer", "Civil", "IT")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("arial", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, font=("arial", 12, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("arial", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, font=("arial", 13, "bold"), state="readonly", width=20)
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("arial", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, font=("arial", 13, "bold"), state="readonly", width=20)
        semester_combo["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3")
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)


        # class stusdent Information
        class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                          text="class stusdent Information", font=("arial", 12, "bold"))
        class_Student_frame.place(x=5, y=250, width=720, height=300)



        



        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                 font=("arial", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)


if __name__ == "__main__":
    root = tk.Tk()
    obj = Student(root)
    root.mainloop()
