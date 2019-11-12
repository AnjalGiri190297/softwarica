from tkinter import *
import mysql.connector
from tkinter import ttk
from tkinter import messagebox


try:
        con=mysql.connector.connect(host='localhost',user='root',passwd='root',database='softwarica')
        cur= con.cursor()
except mysql.connector.Error as e:
        print(e)

root = Tk()
photo=PhotoImage(file="softwarica.png")
title = Label(root,image=photo ,highlightbackground="blue", highlightcolor="blue", highlightthickness=4, bd=8, relief=RIDGE, bg="blue")
title.pack(side=TOP)
title_Frame=Frame()
title.place(x=10,y=0,height=100,width=450)
class Softwarica:
    def __init__(self,root):

        root.title('Student Management')
        root.geometry("1360x700+0+0")
        root.configure(bg='white')
        titletext_Frame = Frame(root, highlightbackground="blue", highlightcolor="blue", highlightthickness=4, bd=8, relief=RIDGE, bg="blue")
        titletext_Frame.place(x=460, y=0, width=900, height=100)
        titletext = Label(titletext_Frame, text="WELCOME!!! TO STUDENT MANAGEMENT SYSTEM", font=("times new roman", 25, "bold"),bg="blue", fg="white")
        titletext.pack(side=TOP)
        addresst=Label(titletext_Frame,text="Dillibazar,kathmadu,Nepal",font=("times new roman",10,"bold"))
        addresst.pack()
        phonet=Label(titletext_Frame,text="1234567,13334536")
        phonet.pack(side=BOTTOM)

        # Lables
        self.entry_frame = Frame(root, highlightbackground="blue", highlightcolor="blue", highlightthickness=4,bd=8,relief=RIDGE,bg="white")
        self.entry_frame.place(x=10,y=100,width=450,height=520)
        E_title = Label(self.entry_frame, text="Student detail", font=("times new roman", 17, "bold"))
        E_title.grid(row=0, columnspan=2, pady=0)

        self.student_id = Label(self.entry_frame,text="Student ID",font=("times new roman",15,"bold"))
        self.first_name = Label(self.entry_frame, text="FIRST NAME",  font=("times new roman", 15, "bold"))
        self.last_name = Label(self.entry_frame, text="LAST NAME",  font=("times new roman", 15, "bold"))

        self.degree = Label(self.entry_frame,  text="DEGREE",  font=("times new roman", 15, "bold"),highlightbackground="grey", highlightcolor="grey", highlightthickness=4)
        self.address = Label(self.entry_frame, text='Address', font=("times new roman", 15, "bold"))
        self.contact_no = Label(self.entry_frame, text='Contact Number', font=("times new roman", 15, "bold"))


        self.student_id.grid(row=1, column=0,padx=10, pady=5,sticky="w")
        self.first_name.grid(row=2, column=0, padx=10, pady=5,sticky="w")
        self.last_name.grid(row=3, column=0, padx=10,pady=5,sticky="w")

        self.degree.grid(row=5, column=0, padx=10, pady=5,sticky="w")
        self.address.grid(row=6, column=0, padx=10, pady=5,sticky="w")
        self.contact_no.grid(row=7, column=0, padx=10, pady=5,sticky="w")

        # Entry

        self.entrystudent_id =  Entry (self.entry_frame,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE,highlightbackground="grey", highlightcolor="grey", highlightthickness=4)
        self.entryfirst_name = Entry(self.entry_frame,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE,highlightbackground="grey", highlightcolor="grey", highlightthickness=4)
        self.entrylast_name = Entry(self.entry_frame,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE,highlightbackground="grey", highlightcolor="grey", highlightthickness=4)
        self.entrydegree = ttk.Combobox(self.entry_frame,font=("tines new roman", 10, "bold"), values=['Bsc(Hons)computing', 'Ethical Hacking'])
        self.entryaddress = Entry(self.entry_frame,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE,highlightbackground="grey", highlightcolor="grey", highlightthickness=4)
        self.entrycontact_no = Entry(self.entry_frame,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE,highlightbackground="grey", highlightcolor="grey", highlightthickness=4)

        self.entrystudent_id.grid(row=1, column=1, padx=10, pady=5,sticky="w")
        self.entryfirst_name.grid(row=2, column=1, padx=10, pady=5,sticky="w")
        self.entrylast_name.grid(row=3, column=1, padx=10, pady=5,sticky="w")
        self.entrydegree.grid(row=5, column=1, padx=10, pady=5,sticky="w")
        self.entryaddress.grid(row=6, column=1, padx=10, pady=5,sticky="w")
        self.entrycontact_no.grid(row=7, column=1, padx=10, pady=5,sticky="w")


        self.btn_frame = Frame(root,bd=5,relief=RIDGE,bg="blue",highlightbackground="blue", highlightcolor="blue", highlightthickness=4)
        self.btn_frame.place(x=22,y=480,width=430,height=60)
        self.Detail_Frame = Frame(root, highlightbackground="blue", highlightcolor="blue", highlightthickness=4, bd=8,
                             relief=RIDGE, bg="white")
        self.Detail_Frame.place(x=460, y=100, width=900, height=520)

        self.btn_sort = Button(self.Detail_Frame,  text="SORT", width=10, bd=5, relief=RIDGE, command=self.sort)
        self.btn_sort.grid(row=0, column=5, padx=10)


        self.table_frame = Frame(self.Detail_Frame, bd=5,relief=RIDGE,bg="blue",highlightbackground="blue", highlightcolor="blue", highlightthickness=4)
        self.table_frame.place(x=10,y=50,width=860,height=440)

        # scrollbar
        self.scroll_x = Scrollbar(self.table_frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)

        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        # table
        self.student_table = ttk.Treeview(self.table_frame, column=(
        'student_id', 'first_name', 'last_name', 'degree', 'address', 'contact_no'), xscrollcommand=self.scroll_x.set,
                                          yscrollcommand=self.scroll_y.set)
        self.student_table.heading('student_id', text="Id")
        self.student_table.heading('first_name', text="First Name")
        self.student_table.heading('last_name', text="Last Name")
        self.student_table.heading('degree', text="Degree")
        self.student_table.heading('address', text="Address")
        self.student_table.heading('contact_no', text="Contact Number")
        self.student_table['show'] = 'headings'

        self.student_table.column('student_id', width=10)
        self.student_table.column('first_name', width=40)
        self.student_table.column('last_name', width=40)
        self.student_table.column('degree', width=80)
        self.student_table.column('address', width=80)
        self.student_table.column('contact_no', width=20)

        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)
        self.show()

        self.student_table.bind(('<ButtonRelease-1>'), self.pointer)
        self.student_table.pack(fill=BOTH, expand=True)

        # Buttons
        self.addbutton = Button(self.btn_frame, text='Add', command=self.add, width=8, height=2)
        self.addbutton.grid(row=7, column=0, padx=10)

        self.btn_update = Button(self.btn_frame, text='Update', width=8, height=2, command=self.update)
        self.btn_update.grid(row=7, column=1, padx=10)

        self.delete = Button(self.btn_frame, text='Delete', command=self.delete_data, width=8, height=2)
        self.delete.grid(row=7, column=2, padx=10)

        self.btn_clear = Button(self.btn_frame, text='Clear', width=8, height=2, command=self.clear)
        self.btn_clear.grid(row=7, column=3, padx=10)

        self.btn_search = Button(self.Detail_Frame, text="SEARCH", width=10,bd=5, relief=RIDGE, command=self.search_fetch)
        self.btn_search.grid(row=0,column=4,pady=10,padx=10,sticky="w")

        self.lbl_search = Label(self.Detail_Frame,text="Search By",bg="white",fg="blue",font=("times new roman",20,"bold"))
        self.lbl_search.grid(row=0,column=0,pady=10,padx=10,sticky="w")
        self.combo_search = ttk.Combobox(self.Detail_Frame,font=("tines new roman", 10, "bold"))
        self.combo_search['values'] = ('student_id', 'first_name', 'last_name', 'degree', 'address', 'contact_no')
        self.combo_search.set('student_id')
        self.combo_search.grid(row=0, column=1, padx=10, pady=10)

        self.Esearch = Entry(self.Detail_Frame,font=("times new roman", 10, "bold"), bd=5, relief=GROOVE,highlightbackground="grey", highlightcolor="grey", highlightthickness=4)
        self.Esearch.grid(row=0, column=2, padx=10, pady=10, sticky="w")
        root.mainloop()

    def add(self):
        self.student_id=(self.entrystudent_id.get())
        self.first_name=self.entryfirst_name.get()
        self.last_name=self.entrylast_name.get()
        self.degree = self.entrydegree.get()
        self.address=self.entryaddress.get()
        self.contact_no=(self.entrycontact_no.get())
        if self.student_id == "" or self.first_name == "" or self.last_name == "" or self.degree == "" or self.address == "" or self.contact_no == "":
            messagebox.showerror("error", "All field are requird")
        else:



            query='insert into new_table values(%s,%s,%s,%s,%s,%s)'
            self.values=(self.student_id,self.first_name,self.last_name,self.degree,self.address,self.contact_no)
            cur.execute(query,self.values)
            print('Data saved successfully')
            con.commit()
            self.show()
            self.clear()

    def show(self):
        query='select * from new_table'
        cur.execute(query)
        self.result=cur.fetchall()
        if len(self.result)!=0:
            self.student_table.delete(*self.student_table.get_children())
        for row in self.result:
            self.student_table.insert('',END,values=row)
            con.commit()


    def delete_data(self):
        self.student_id = (self.entrystudent_id.get())
        print(self.student_id)
        if self.student_id == "":
            messagebox.showinfo("Error", "Nothing to Delete !")
        else:
            query = 'delete from new_table where student_id = %s'
            self.values = (self.student_id,)
            cur.execute(query, self.values)
            con.commit()
            self.show()
            print('data deleted successfully')

    def clear(self):
        self.entrystudent_id.delete(0,END)
        self.entryfirst_name.delete(0,END)
        self.entrylast_name.delete(0,END)
        self.entrydegree.delete(0,END)
        self.entryaddress.delete(0,END)
        self.entrycontact_no.delete(0,END)


    def pointer(self,event):
        self.point=self.student_table.focus()
        self.content=self.student_table.item(self.point)
        self.row=self.content['values']
        self.clear()
        self.entrystudent_id.insert(0,self.row[0])
        self.entryfirst_name.insert(0,self.row[1])
        self.entrylast_name.insert(0,self.row[2])
        self.entrydegree.insert(0,self.row[3])
        self.entryaddress.insert(0,self.row[4])
        self.entrycontact_no.insert(0,self.row[5])


    def update(self):
        query='update new_table set first_name=%s,last_name=%s,degree=%s,address=%s,contact_no=%s where student_id=%s'
        self.student_id=(self.entrystudent_id.get())
        self.first_name=self.entryfirst_name.get()
        self.last_name=self.entrylast_name.get()
        self.degree=self.entrydegree.get()
        self.address=self.entryaddress.get()
        self.contact_no=(self.entrycontact_no.get())
        if self.student_id == "" or self.first_name == "" or self.last_name == "" or self.degree == "" or self.address == "" or self.contact_no == "":
            messagebox.showerror("error", "All field are requird")
        else:
            self.values=(self.first_name,self.last_name,self.degree,self.address,self.contact_no,self.student_id)
            cur.execute(query,self.values)
            con.commit()
            self.show()
            self.clear()

    def search(self,data, search_index, search_for):
        global search_results
        search_results = []
        for i in data:
            if str(search_for) in str(i[search_index]):
                search_results.append(i)
                return search_results




    def search_fetch(self):
        self.query = "select * from new_table"
        cur.execute(self.query)
        data = cur.fetchall()
        test = self.combo_search.get()
        searching = self.Esearch.get()
        tri = ('student_id', 'first_name', 'last_name', 'degree', 'address', 'contact_no')
        search_index = int()
        for i in tri:
            if i == test:
                search_index = tri.index(i)
        self.search(data, search_index,searching)
        self.student_table.delete(*self.student_table.get_children())
        if len(search_results) != 0:
            for i in search_results:
                self.student_table.insert('', END, values=i)
                con.commit()

    @staticmethod
    def bubble_sort(result,sort_by):
            for i in range(0,len(result)-1):
                for j in range(0,len(result)-1-i):
                    if result[j][sort_by]>result[j+1][sort_by]:
                        result[j],result[j+1]=result[j+1],result[j]
                    return result


    def sort(self):
        values = str(self.combo_search.get())
        self.thelist = 'select * from new_table'
        cur.execute(self.thelist)
        result = cur.fetchall()
        for i in result:
            print(i)
        if values == "student_id":
            sort_index = 0
        elif values == "first_name":
            sort_index = 1
        elif values == "last_name":
            sort_index = 2
        elif values == "degree":
            sort_index = 3
        elif values == "address":
            sort_index = 4
        elif values == "contact_no":
            sort_index = 5
        else:
            print("Error ! No such Parameter , Sorted as accordance to id.")
            sort_index = 0

        self.bubble_sort(result,sort_index)

        if len(result) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in result:
                self.student_table.insert('', END, values=row)
                con.commit()






a = Softwarica(root)
root.mainloop()