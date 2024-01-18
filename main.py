from tkinter import *

root = Tk()
root.title("Certificate Generator")
root.configure(bg="#f4f4f4")  # Light gray
root.iconbitmap("favicon.ico")
root.geometry("500x500")
root.resizable(False,False)

header_frame = Frame(root,relief=RIDGE, bg="#004080",width =600,height = 50)
header_frame.grid(row=0,column=0,columnspan=4)
header_label = Label(header_frame,text = "AutoCertify",font=("Helvetica", 26,"bold"), bg="#004080", fg="white")
header_label.pack(side=TOP,padx= 165)

excel_browse_frame = Frame(root,relief=RIDGE,bg="#f4f4f4",width = 600, height =50)
excel_browse_frame.grid(row = 1,column = 0,pady=10,sticky=W)
excel_browse_label = Label(excel_browse_frame,text = "Enter the Path of Excel file:",font= ("Helvetica",12,"bold"),bg="#f4f4f4",fg = "black")
excel_browse_label.grid(row=0,column=0,pady =5,padx=10,sticky=W)

excel_entry_var = StringVar()
excel_entry_field = Entry(excel_browse_frame,width=40,font=("Helvetica", 12),bg ="white",textvariable=excel_entry_var)
excel_entry_field.grid(row=1, column=0,padx=10)


excel_browse_button = Button(excel_browse_frame, text="Browse",font =("Helvetica",12), bg="#003366", fg="white")
excel_browse_button.grid(row=1, column=1,padx=10,sticky = W)

root.mainloop()