# MIS 310 - Midterm Project 2
# Uses functions, lists, loops, conditionals, exceptions, and Tkinter.
from tkinter import *
from PIL import Image, ImageTk
import pandas as pd
import os

folder = os.path.dirname(os.path.abspath(__file__))
window = Tk()
window.title("CCSU Mobile App")
window.geometry("1000x850")
window.resizable(False, False)
window.configure(bg="light blue")

# Keep the CSV and logo1.png (or logo2.png) beside this Python file.
data = pd.DataFrame()
data_error = ""
try:
    data = pd.read_csv(
        os.path.join(folder, "CCSU_Fall_2026_Academic_Calendar.csv"),
        encoding="utf-8-sig")
    if ("CalendarDate" not in data.columns
            or "Buildings" not in data.columns
            or "FacultyName" not in data.columns):
        data_error = "The CSV must contain CalendarDate, Buildings, and FacultyName."
except pd.errors.EmptyDataError:
    data_error = "The calendar CSV is empty."
except (OSError, UnicodeError, pd.errors.ParserError):
    data_error = "Cannot read the calendar CSV. Keep it in the same folder as this program."

logo_loaded = False
for logo_name in ["logo1.png", "logo1.PNG", "logo2.png", "logo2.PNG"]:
    try:
        img = Image.open(os.path.join(folder, logo_name))
        img = img.resize((100, 100))
        img = img.convert("RGBA")
        new_pixels = []
        for pixel in img.getdata():
            if pixel[:3] == (255, 255, 255):
                new_pixels.append((255, 255, 255, 0))
            else:
                new_pixels.append(pixel)
        img.putdata(new_pixels)
        logo = ImageTk.PhotoImage(img)
        Label(window, image=logo, bg="light blue").place(x=20, y=12)
        logo_loaded = True
        break
    except (OSError, ValueError):
        continue

if not logo_loaded:
    Label(window, text="Add logo1.png\nto this folder", bg="light blue",
          fg="red", font=("Arial", 10)).place(x=15, y=35)

Label(window, text="CCSU Mobile App", font=("Arial", 22, "bold"),
      bg="light blue", fg="navy").place(x=145, y=28)
Label(window, text="Central Connecticut State University",
      font=("Arial", 12), bg="light blue").place(x=147, y=72)

# Every button replaces the text in this one Label, preventing overlapping output.
output = Label(window, text="Select a button to view information.",
               font=("Arial", 11), bg="light blue", fg="black",
               justify=LEFT, anchor=NW, padx=10, pady=10,
               relief="groove", borderwidth=2)
output.place(x=20, y=215, width=960, height=615)


def show_column(column_name, heading):
    if data_error != "":
        output.config(text=data_error, bg="light blue", fg="red")
        return
    text = heading + "\n\n"
    count = 0
    # Select one column and remove missing values, as in the starter code.
    df = pd.DataFrame(data, columns=[column_name])
    selected_rows = df[~df[column_name].isnull()]
    for value in selected_rows[column_name]:
        value = str(value)
        if value.strip() != "":
            text = text + value.strip() + "\n"
            count = count + 1
    if count == 0:
        text = text + "No information is available."
    output.config(text=text.rstrip(), bg="light blue", fg="black")


def calendar():
    show_column("CalendarDate", "Fall 2026 Academic Calendar")


def buildings():
    show_column("Buildings", "Campus Buildings")


def faculty():
    show_column("FacultyName", "Faculty")


Button(window, text="Calendar", command=calendar, bg="light green",
       font=("Arial", 11), width=16, pady=8).place(x=20, y=130)
Button(window, text="Buildings", command=buildings, bg="light green",
       font=("Arial", 11), width=16, pady=8).place(x=200, y=130)
Button(window, text="Faculty", command=faculty, bg="light green",
       font=("Arial", 11), width=16, pady=8).place(x=380, y=130)

# Part Two adds two lists and two buttons to the Part One program.
school_subjects = ["Accounting", "Finance", "Management & Organization",
                   "Marketing", "Management Information Systems (MIS)",
                   "Business Analytics"]
mis_courses = ["Intro to MIS", "Intro to MIS", "Databases Management",
               "Systems Analysis & Design",
               "Business Analytics / Data Visualization",
               "Network and Information Security", "Project Management"]


def school_of_business():
    text = "School of Business\n\n"
    for subject in school_subjects:
        text = text + subject + "\n"
    output.config(text=text.rstrip(), bg="light yellow", fg="black")


def mis_department():
    text = "MIS Department\n\n"
    for course in mis_courses:
        text = text + course + "\n"
    output.config(text=text.rstrip(), bg="light pink", fg="black")


Button(window, text="School of Business", command=school_of_business,
       bg="light yellow", font=("Arial", 11), width=22, pady=8).place(x=20, y=180)
Button(window, text="MIS Department", command=mis_department,
       bg="light pink", font=("Arial", 11), width=22, pady=8).place(x=250, y=180)
# Allow space below the second row of buttons.
output.place(x=20, y=240, width=960, height=590)

if __name__ == "__main__":
    window.mainloop()

