# import mysql.connector
# mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='mydb', auth_plugin='mysql_native_password')
# mycursor = mydb.cursor()
# xy = mycursor.execute('Select * from mytable')
# for i in mycursor:
#     print(i)

from tkinter import *
import mysql.connector
from tkinter import messagebox

root = Tk()
# widget features & style
root.geometry("450x400")
root.title("MySQL (Uthmaan Breda)")
root.config(bg="red")

Label(root, text='User:', bg="red", font="poppins 10 bold").place(x=30, y=50)
user_ent = Entry(root)
user_ent.place(x=100, y=50)
Label(root, text='Email:', bg="red", font="poppins 10 bold").place(x=30, y=100)
mail_ent = Entry(root)
mail_ent.place(x=100, y=100)


def register():
    mydb = mysql.connector.connect(user='root', password='Themainp1zza!', host='127.0.0.1', database='mydb',
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()

    sql = "INSERT INTO mytable (username, email) VALUES (%s, %s)"
    val = (user_ent.get(), mail_ent.get())
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


def login():
    mydb = mysql.connector.connect(user='root', password='Themainp1zza!', host='127.0.0.1', database='mydb',
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()

    xy = mycursor.execute('Select * from mytable')
    if user_ent.get() == '' or mail_ent.get() == '':
        messagebox.showerror('error', 'fill in all fields', parent=root)
    for i in mycursor:
        print(i)
        if user_ent.get() == i[1] and mail_ent.get() == i[2]:
            messagebox.showinfo('Success', 'You are logged in')
            break

    else:
        messagebox.showerror('ERROR!!!!!!!!!!!', 'Incorrect credentials')


Button(root, text='Login', command=login, bg="red", font="poppins 10 bold", border="5").place(x=80, y=150)
Button(root, text='Register', command=register, bg="red", font="poppins 10 bold", border="5").place(x=180, y=150)

root.mainloop()  # continuously runs program in window

# (ctrl + alt + L) to reformat code
