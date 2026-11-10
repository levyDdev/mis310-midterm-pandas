# MIS 310 - Midterm Project 1
# Employee records are stored in a list while the program is open.
from tkinter import *

employees = []
selected_employee = -1


def validate_input():
    if name_entry.get().strip() == "":
        message_label.config(text="Enter the employee's full name.", fg="red")
        name_entry.focus_set()
        return False
    elif department.get() == "Select a department":
        message_label.config(text="Select a department.", fg="red")
        return False
    return True


def clear_input():
    global selected_employee
    name_entry.delete(0, END)
    department.set("Select a department")
    full_time.set(0)
    employee_list.selection_clear(0, END)
    selected_employee = -1


def display_employees():
    employee_list.delete(0, END)
    for employee in employees:
        employee_list.insert(END, employee[0] + " | " + employee[1]
                             + " | " + employee[2])


def add_employee():
    if not validate_input():
        return
    if full_time.get() == 1:
        status = "Full-Time"
    else:
        status = "Part-Time"
    employees.append([name_entry.get().strip(), department.get(), status])
    display_employees()
    clear_input()
    message_label.config(text="Employee added successfully.", fg="dark green")


def select_employee(event):
    global selected_employee
    selection = employee_list.curselection()
    if len(selection) == 0:
        return
    selected_employee = selection[0]
    employee = employees[selected_employee]
    name_entry.delete(0, END)
    name_entry.insert(0, employee[0])
    department.set(employee[1])
    if employee[2] == "Full-Time":
        full_time.set(1)
    else:
        full_time.set(0)
    message_label.config(text="Change the fields, then click Edit Employee.",
                         fg="navy")


def edit_employee():
    if selected_employee == -1 or len(employee_list.curselection()) == 0:
        message_label.config(text="Select an employee from the list to edit.",
                             fg="red")
        return
    if not validate_input():
        return
    if full_time.get() == 1:
        status = "Full-Time"
    else:
        status = "Part-Time"
    employees[selected_employee] = [name_entry.get().strip(), department.get(),
                                    status]
    display_employees()
    clear_input()
    message_label.config(text="Employee updated successfully.", fg="dark green")


def close_application():
    window.destroy()


window = Tk()
window.title("Employee Record System")
window.geometry("820x620")
window.configure(bg="light blue")
window.minsize(820, 620)
window.columnconfigure(1, weight=1)
window.rowconfigure(7, weight=1)

department = StringVar(value="Select a department")
full_time = IntVar(value=0)

Label(window, text="Employee Record System", font=("Arial", 20, "bold"),
      bg="light blue", relief="ridge", borderwidth=2, padx=16, pady=10).grid(
          row=0, column=0, columnspan=2, sticky="ew", padx=20, pady=(18, 12))

Label(window, text="Employee Name", bg="light blue", relief="groove",
      borderwidth=2, padx=10, pady=6).grid(row=1, column=0, sticky="ew",
                                         padx=(20, 10), pady=5)
name_entry = Entry(window, font=("Arial", 12))
name_entry.grid(row=1, column=1, sticky="ew", padx=(0, 20), pady=5, ipady=4)

Label(window, text="Department", bg="light blue", relief="groove",
      borderwidth=2, padx=10, pady=6).grid(row=2, column=0, sticky="ew",
                                         padx=(20, 10), pady=5)
department_menu = OptionMenu(window, department, "Select a department",
                             "Human Resources", "Finance",
                             "Information Technology", "Marketing", "Operations")
department_menu.grid(row=2, column=1, sticky="ew", padx=(0, 20), pady=5)

Label(window, text="Employment Status", bg="light blue", relief="groove",
      borderwidth=2, padx=10, pady=6).grid(row=3, column=0, sticky="ew",
                                         padx=(20, 10), pady=5)
Checkbutton(window, text="Full-Time (unchecked = Part-Time)", variable=full_time,
            bg="light blue", font=("Arial", 11)).grid(row=3, column=1,
            sticky="w", padx=(0, 20), pady=5)

button_frame = Frame(window, bg="light blue")
button_frame.grid(row=4, column=0, columnspan=2, pady=12)
Button(button_frame, text="Add Employee", command=add_employee,
       bg="light green", width=19, padx=8, pady=6).grid(row=0, column=0, padx=8)
Button(button_frame, text="Edit Employee", command=edit_employee,
       bg="light green", width=19, padx=8, pady=6).grid(row=0, column=1, padx=8)

message_label = Label(window, text="Enter employee information to begin.",
                      bg="light blue", fg="navy", font=("Arial", 11))
message_label.grid(row=5, column=0, columnspan=2, padx=20, pady=(0, 8))
Label(window, text="Employee Record Display: Name | Department | Status",
      bg="light blue", relief="sunken", borderwidth=2, padx=10, pady=6).grid(
          row=6, column=0, columnspan=2, sticky="ew", padx=20, pady=(0, 5))

list_frame = Frame(window)
list_frame.grid(row=7, column=0, columnspan=2, sticky="nsew", padx=20, pady=5)
list_frame.columnconfigure(0, weight=1)
list_frame.rowconfigure(0, weight=1)
employee_list = Listbox(list_frame, height=9, font=("Arial", 11),
                       exportselection=False)
employee_list.grid(row=0, column=0, sticky="nsew")
scrollbar = Scrollbar(list_frame, orient=VERTICAL, command=employee_list.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
employee_list.config(yscrollcommand=scrollbar.set)
employee_list.bind("<<ListboxSelect>>", select_employee)

Button(window, text="Quit", command=close_application, width=15,
       padx=8, pady=6).grid(row=8, column=0, columnspan=2, pady=(10, 18))
name_entry.focus_set()

if __name__ == "__main__":
    window.mainloop()
