#All necessary Packages
import datetime
from tkinter import *
import sqlite3
from tkinter.ttk import Style, Treeview
import atexit
from os import path
import fpdf
from json import dumps, loads
import atexit
from tkcalendar import Calendar, DateEntry

#font
book_antiqua=("Helvetica Neue Light",12,"normal")
arial=('Arial', 12)
book_antiqua_size18=("Book Antiqua",18,"bold underline")

frame_color='#212125'
element_color='white'
element_color_dark='#6a6c6e'


#date and time, sorting date into dd/mm/yyyy
date=datetime.date.today()
datesorted=date.strftime("%d-%m-%Y")

#Bill Number Counter
def read_counter(filename):
    #reads the Bill number from the counter.json file
    if path.exists("{}.json".format(filename)):
            if filename=='company_details':
                return loads(open("{}.json".format(filename), "r").read())
            elif filename=='bill_number':
                return loads(open("{}.json".format(filename), "r").read()) + 1 if path.exists("{}.json".format(filename)) else 0
            elif filename=='purchase_invoice_number':
                return loads(open("{}.json".format(filename), "r").read()) + 1 if path.exists("{}.json".format(filename)) else 0
    
def write_counter(filename,data_to_write):
    #writes/saves the Bill Number in counter.json file
    with open("{}.json".format(filename), "w") as f:
        f.write(dumps(data_to_write))

#bill_number = read_counter('bill_number')

#Tkinter window configs
if "__main__"==__name__:
    root=Tk()
    root.title("Billing App")
    #get your Windows width/height, set size to full window
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    #wont allow to resize window, and full screen when opening
    root.resizable(False,False)
    root.state('zoomed')

    #Logo
menu_frame= Frame(root,bg="#333232",width=250,height=1060)
menu_frame.grid(row=0,column=0)
menu_frame.propagate(0)

img=PhotoImage(file='logo.png')
image = Label(menu_frame,image=img)

style = Style(root)
style.theme_use("clam")
style.configure("Treeview", background=element_color_dark,fieldbackground=element_color_dark, foreground="white")

def clear_all(treeview_name):
        for item in treeview_name.get_children():
            treeview_name.delete(item)

def selected_item_from_treeview(treeview_name):
    curItem = treeview_name.focus()
    treeview_name.item(curItem)
    selected_items =treeview_name.item(curItem)
    for key, value in selected_items.items():
        if key == 'values':
            k=value[0]
            return k

def menu_frame_obj():
    image.place(relx = 0.45, rely = 0.075, anchor = CENTER)

    company_details_btn=Button(menu_frame,text="Company",width = 25,fg=element_color,bg=element_color_dark,command=lambda:[company_details_obj()])
    company_details_btn.place(relx = 0.475, rely = 0.23, anchor = CENTER)

    purchase_btn=Button(menu_frame,text="Purchase",width = 25,fg=element_color,bg=element_color_dark,command=lambda:[purchase_obj()])
    purchase_btn.place(relx = 0.475, rely = 0.26, anchor = CENTER)

    dealer_btn=Button(menu_frame,text="Dealer",width = 25,fg=element_color,bg=element_color_dark,command=lambda:[dealer_obj()])
    dealer_btn.place(relx = 0.475, rely = 0.29, anchor = CENTER)
    
    '''customer_btn=Button(menu_frame,text="Customer",width = 25,fg=element_color,bg=element_color_dark,command=lambda:[customer_detail_obj()])
    customer_btn.place(relx = 0.475, rely = 0.35, anchor = CENTER)'''

    item_btn=Button(menu_frame,text="Items",width = 25,fg=element_color,bg=element_color_dark,command=lambda:[item_obj()])
    item_btn.place(relx = 0.475, rely = 0.35, anchor = CENTER)

    reports_btn=Button(menu_frame,text="Reports",width = 25,fg=element_color,bg=element_color_dark,command=lambda:[report_obj()])
    reports_btn.place(relx = 0.475, rely = 0.32, anchor = CENTER)

    billing_btn=Button(menu_frame,text="Billing",width = 25,fg=element_color,bg=element_color_dark,command=lambda:[billing_obj()])
    billing_btn.place(relx = 0.475, rely = 0.38, anchor = CENTER)

def company_details_obj():
    company_details_frame= Frame(root,width=1670,height=1060,bg=frame_color)
    company_details_frame.grid(row=0,column=1)
    company_details_frame.propagate(0)

    #Company Name
    company_name_lbl=Label(company_details_frame,text="Company Name",font=book_antiqua,bg=frame_color,fg=element_color)
    company_name_lbl.place(relx = 0.1, rely = 0.2, anchor = NW)

    company_name_tb=Entry(company_details_frame,fg=element_color,bg=element_color_dark,font=arial,border=4)
    company_name_tb.place(relx = 0.2, rely = 0.2, anchor = NW)

    #Company Adress
    company_adress_lbl=Label(company_details_frame,text="Company Adress",font=book_antiqua,bg=frame_color,fg=element_color)
    company_adress_lbl.place(relx = 0.1, rely = 0.24, anchor = NW)

    company_adress_tb=Entry(company_details_frame,fg=element_color,bg=element_color_dark,font=arial,border=4)
    company_adress_tb.place(relx = 0.2, rely = 0.24, anchor = NW)

    #Company GSTIN
    company_gstin_lbl=Label(company_details_frame,text="Company GSTIN",font=book_antiqua,bg=frame_color,fg=element_color)
    company_gstin_lbl.place(relx = 0.1, rely = 0.28, anchor = NW)

    company_gstin_tb=Entry(company_details_frame,fg=element_color,bg=element_color_dark,font=arial,border=4)
    company_gstin_tb.place(relx = 0.2, rely = 0.28, anchor = NW)

    #Company Adress
    company_contact_number_lbl=Label(company_details_frame,text="Company Contact",font=book_antiqua,bg=frame_color,fg=element_color)
    company_contact_number_lbl.place(relx = 0.1, rely = 0.32, anchor = NW)

    company_contact_number_tb=Entry(company_details_frame,fg=element_color,bg=element_color_dark,font=arial,border=4)
    company_contact_number_tb.place(relx = 0.2, rely = 0.32, anchor = NW)

    #Update BUtton and message
    add_update_btn=Button(company_details_frame,fg=element_color,bg=element_color_dark,text="Add/Update Details",width = 25,border=4,command=lambda:[details_updated_obj()])
    add_update_btn.place(relx = 0.1, rely = 0.38, anchor = NW)

    def details_updated_obj():
        if company_name_tb.get() =="" or company_adress_tb.get() =="" or company_gstin_tb.get() =="" or company_contact_number_tb.get() =="":
            message_lbl=Label(company_details_frame,text='Enter All Fields',font=book_antiqua,fg="red",bg=frame_color)
            message_lbl.place(relx = 0.1, rely = 0.42, anchor = NW)
        else:
            message_lbl=Label(company_details_frame,text='Details Updated',font=book_antiqua,fg="#2ea307",bg=frame_color)
            message_lbl.place(relx = 0.1, rely = 0.42, anchor = NW)
            
            #stores company data in company_details.json file
            company=[]
            company.append(company_name_tb.get())
            company.append(company_adress_tb.get())
            company.append(company_gstin_tb.get())
            company.append(company_contact_number_tb.get())
            write_counter('company_details',company)

    if path.exists("company_details.json"):
        current_company_details=read_counter('company_details')
        company_name_tb.insert(0,current_company_details[0])
        company_adress_tb.insert(0,current_company_details[1])
        company_gstin_tb.insert(0,current_company_details[2])
        company_contact_number_tb.insert(0,current_company_details[3])

def purchase_obj():
    purchase_frame= Frame(root,width=1670,height=1060,bg=frame_color)
    purchase_frame.grid(row=0,column=1)
    purchase_frame.propagate(0)

    purchase_details_lbl=Label(purchase_frame,text="Purchase Products",font=book_antiqua_size18,bg=frame_color,fg=element_color)
    purchase_details_lbl.place(relx = 0.4, rely = 0.065, anchor = NW)

    #Dealer name
    dealer_name_lbl=Label(purchase_frame,text="Dealer Name",font=book_antiqua,bg=frame_color,fg=element_color)
    dealer_name_lbl.place(relx = 0.04, rely = 0.14, anchor = NW)

    dealer_name_tb=Entry(purchase_frame,fg=element_color,bg=element_color_dark,font=arial,border=4,width=25)
    dealer_name_tb.place(relx = 0.105, rely = 0.14, anchor = NW)

    #Dealer Gstin
    dealer_gstin_lbl=Label(purchase_frame,text="GSTIN",font=book_antiqua,bg=frame_color,fg=element_color)
    dealer_gstin_lbl.place(relx = 0.265, rely = 0.14, anchor = NW)

    dealer_gstin_tb=Entry(purchase_frame,fg=element_color,bg=element_color_dark,font=arial,border=4)
    dealer_gstin_tb.place(relx = 0.3, rely = 0.14, anchor = NW)

    #Purchase Date
    purchase_date_lbl=Label(purchase_frame,text="Date",font=book_antiqua,bg=frame_color,fg=element_color)
    purchase_date_lbl.place(relx = 0.43, rely = 0.14, anchor = NW)

    #date
    today = date.today()
    purchase_date= DateEntry(purchase_frame, width= 16,height=0, background= "grey", foreground= "white",bd=4, maxdate=today)
    purchase_date.place(relx = 0.455, rely = 0.1405, anchor = NW)

    #Purchase INvoice Number
    invoice_number_lbl=Label(purchase_frame,text="Invoice Number",font=book_antiqua,bg=frame_color,fg=element_color)
    invoice_number_lbl.place(relx = 0.55, rely = 0.14, anchor = NW)

    invoice_number_tb=Entry(purchase_frame,fg=element_color,bg=element_color_dark,font=arial,border=4)
    invoice_number_tb.place(relx = 0.62, rely = 0.14, anchor = NW)

    #dealer Address
    purchase_dealer_address_lbl=Label(purchase_frame,text="Address",font=book_antiqua,bg=frame_color,fg=element_color)
    purchase_dealer_address_lbl.place(relx = 0.06, rely = 0.19, anchor = NW)

    purchase_dealer_address_tb=Entry(purchase_frame,fg=element_color,bg=element_color_dark,font=arial,border=4,width=25)
    purchase_dealer_address_tb.place(relx = 0.105, rely = 0.19, anchor = NW)

    #dealer contact
    purchase_dealer_contact_lbl=Label(purchase_frame,text="Contact",font=book_antiqua,bg=frame_color,fg=element_color)
    purchase_dealer_contact_lbl.place(relx = 0.26, rely = 0.19, anchor = NW)

    purchase_dealer_contact_tb=Entry(purchase_frame,fg=element_color,bg=element_color_dark,font=arial,border=4,width=20)
    purchase_dealer_contact_tb.place(relx = 0.3, rely = 0.19, anchor = NW)

    #Purchase Item Code TextBox
    purchase_item_code_tb=Entry(purchase_frame,fg=element_color,bg=element_color_dark,font=arial,border=4,width=14)
    purchase_item_code_tb.place(relx = 0.03, rely = 0.24, anchor = NW)

    #Purchase Item Name TextBox
    purchase_item_name_tb=Entry(purchase_frame,fg=element_color,bg=element_color_dark,font=arial,border=4,width=28)
    purchase_item_name_tb.place(relx = 0.11, rely = 0.24, anchor = NW)

    #Purchase Quantity TextBox
    purchase_quantity_tb=Entry(purchase_frame,fg=element_color,bg=element_color_dark,font=arial,border=4,width=10)
    purchase_quantity_tb.place(relx = 0.266, rely = 0.24, anchor = NW)

    #Purchase Price
    purchase_price_tb=Entry(purchase_frame,fg=element_color,bg=element_color_dark,font=arial,border=4,width=10)
    purchase_price_tb.place(relx = 0.325, rely = 0.24, anchor = NW)


    #Purchase Add Button
    purchase_add_update_btn=Button(purchase_frame,fg=element_color,bg=element_color_dark,text="Add",width = 21,border=4,command=lambda:[add_purchase_item()])
    purchase_add_update_btn.place(relx = 0.384, rely = 0.24, anchor = NW)

    #Purchase Delete Button
    purchase_delete_btn=Button(purchase_frame,fg=element_color,bg=element_color_dark,text="Delete",width = 21,border=4,command=lambda:[delete_purchase_item()])
    purchase_delete_btn.place(relx = 0.0275, rely = 0.73, anchor = NW)

    #Purchase Total
    purchase_total_lbl=Label(purchase_frame,text="RS.0",font=book_antiqua_size18,bg=frame_color,fg=element_color)
    purchase_total_lbl.place(relx = 0.4, rely = 0.735, anchor = NW)

    #Purchase save
    purchase_print_button=Button(purchase_frame,fg=element_color,bg=element_color_dark,text="Save",width = 16,height=2,border=4,command=lambda:[invoice_number_update()])
    purchase_print_button.place(relx = 0.4, rely = 0.775, anchor = NW)
    #get all data


    def invoice_number_update():
        purchase_invoice_no=read_counter('purchase_invoice_number')
        if path.exists('purchase_invoice_number.json'):
            write_counter('purchase_invoice_number',purchase_invoice_no)
            invoice_number_tb.config(state='normal')
            invoice_number_tb.delete(0,END)
            invoice_number_tb.insert(0,purchase_invoice_no)
            invoice_number_tb.config(state='disabled')
        else:
            write_counter('purchase_invoice_number',1000)
            invoice_number_tb.config(state='normal')
            invoice_number_tb.delete(0,END)
            invoice_number_tb.insert(0,1000)
            invoice_number_tb.config(state='disabled')
    invoice_number_update()

    def add_purchase_item():
        invoice_number=int(invoice_number_tb.get())
        dealer_name=dealer_name_tb.get()
        dealer_gstin=dealer_gstin_tb.get()
        purchase_dealer_address=purchase_dealer_address_tb.get()
        purchase_dealer_contact=purchase_dealer_contact_tb.get()
        dealer_data=[invoice_number,dealer_name,dealer_gstin,purchase_dealer_address,purchase_dealer_contact]

        purchase_item_code=int(purchase_item_code_tb.get())
        date=purchase_date.get_date()
        purchase_item_name=purchase_item_name_tb.get()
        purchase_quantity=float(purchase_quantity_tb.get())
        purchase_price=float(purchase_price_tb.get())
        purchase_total=purchase_quantity*purchase_price
        try:
            con=sqlite3.connect("Store_Data.sql")
            cur=con.cursor()
            #cur.execute("CREATE TABLE IF NOT EXISTS temp_dealer_purchase_details(invoice_number int(10) PRIMARY KEY NOT NULL,dealer_name varhcar(20),dealer_gstin varhcar(20),dealer_address varhcar(30),dealer_contact int(12))")
            cur.execute("CREATE TABLE IF NOT EXISTS temp_item_purchase_details(item_id int(15) PRIMARY KEY,date date,item_name varhcar(30),purchase_quantity REAL,buying_price REAL,total_price REAL)")
            
            #cur.execute("INSERT INTO temp_dealer_purchase_details(invoice_number,dealer_name,dealer_gstin,dealer_address,dealer_contact)VALUES({},'{}','{}','{}',{})".format(invoice_number,dealer_name,dealer_gstin,purchase_dealer_address,purchase_dealer_contact))
            cur.execute("INSERT INTO temp_item_purchase_details(item_id,date,item_name,purchase_quantity,buying_price,total_price)VALUES({},'{}','{}',{:.2f},{:.2f},{:.2f})".format(purchase_item_code,date,purchase_item_name,purchase_quantity,purchase_price,purchase_total))
            
            cur.execute("SELECT item_id,item_name,purchase_quantity,buying_price,total_price FROM temp_item_purchase_details")
            row=cur.fetchall()
            clear_all(purchase_tree_view)
            for i in row:
                purchase_tree_view.insert("", 'end', text ="L1",values =(i[0],i[1],i[2],i[3],i[4]))

            cur.execute("SELECT SUM(total_price) FROM temp_item_purchase_details")
            total=cur.fetchall()
            purchase_total_lbl.configure(text="{:.2f}".format(total[0][0]))
            

            con.commit()
            con.close()
        except sqlite3.Error as err:
            print("Error - ",err)

    def delete_purchase_item():
        k=selected_item_from_treeview(purchase_tree_view)

        try:
            con=sqlite3.connect("Store_Data.sql")
            cur=con.cursor()
            cur.execute("DELETE FROM temp_item_purchase_details where item_id={}".format(k))
            cur.execute("SELECT item_id,item_name,purchase_quantity,buying_price,total_price FROM temp_item_purchase_details")
            row=cur.fetchall()
            clear_all(purchase_tree_view)
            for i in row:
                purchase_tree_view.insert("", 'end', text ="L1",values =(i[0],i[1],i[2],i[3],i[4]))

            cur.execute("SELECT SUM(total_price) FROM temp_item_purchase_details")
            total=cur.fetchall()
            purchase_total_lbl.configure(text="{:.2f}".format(total[0][0]))

            con.commit()
            con.close()
        except sqlite3.Error as err:
            print("Error - ",err)

    #treeview element
    purchase_tree_view= Treeview(purchase_frame,selectmode='browse',height=23)
    purchase_tree_view.place(relx = 0.03, rely = 0.27, anchor = NW)

    #verticle scrollbar
    #vertical_scrollbar=Scrollbar(billing_frame,orient="vertical",command=tree_view.yview)
    #vertical_scrollbar.place(relx = 0.03, rely = 0.3, anchor = NW)
    #tree_view.configure(xscrollcommand=vertical_scrollbar.set)

    #Definning number of columns
    purchase_tree_view["columns"]=("1","2","3","4","5")

    #defining heading
    purchase_tree_view["show"]='headings'

    #modifying the size of the columns
    purchase_tree_view.column("1",width=130)
    purchase_tree_view.column("2",width=260)
    purchase_tree_view.column("3",width=100)
    purchase_tree_view.column("4",width=100)
    purchase_tree_view.column("5",width=160)

    #assigning heading name
    purchase_tree_view.heading("1",text="ItemCode")
    purchase_tree_view.heading("2",text="Item Name")
    purchase_tree_view.heading("3",text="Quantity")
    purchase_tree_view.heading("4",text="Price")
    purchase_tree_view.heading("5",text="Total")





def dealer_obj():
    dealer_frame= Frame(root,width=1670,height=1060,bg=frame_color)
    dealer_frame.grid(row=0,column=1)
    dealer_frame.propagate(0)

    dealer_lbl=Label(dealer_frame,text="Dealer Details",font=book_antiqua_size18,bg=frame_color,fg=element_color)
    dealer_lbl.place(relx = 0.4, rely = 0.065, anchor = NW)

    #dealer Name
    dealer_name_lbl=Label(dealer_frame,text="Dealer Name",font=book_antiqua,bg=frame_color,fg=element_color)
    dealer_name_lbl.place(relx = 0.04, rely = 0.14, anchor = NW)

    dealer_name_tb=Entry(dealer_frame,fg=element_color,bg=element_color_dark,font=arial,border=4,width=20)
    dealer_name_tb.place(relx = 0.115, rely = 0.14, anchor = NW)

    #dealer GSTIN Number
    dealer_gstin_number_lbl=Label(dealer_frame,text="GSTIN No",font=book_antiqua,bg=frame_color,fg=element_color)
    dealer_gstin_number_lbl.place(relx = 0.25, rely = 0.14, anchor = NW)

    dealer_gstin_number_tb=Entry(dealer_frame,fg=element_color,bg=element_color_dark,font=arial,border=4)
    dealer_gstin_number_tb.place(relx = 0.3, rely = 0.14, anchor = NW)

    #dealer Address
    dealer_address_lbl=Label(dealer_frame,text="Address",font=book_antiqua,bg=frame_color,fg=element_color)
    dealer_address_lbl.place(relx = 0.429, rely = 0.14, anchor = NW)

    dealer_address_tb=Entry(dealer_frame,fg=element_color,bg=element_color_dark,font=arial,border=4)
    dealer_address_tb.place(relx = 0.475, rely = 0.14, anchor = NW)

    #dealer Contact
    dealer_contact_number_lbl=Label(dealer_frame,text="Contact Number",font=book_antiqua,bg=frame_color,fg=element_color)
    dealer_contact_number_lbl.place(relx = 0.0385, rely = 0.19, anchor = NW)

    dealer_contact_number_tb=Entry(dealer_frame,fg=element_color,bg=element_color_dark,font=arial,border=4)
    dealer_contact_number_tb.place(relx = 0.115, rely = 0.19, anchor = NW)

    #dealer add button
    dealer_add_btn=Button(dealer_frame,fg=element_color,bg=element_color_dark,text="Add",width = 15,border=4,command=lambda:[])
    dealer_add_btn.place(relx = 0.25, rely = 0.19, anchor = NW)

    #item treeview element
    dealer_tree_view= Treeview(dealer_frame,selectmode='browse',height=23)
    dealer_tree_view.place(relx = 0.04, rely = 0.23, anchor = NW)

    #verticle scrollbar
    #vertical_scrollbar=Scrollbar(billing_frame,orient="vertical",command=tree_view.yview)
    #vertical_scrollbar.place(relx = 0.03, rely = 0.3, anchor = NW)
    #tree_view.configure(xscrollcommand=vertical_scrollbar.set)

    #Definning number of columns
    dealer_tree_view["columns"]=("1","2","3","4")

    #defining heading
    dealer_tree_view["show"]='headings'

    #modifying the size of the columns
    dealer_tree_view.column("1",width=200)
    dealer_tree_view.column("2",width=130)
    dealer_tree_view.column("3",width=300)
    dealer_tree_view.column("4",width=130)

    #assigning heading name
    dealer_tree_view.heading("1",text="Name")
    dealer_tree_view.heading("2",text="Contact")
    dealer_tree_view.heading("3",text="Address")
    dealer_tree_view.heading("4",text="GSTIN No")

    #dealer refresh btn
    dealer_refresh_btn=Button(dealer_frame,fg=element_color,bg=element_color_dark,text="Delete",width = 15,border=4,command=lambda:[])
    dealer_refresh_btn.place(relx = 0.04, rely = 0.7, anchor = NW)

    #dealer Delete btn
    dealer_delete_btn=Button(dealer_frame,fg=element_color,bg=element_color_dark,text="Refresh",width = 15,border=4,command=lambda:[])
    dealer_delete_btn.place(relx = 0.12, rely = 0.7, anchor = NW)

    #dealer Edit btn
    dealer_edit_btn=Button(dealer_frame,fg=element_color,bg=element_color_dark,text="Edit",width = 15,border=4,command=lambda:[])
    dealer_edit_btn.place(relx = 0.2, rely = 0.7, anchor = NW)

    #Show details btn
    dealer_show_details_btn=Button(dealer_frame,fg=element_color,bg=element_color_dark,text="Show Details",width = 16,border=4,command=lambda:[])
    dealer_show_details_btn.place(relx = 0.424, rely = 0.7, anchor = NW)

'''def customer_detail_obj():
    customer_detail_frame=Frame(root,width=1670,height=1060,bg=frame_color)
    customer_detail_frame.grid(row=0,column=1)
    customer_detail_frame.propagate(0)

    customer_detail_customer_details_lbl=Label(customer_detail_frame,text="Customer Details",font=book_antiqua_size18,bg=frame_color,fg=element_color)
    customer_detail_customer_details_lbl.place(relx = 0.4, rely = 0.065, anchor = NW)
    
    #customer_detail_ Customer Name
    customer_detail_customer_name_lbl=Label(customer_detail_frame,text="Customer Name",font=book_antiqua,bg=frame_color,fg=element_color)
    customer_detail_customer_name_lbl.place(relx = 0.04, rely = 0.14, anchor = NW)

    customer_detail_customer_name_tb=Entry(customer_detail_frame,fg=element_color,bg=element_color_dark,font=arial,border=4,width=30)
    customer_detail_customer_name_tb.place(relx = 0.115, rely = 0.14, anchor = NW)

    #customer_detail_ Customer Mobile NUmber
    customer_detail_mobile_lbl=Label(customer_detail_frame,text="Mobile",font=book_antiqua,bg=frame_color,fg=element_color)
    customer_detail_mobile_lbl.place(relx = 0.31, rely = 0.14, anchor = NW)

    customer_detail_mobile_tb=Entry(customer_detail_frame,fg=element_color,bg=element_color_dark,font=arial,border=4)
    customer_detail_mobile_tb.place(relx = 0.345, rely = 0.14, anchor = NW)

    #customer_detail add button
    customer_detail_add_btn=Button(customer_detail_frame,fg=element_color,bg=element_color_dark,text="Add",width = 25,border=4,command=lambda:[])
    customer_detail_add_btn.place(relx = 0.5, rely = 0.14, anchor = NW)

    #customer_detail_ refresh btn
    customer_detail_refresh_btn=Button(customer_detail_frame,fg=element_color,bg=element_color_dark,text="Delete",width = 15,border=4,command=lambda:[])
    customer_detail_refresh_btn.place(relx = 0.03, rely = 0.67, anchor = NW)

    #customer_detail_ Delete btn
    customer_detail_delete_btn=Button(customer_detail_frame,fg=element_color,bg=element_color_dark,text="Refresh",width = 15,border=4,command=lambda:[])
    customer_detail_delete_btn.place(relx = 0.11, rely = 0.67, anchor = NW)

    #customer_detail_ Edit btn
    customer_detail_edit_btn=Button(customer_detail_frame,fg=element_color,bg=element_color_dark,text="Edit",width = 15,border=4,command=lambda:[])
    customer_detail_edit_btn.place(relx = 0.19, rely = 0.67, anchor = NW)

    #customer_detail_treeview element
    customer_detail_tree_view= Treeview(customer_detail_frame,selectmode='browse',height=23)
    customer_detail_tree_view.place(relx = 0.03, rely = 0.2, anchor = NW)

    #verticle scrollbar
    #vertical_scrollbar=Scrollbar(billing_frame,orient="vertical",command=tree_view.yview)
    #vertical_scrollbar.place(relx = 0.03, rely = 0.3, anchor = NW)
    #tree_view.configure(xscrollcommand=vertical_scrollbar.set)

    #Definning number of columns
    customer_detail_tree_view["columns"]=("1","2","3")

    #defining heading
    customer_detail_tree_view["show"]='headings'

    #modifying the size of the columns
    customer_detail_tree_view.column("1",width=100)
    customer_detail_tree_view.column("2",width=250)
    customer_detail_tree_view.column("3",width=200)

    #assigning heading name
    customer_detail_tree_view.heading("1",text="Customer Id")
    customer_detail_tree_view.heading("2",text="Customer Name")
    customer_detail_tree_view.heading("3",text="Mobile Number")'''

def item_obj():
    item_frame= Frame(root,width=1670,height=1060,bg=frame_color)
    item_frame.grid(row=0,column=1)
    item_frame.propagate(0)

    item_lbl=Label(item_frame,text="Add/Search Items",font=book_antiqua_size18,bg=frame_color,fg=element_color)
    item_lbl.place(relx = 0.4, rely = 0.065, anchor = NW)

    #item refresh btn
    item_refresh_btn=Button(item_frame,fg=element_color,bg=element_color_dark,text="Delete",width = 15,border=4,command=lambda:[])
    item_refresh_btn.place(relx = 0.03, rely = 0.67, anchor = NW)

    #item Delete btn
    item_delete_btn=Button(item_frame,fg=element_color,bg=element_color_dark,text="Refresh",width = 15,border=4,command=lambda:[])
    item_delete_btn.place(relx = 0.11, rely = 0.67, anchor = NW)

    #item Edit btn
    item_edit_btn=Button(item_frame,fg=element_color,bg=element_color_dark,text="Edit",width = 15,border=4,command=lambda:[])
    item_edit_btn.place(relx = 0.19, rely = 0.67, anchor = NW)

    item_add_btn=Button(item_frame,fg=element_color,bg=element_color_dark,text="Add",width = 15,border=4,command=lambda:[])
    item_add_btn.place(relx = 0.4, rely = 0.67, anchor = NW)

    #Id auto gen label
    item_id_tb=Entry(item_frame,fg=element_color,bg=element_color_dark,font=arial,border=4,width=11)
    item_id_tb.place(relx = 0.03, rely = 0.17, anchor = NW)
    item_id_tb.insert(0, 'Item Id')
    item_id_tb.bind("<FocusIn>", lambda args: item_id_tb.delete('0', 'end'))

    #Item Name TextBox
    item_name_tb=Entry(item_frame,fg=element_color,bg=element_color_dark,font=arial,border=4,width=26)
    item_name_tb.place(relx = 0.0925, rely = 0.17, anchor = NW)
    item_name_tb.insert(0, 'Item Name')
    item_name_tb.bind("<FocusIn>", lambda args: item_name_tb.delete('0', 'end'))

    #Quantity TextBox
    item_quantity_tb=Entry(item_frame,fg=element_color,bg=element_color_dark,font=arial,border=4,width=14)
    item_quantity_tb.place(relx = 0.239, rely = 0.17, anchor = NW)
    item_quantity_tb.insert(0, 'Stock')
    item_quantity_tb.bind("<FocusIn>", lambda args: item_quantity_tb.delete('0', 'end'))

    #Price TextBox
    item_price_tb=Entry(item_frame,fg=element_color,bg=element_color_dark,font=arial,border=4,width=13)
    item_price_tb.place(relx = 0.32, rely = 0.17, anchor = NW)
    item_price_tb.insert(0, 'Price')
    item_price_tb.bind("<FocusIn>", lambda args: item_price_tb.delete('0', 'end'))

    #Selling Price
    selling_price_tb=Entry(item_frame,fg=element_color,bg=element_color_dark,font=arial,border=4,width=14)
    selling_price_tb.place(relx = 0.395, rely = 0.17, anchor = NW)
    selling_price_tb.insert(0, 'Selling Price')
    selling_price_tb.bind("<FocusIn>", lambda args: selling_price_tb.delete('0', 'end'))

    #item treeview element
    item_tree_view= Treeview(item_frame,selectmode='browse',height=23)
    item_tree_view.place(relx = 0.03, rely = 0.2, anchor = NW)

    #verticle scrollbar
    #vertical_scrollbar=Scrollbar(billing_frame,orient="vertical",command=tree_view.yview)
    #vertical_scrollbar.place(relx = 0.03, rely = 0.3, anchor = NW)
    #tree_view.configure(xscrollcommand=vertical_scrollbar.set)

    #Definning number of columns
    item_tree_view["columns"]=("1","2","3","4","5")

    #defining heading
    item_tree_view["show"]='headings'

    #modifying the size of the columns
    item_tree_view.column("1",width=100)
    item_tree_view.column("2",width=250)
    item_tree_view.column("3",width=130)
    item_tree_view.column("4",width=130)
    item_tree_view.column("5",width=130)

    #assigning heading name
    item_tree_view.heading("1",text="Id")
    item_tree_view.heading("2",text="Item Name")
    item_tree_view.heading("3",text="Stock")
    item_tree_view.heading("4",text="Price")
    item_tree_view.heading("5",text="Selling Price")

def report_obj():
    report_frame= Frame(root,width=1670,height=1060,bg=frame_color)
    report_frame.grid(row=0,column=1)
    report_frame.propagate(0)

    report_lbl=Label(report_frame,text="Report",font=book_antiqua_size18,bg=frame_color,fg=element_color)
    report_lbl.place(relx = 0.4, rely = 0.065, anchor = NW)

    #Filter
    report_filter_lbl=Label(report_frame,text="Filter",font=book_antiqua,bg=frame_color,fg=element_color)
    report_filter_lbl.place(relx = 0.04, rely = 0.15, anchor = NW)

    report_filter_tb=Entry(report_frame,fg=element_color,bg=element_color_dark,font=arial,border=4,width=15)
    report_filter_tb.place(relx = 0.07, rely = 0.15, anchor = NW)

    #from date
    report_date_lbl=Label(report_frame,text="From",font=book_antiqua,bg=frame_color,fg=element_color)
    report_date_lbl.place(relx = 0.04, rely = 0.19, anchor = NW)
    
    today = date.today()
    report_date_tb = DateEntry(report_frame, width= 16,height=0, background= "grey", foreground= "white",bd=4, maxdate=today)
    report_date_tb.place(relx = 0.07, rely = 0.19, anchor = NW)

    #to date
    report_date_lbl=Label(report_frame,text="To",font=book_antiqua,bg=frame_color,fg=element_color)
    report_date_lbl.place(relx = 0.16, rely = 0.19, anchor = NW)
    
    report_date_tb = DateEntry(report_frame, width= 16,height=0, background= "grey", foreground= "white",bd=4, maxdate=today)
    report_date_tb.place(relx = 0.177, rely = 0.19, anchor = NW)

    #Search btn
    report_seacrh_btn=Button(report_frame,fg=element_color,bg=element_color_dark,text="Search",width = 16,border=4,command=lambda:[])
    report_seacrh_btn.place(relx = 0.27, rely = 0.19, anchor = NW)
    
    #Show details btn
    report_show_details_btn=Button(report_frame,fg=element_color,bg=element_color_dark,text="Show Details",width = 16,border=4,command=lambda:[])
    report_show_details_btn.place(relx = 0.365, rely = 0.19, anchor = NW)

    #treeview element
    report_tree_view= Treeview(report_frame,selectmode='browse',height=23)
    report_tree_view.place(relx = 0.03, rely = 0.23, anchor = NW)

    #verticle scrollbar
    #vertical_scrollbar=Scrollbar(billing_frame,orient="vertical",command=tree_view.yview)
    #vertical_scrollbar.place(relx = 0.03, rely = 0.3, anchor = NW)
    #tree_view.configure(xscrollcommand=vertical_scrollbar.set)

    #Definning number of columns
    report_tree_view["columns"]=("1","2","3","4","5")

    #defining heading
    report_tree_view["show"]='headings'

    #modifying the size of the columns
    report_tree_view.column("1",width=100)
    report_tree_view.column("2",width=100)
    report_tree_view.column("3",width=250)
    report_tree_view.column("4",width=150)
    report_tree_view.column("5",width=100)

    #assigning heading name
    report_tree_view.heading("1",text="Bill No")
    report_tree_view.heading("2",text="Date")
    report_tree_view.heading("3",text="Customer Name")
    report_tree_view.heading("4",text="Customer Number")
    report_tree_view.heading("5",text="Amount")

def billing_obj():
    billing_frame=Frame(root,width=1670,height=1060,bg=frame_color)
    billing_frame.grid(row=0,column=1)
    billing_frame.propagate(0)

    billing_lbl=Label(billing_frame,text="Billing",font=book_antiqua_size18,bg=frame_color,fg=element_color)
    billing_lbl.place(relx = 0.4, rely = 0.065, anchor = NW)
    
    #Customer Name
    billing_customer_name_lbl=Label(billing_frame,text="Customer Name",font=book_antiqua,bg=frame_color,fg=element_color)
    billing_customer_name_lbl.place(relx = 0.04, rely = 0.14, anchor = NW)

    billing_customer_name_tb=Entry(billing_frame,fg=element_color,bg=element_color_dark,font=arial,border=4,width=25)
    billing_customer_name_tb.place(relx = 0.115, rely = 0.14, anchor = NW)

    #Customer Mobile NUmber
    billing_mobile_lbl=Label(billing_frame,text="Mobile",font=book_antiqua,bg=frame_color,fg=element_color)
    billing_mobile_lbl.place(relx = 0.27, rely = 0.14, anchor = NW)

    billing_mobile_tb=Entry(billing_frame,font=arial,fg=element_color,bg=element_color_dark,border=4)
    billing_mobile_tb.place(relx = 0.305, rely = 0.14, anchor = NW)

    #Bill Number
    billing_bill_number_lbl=Label(billing_frame,text="Bill Number",font=book_antiqua,bg=frame_color,fg=element_color)
    billing_bill_number_lbl.place(relx = 0.43, rely = 0.14, anchor = NW)

    billing_bill_number_tb=Entry(billing_frame,fg=element_color,bg=element_color_dark,font=arial,border=4)
    billing_bill_number_tb.place(relx = 0.485, rely = 0.14, anchor = NW)

    #billed date
    today = date.today()
    billing_billed_date = DateEntry(billing_frame, width= 16,height=0, background= "grey", foreground= "white",bd=4, maxdate=today)
    billing_billed_date.place(relx = 0.612, rely = 0.14, anchor = NW)


    
    #Item Code TextBox
    billing_item_code_tb=Entry(billing_frame,fg=element_color,bg=element_color_dark,font=arial,border=4,width=16)
    billing_item_code_tb.place(relx = 0.03, rely = 0.22, anchor = NW)
    billing_item_code_tb.insert(0, 'Item Code')
    billing_item_code_tb.bind("<FocusIn>", lambda args: billing_item_code_tb.delete('0', 'end'))

    #Item Name TextBox
    billing_item_name_tb=Entry(billing_frame,fg=element_color,bg=element_color_dark,font=arial,border=4,width=28)
    billing_item_name_tb.place(relx = 0.12, rely = 0.22, anchor = NW)
    billing_item_name_tb.insert(0, 'Item Name')
    billing_item_name_tb.bind("<FocusIn>", lambda args: billing_item_name_tb.delete('0', 'end'))

    #Quantity TextBox
    billing_quantity_tb=Entry(billing_frame,fg=element_color,bg=element_color_dark,font=arial,border=4,width=10)
    billing_quantity_tb.place(relx = 0.275, rely = 0.22, anchor = NW)
    billing_quantity_tb.insert(0, 'Quantity')
    billing_quantity_tb.bind("<FocusIn>", lambda args: billing_quantity_tb.delete('0', 'end'))

    #Add Button
    billing_add_update_btn=Button(billing_frame,fg=element_color,bg=element_color_dark,text="Add",width = 21,border=4,command=lambda:[])
    billing_add_update_btn.place(relx = 0.648, rely = 0.22, anchor = NW)

    #treeview element
    billing_tree_view= Treeview(billing_frame,selectmode='browse',height=23)
    billing_tree_view.place(relx = 0.03, rely = 0.25, anchor = NW)
    
    

    #verticle scrollbar
    #vertical_scrollbar=Scrollbar(billing_frame,orient="vertical",command=tree_view.yview)
    #vertical_scrollbar.place(relx = 0.03, rely = 0.3, anchor = NW)
    #tree_view.configure(xscrollcommand=vertical_scrollbar.set)

    #Definning number of columns
    billing_tree_view["columns"]=("1","2","3","4","5","6","7","8")

    #defining heading
    billing_tree_view["show"]='headings'

    #modifying the size of the columns
    billing_tree_view.column("1",width=150)
    billing_tree_view.column("2",width=260)
    billing_tree_view.column("3",width=100)
    billing_tree_view.column("4",width=100)
    billing_tree_view.column("5",width=160)
    billing_tree_view.column("6",width=160)
    billing_tree_view.column("7",width=100)
    billing_tree_view.column("8",width=160)

    #assigning heading name
    billing_tree_view.heading("1",text="ItemCode")
    billing_tree_view.heading("2",text="Item Name")
    billing_tree_view.heading("3",text="Quantity")
    billing_tree_view.heading("4",text="Price")
    billing_tree_view.heading("5",text="CGST")
    billing_tree_view.heading("6",text="SGST")
    billing_tree_view.heading("7",text="Discount")
    billing_tree_view.heading("8",text="Total")

    billing_tree_view.insert("", 0, "item", text="item")


    #Delete Button
    delete_btn=Button(billing_frame,fg=element_color,bg=element_color_dark,text="Delete",width = 15,border=4,command=lambda:[])
    delete_btn.place(relx = 0.0275, rely = 0.71, anchor = NW)

    #Total Gst Label
    total_cgst_lbl=Label(billing_frame,text="Total CGST",font=book_antiqua,bg=frame_color,fg=element_color)
    total_cgst_lbl.place(relx = 0.41, rely = 0.71, anchor = NW)

    total_cgst_lbl2=Label(billing_frame,text="RS.00%",font=book_antiqua,bg=frame_color,fg=element_color)
    total_cgst_lbl2.place(relx = 0.465, rely = 0.71, anchor = NW)

    #Total Sgst Label
    total_sgst_lbl=Label(billing_frame,text="Total SGST",font=book_antiqua,bg=frame_color,fg=element_color)
    total_sgst_lbl.place(relx = 0.41, rely = 0.735, anchor = NW)

    total_sgst_lbl2=Label(billing_frame,text="RS.00%",font=book_antiqua,bg=frame_color,fg=element_color)
    total_sgst_lbl2.place(relx = 0.465, rely = 0.735, anchor = NW)

    #Total
    total_lbl=Label(billing_frame,text="RS.000000",font=book_antiqua_size18,bg=frame_color,fg=element_color)
    total_lbl.place(relx = 0.66, rely = 0.715, anchor = NW)

    #Save And Print Button
    save_print_button=Button(billing_frame,fg=element_color,bg=element_color_dark,text="Save & Print",width = 16,height=2,border=4,command=lambda:[])
    save_print_button.place(relx = 0.66, rely = 0.755, anchor = NW)


menu_frame_obj()
#company_details_obj()
purchase_obj()

root.mainloop()