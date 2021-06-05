from tkinter import *
import backend


def change_entries(title="", author="", year="", isbn=""):
    e1.delete(0, END)
    e1.insert(END, title)
    e2.delete(0, END)
    e2.insert(END, author)
    e3.delete(0, END)
    e3.insert(END, year)
    e4.delete(0, END)
    e4.insert(END, isbn)


def get_selected_row(event):
    global selected_row
    if len(list1.curselection()) > 0:
        index = list1.curselection()[0]
        selected_row = list1.get(index)
        change_entries(selected_row[1], selected_row[2],
                       selected_row[3], selected_row[4])
    


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in backend.search(title=title_text.get(), author=author_text.get(), year=year_text.get(), isbn=isbn_text.get()):
        list1.insert(END, row)


def add_command():
    backend.insert(title=title_text.get(), author=author_text.get(),
                   year=year_text.get(), isbn=isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(),
                 year_text.get(), isbn_text.get()))
    change_entries()


def update_command():
    backend.update(id=selected_row[0], title=title_text.get(), author=author_text.get(),
                   year=year_text.get(), isbn=isbn_text.get())
    change_entries()
    view_command()


def delete_command():
    backend.delete(selected_row[0])
    change_entries()
    view_command()


window = Tk()

window.wm_title("BookStore")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=7, width=35)
list1.grid(row=2, column=0, rowspan=7, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=7)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
