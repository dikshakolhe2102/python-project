from tkinter import *
from tkinter import messagebox,ttk
import re
import sqlite3

win = Tk()
win.title("Login System")
win.geometry("650x550")
win.config(bg="#EDE7F6")  

# =====================================================
#                Data Base
# ======================================================
try:
    conne=sqlite3.connect('Registration_System.db')
    cursor=conne.cursor()

    # Register table
    cursor.execute('''
    create table if not exists register (
            Name text,
            Email_ID text,
            Mobile_No integer,
            Password text
    )
    ''')

    # Admission table  (ADDED)
    cursor.execute('''
    create table if not exists admission (
        Student_Name text,
        Father_Name text,
        Mother_Name text,
        Gender text,
        DOB text,
        Course text,
        Category text,
        Address text
    )
    ''')

    conne.commit()
except sqlite3.Error as e:
    print("An error occured:",e)

# ---------------- Frames ----------------
login_frame = Frame(win, bg="#EDE7F6")
register_frame = Frame(win, bg="#EDE7F6")
dashboard_frame = Frame(win, bg="#EDE7F6")
admission_frame = Frame(win, bg='#EDE7F6')

for frame in (login_frame, register_frame, dashboard_frame,admission_frame):
    frame.place(x=0, y=0, relwidth=1, relheight=1)

# =================================================
#                   LOGIN PAGE
# =================================================
login_card = Frame(login_frame, bg="#FFFFFF", width=350, height=350, bd=2, relief="ridge")
login_card.place(relx=0.5, rely=0.5, anchor=CENTER)
login_card.pack_propagate(False)

Label(login_card, text="LOGIN", font=("Arial", 18, "bold"),
    bg="#FFFFFF", fg="#6A1B9A").pack(pady=20)

Label(login_card, text="Username", bg="#FFFFFF", fg="#212121").pack(anchor="w", padx=30, pady=(0,5))
login_user = Entry(login_card, width=28, bd=2, bg="#FAFAFA", fg="#212121",
                relief="solid", highlightbackground="#CE93D8", highlightcolor="#6A1B9A")
login_user.pack(pady=(0,10), padx=30, fill="x")

Label(login_card, text="Password", bg="#FFFFFF", fg="#212121").pack(anchor="w", padx=30, pady=(0,5))
login_pass = Entry(login_card, width=28, show="*", bd=2, bg="#FAFAFA", fg="#212121",
                relief="solid", highlightbackground="#CE93D8", highlightcolor="#6A1B9A")
login_pass.pack(pady=(0,15), padx=30, fill="x")

def login():
    u = login_user.get()
    p = login_pass.get()

    if u == "" or p == "":
        messagebox.showwarning("Warning", "All fields required")
        return
    cursor.execute(
        "SELECT * FROM register WHERE Name=? AND Password=?",
        (u, p))
    data = cursor.fetchone()
    if data:
        messagebox.showinfo("Success", "Login Successful")
        dashboard_frame.tkraise()
    else:
        messagebox.showerror("Error", "User not found, please register")
        register_frame.tkraise()

Button(login_card, text="Login", width=20, bg="#8E24AA", fg="#FFFFFF",
    font=('Arial',10,'bold'), command=login).pack(pady=10)

Button(login_card, text="Register", bg="#8E24AA", fg="#FFFFFF",
    font=('Arial',10,'bold'), width=20, command=register_frame.tkraise).pack()

# =================================================
#                 REGISTER PAGE
# =================================================
register_card = Frame(register_frame, bg="#FFFFFF", width=400, height=500, bd=2, relief="ridge")
register_card.place(relx=0.5, rely=0.5, anchor=CENTER)
register_card.pack_propagate(False)

Label(register_card, text="REGISTER", font=("Arial", 18, "bold"),
    bg="#FFFFFF", fg="#6A1B9A").pack(pady=20)

def validate_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

def validate_mobile(mobile):
    return re.match(r'^[6-9]\d{9}$', mobile)

def validate_password(password):
    return re.match(r'^[A-Z][a-z]{5,6}[@#$%!&]\d{2}$', password)

def clear():
    for e in (name_entry, email_entry, mobile_entry, pass_entry, confirm_entry):
        e.delete(0, END)

def register():
    if "" in (name_entry.get(), email_entry.get(), mobile_entry.get(), pass_entry.get(), confirm_entry.get()):
        messagebox.showwarning("Warning", "All fields required")
    elif not validate_email(email_entry.get()):
        messagebox.showerror("Error", "Invalid Email")
    elif not validate_mobile(mobile_entry.get()):
        messagebox.showerror("Error", "Invalid Mobile Number")
    elif not validate_password(pass_entry.get()):
        messagebox.showerror("Error", "Invalid Password Format")
    elif pass_entry.get() != confirm_entry.get():
        messagebox.showerror("Error", "Passwords do not match")
    else:
        cursor.execute('''
            insert into register(Name,Email_ID,Mobile_No,Password)
            values (?,?,?,?)
            ''',(name_entry.get(),email_entry.get(),mobile_entry.get(),pass_entry.get()))
        conne.commit()
        messagebox.showinfo("Success", "Registration Successful")
        clear()
        login_frame.tkraise()

Label(register_card,text="Name",bg="#FFFFFF").pack(anchor="w", padx=30)
name_entry =Entry(register_card)
name_entry.pack(padx=30, fill="x")

Label(register_card, text="Email ID", bg="#FFFFFF").pack(anchor="w", padx=30)
email_entry =Entry(register_card)
email_entry.pack(padx=30, fill="x")

Label(register_card, text="Mobile Number", bg="#FFFFFF").pack(anchor="w", padx=30)
mobile_entry =Entry(register_card)
mobile_entry.pack(padx=30, fill="x")

Label(register_card, text="Password", bg="#FFFFFF").pack(anchor="w", padx=30)
pass_entry = Entry(register_card,show="*")
pass_entry.pack(padx=30, fill="x")

Label(register_card, text="Confirm Password", bg="#FFFFFF").pack(anchor="w", padx=30)
confirm_entry = Entry(register_card,show="*")
confirm_entry.pack(padx=30, fill="x")

Button(register_card, text="Register", width=20, bg="#8E24AA", fg="#FFFFFF",
    font=("Arial",10,"bold"), command=register).pack(pady=10)

Button(register_card, text="Already Registered? Login",
    bg="#FFFFFF", fg="#8E24AA", bd=0,
    font=("Arial",10,"bold"), command=login_frame.tkraise).pack(pady=10)

# =================================================
#                 DASHBOARD
# =================================================
dash_card = Frame(dashboard_frame, bg="#FFFFFF", width=350, height=200, bd=2, relief="ridge")
dash_card.place(relx=0.5, rely=0.5, anchor=CENTER)
dash_card.pack_propagate(False)

Label(dash_card, text="Welcome to Dashboard",
    font=("Arial", 16, "bold"),
    bg="#FFFFFF", fg="#6A1B9A").pack(pady=25)

Button(dash_card, text="Fill admission form", width=25,
    fg="#FFFFFF", bg="#8E24AA",
    font=("Arial",10,"bold"), command=admission_frame.tkraise).pack(pady=10)

Button(dash_card, text="Logout", width=20,
    bg="#D32F2F", fg="#FFFFFF",
    font=("Arial", 11, "bold"),
    command=login_frame.tkraise).pack()

# =================================================
#        ADMISSION FORM 
# ==================================================
admission_card = Frame(admission_frame, bg="#FFFFFF", width=650, height=550, bd=2, relief="ridge")
admission_card.place(relx=0.5, rely=0.5, anchor=CENTER)
admission_card.pack_propagate(False)

Label(admission_card,text="ADMISSION FORM",
    font=("Arial", 13, "bold"),
    bg="#FFFFFF", fg="#6A1B9A").pack(pady=5)

Label(admission_card, text="Student Name", bg="#FFFFFF").place(x=40, y=90)
student_name = Entry(admission_card, width=40)
student_name.place(x=300, y=90)

Label(admission_card, text="Father's Name", bg="#FFFFFF").place(x=40, y=130)
father_name = Entry(admission_card, width=40)
father_name.place(x=300, y=130)

Label(admission_card, text="Mother's Name", bg="#FFFFFF").place(x=40, y=170)
mother_name = Entry(admission_card, width=40)
mother_name.place(x=300, y=170)

Label(admission_card, text="Gender", bg="#FFFFFF").place(x=40, y=210)
gender = ttk.Combobox(admission_card,values=["Male", "Female", "Other"],state="readonly",width=37)
gender.place(x=300, y=210)

Label(admission_card, text="Date of Birth", bg="#FFFFFF").place(x=40, y=250)
dob_entry = Entry(admission_card, width=10)
dob_entry.place(x=300, y=250)

Label(admission_card, text="Course", bg="#FFFFFF").place(x=40, y=290)
course = ttk.Combobox(admission_card,values=["B.A", "B.Com", "B.Sc", "BCA", "BBA"],state="readonly",width=37)
course.place(x=300, y=290)

Label(admission_card, text="Category", bg="#FFFFFF").place(x=40, y=330)
category = ttk.Combobox(admission_card,values=["Open", "OBC", "SC", "ST"],state="readonly",width=37)
category.place(x=300, y=330)

Label(admission_card, text="Permanent Address", bg="#FFFFFF").place(x=40, y=370)
address = Text(admission_card, width=40, height=3)
address.place(x=300, y=370)

agree = IntVar()
Checkbutton(admission_card,
    text="I hereby declare that the information given above is true.",
    variable=agree,
    bg="#FFFFFF").place(x=40, y=450)

def submit_form():
    if course.get() == "Select Course":
        messagebox.showwarning("Warning", "Please select course")
    elif agree.get() == 0:
        messagebox.showerror("Error", "Please accept declaration")
    else:
        cursor.execute('''
            insert into admission
            values (?,?,?,?,?,?,?,?)
        ''',(
            student_name.get(),
            father_name.get(),
            mother_name.get(),
            gender.get(),
            dob_entry.get(),
            course.get(),
            category.get(),
            address.get("1.0",END)
        ))
        conne.commit()
        messagebox.showinfo("Success", "Admission Form Submitted Successfully")
        dashboard_frame.tkraise()

Button(admission_card, text="Submit",
    bg="#8E24AA", fg="#FFFFFF",
    font=("Arial", 10, "bold"),
    width=15,
    command=submit_form).place(x=200, y=490)

Button(admission_card, text="Back",
    bg="#757575", fg="#FFFFFF",
    font=("Arial", 10, "bold"),
    width=15,
    command=dashboard_frame.tkraise).place(x=360, y=490)

# ---------------- Start ----------------
login_frame.tkraise()
win.mainloop()

