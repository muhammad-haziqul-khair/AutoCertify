from tkinter import *
from tkinter import messagebox

def validate_num_input(num):  # allows the user to input numbers only in coordinates field  
    if num.isdigit():
        return True
    elif num == "":
        return True
    else:
        return False

def guide_clicked(event):
    messagebox.showinfo("GUIDE","Open the Sample Certificate in the Paint and Hover on the area where you want to write the name.\nOn the bottom left, you will see the co-ordinates(x,y)")

root = Tk()
root.title("Certificate Generator")
root.configure(bg="#f4f4f4")  # Light gray
root.iconbitmap("favicon.ico")
root.geometry("500x500")
root.resizable(False,False)
reg = root.register(validate_num_input)

# Main Label
header_frame = Frame(root,relief=RIDGE, bg="#004080",width =600,height = 50)
header_frame.grid(row=0,column=0,columnspan=4)
header_label = Label(header_frame,text = "AutoCertify",font=("Helvetica", 26,"bold"), bg="#004080", fg="white")
header_label.pack(side=TOP,padx= 165)

# gets the path of the Excel file
excel_browse_frame = Frame(root,relief=RIDGE,bg="#f4f4f4",width = 600, height =50)
excel_browse_frame.grid(row = 1,column = 0,pady=10,sticky=W)
excel_browse_label = Label(excel_browse_frame,text = "Enter the Path of Excel file:",font= ("Helvetica",12,"bold"),bg="#f4f4f4",fg = "black")
excel_browse_label.grid(row=0,column=0,pady =5,padx=10,sticky=W)

excel_entry_var = StringVar()
excel_entry_field = Entry(excel_browse_frame,width=40,font=("Helvetica", 12),bg ="white",textvariable=excel_entry_var)
excel_entry_field.grid(row=1, column=0,padx=10)

excel_browse_button = Button(excel_browse_frame, text="Browse",font =("Helvetica",12), bg="#003366", fg="white")
excel_browse_button.grid(row=1, column=1,padx=10,sticky = W)

# gets the path of sample of certificate
cert_browse_frame = Frame(root, relief=RIDGE, bg="#f4f4f4", width=500, height=80)
cert_browse_frame.grid(row=2, column=0, pady=10, sticky=W)
cert_browse_label = Label(cert_browse_frame, text="Enter the Path of Sample Certificate:",font=("Helvetica", 12, "bold"), bg="#f4f4f4", fg="black")
cert_browse_label.grid(row=0, column=0, pady=5, padx=10, sticky=W)

cert_entry_var = StringVar()
cert_entry_field = Entry(cert_browse_frame, width=40, font=("Helvetica", 12), bg="white", textvariable=cert_entry_var)
cert_entry_field.grid(row=1, column=0, padx=10)

cert_browse_button = Button(cert_browse_frame, text="Browse", font=("Helvetica", 12), bg="#003366", fg="white")
cert_browse_button.grid(row=1, column=1, padx=10, sticky=W)

pos_frame = Frame(root, relief=RIDGE, bg="#f4f4f4", width=500, height=80)
pos_frame.grid(row=3, column=0, pady=10, sticky=W)
pos_label = Label(pos_frame,text="Enter the Position of the Name on the certificate:",font=("Helvetica", 12, "bold"), bg="#f4f4f4", fg="black")
pos_label.grid(row=0, column=0,columnspan=3, pady=5, padx=10, sticky=W)

guide_btn = Label(pos_frame,text="Guide",width = 5,height=2,cursor="hand2",font=("Helvetica",12,"underline"),bg="#f4f4f4",fg="black")
guide_btn.grid(row=0,column=3,pady=5,sticky=W)
guide_btn.bind("<Button-1>",guide_clicked)

x_label = Label(pos_frame,text="X:",font=("Helvetica", 12, "bold"), bg="#f4f4f4", fg="black")
x_label.grid(row=1,column=0,pady=5,padx=5,sticky=W)

x_entry_var = IntVar()
x_entry_field = Entry(pos_frame, width=15, font=("Helvetica", 12), bg="white", textvariable=x_entry_var,validate="key",validatecommand=(reg,"%P"))
x_entry_field.grid(row=1,column=0,pady=5,padx=20)

y_label = Label(pos_frame,text="Y:",font=("Helvetica", 12, "bold"), bg="#f4f4f4", fg="black")
y_label.grid(row=1,column=1,pady=5,padx=5,sticky=W)

y_entry_var = IntVar()
y_entry_field = Entry(pos_frame, width=15, font=("Helvetica", 12), bg="white", textvariable=y_entry_var,validate="key",validatecommand=(reg,"%P"))
y_entry_field.grid(row=1,column=1,pady=5,padx=20)

root.mainloop()