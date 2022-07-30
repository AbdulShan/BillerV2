#All necessary Packages
from asyncio.windows_events import NULL
import datetime
from tkinter import *
import sqlite3
from tkinter.ttk import Treeview
import atexit
from os import path
from turtle import bgcolor
import fpdf
from json import dumps, loads
import atexit
from tkcalendar import Calendar, DateEntry


#font
book_antiqua=("Book Antiqua",12)
arial=('Arial', 12)
book_antiqua_size18=("Book Antiqua",18,"bold underline")

#date and time, sorting date into dd/mm/yyyy
date=datetime.date.today()
datesorted=date.strftime("%d-%m-%Y")

#Bill Number Counter
def read_counter():
    #reads the Bill number from the counter.json file
    return loads(open("counter.json", "r").read()) + 1 if path.exists("counter.json") else 0
def write_counter():
    #writes/saves the Bill Number in counter.json file
    with open("counter.json", "w") as f:
        f.write(dumps(bill_number))
bill_number = read_counter()

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
    menu_frame= Frame(root,bg="#5f6363",width=250,height=1060)
    menu_frame.grid(row=0,column=0)
    menu_frame.propagate(0)

    img=PhotoImage(file='logo.png')
    image = Label(menu_frame,image=img)

def menu_frame_obj():
    image.place(relx = 0.45, rely = 0.075, anchor = CENTER)

    billing_btn=Button(menu_frame,text="Billing",width = 25,command=lambda:[billing_obj()])
    billing_btn.place(relx = 0.475, rely = 0.23, anchor = CENTER)

    purchase_btn=Button(menu_frame,text="Purchase",width = 25,command=lambda:[purchase_obj()])
    purchase_btn.place(relx = 0.475, rely = 0.26, anchor = CENTER)

    customer_btn=Button(menu_frame,text="Customer",width = 25,command=lambda:[customer_detail_obj()])
    customer_btn.place(relx = 0.475, rely = 0.29, anchor = CENTER)

    item_btn=Button(menu_frame,text="Items",width = 25,command=lambda:[item_obj()])
    item_btn.place(relx = 0.475, rely = 0.32, anchor = CENTER)

    dealer_btn=Button(menu_frame,text="Dealer",width = 25,command=lambda:[dealer_obj()])
    dealer_btn.place(relx = 0.475, rely = 0.35, anchor = CENTER)

    reports_btn=Button(menu_frame,text="Reports",width = 25,command=lambda:[])
    reports_btn.place(relx = 0.475, rely = 0.38, anchor = CENTER)

    company_details_btn=Button(menu_frame,text="Company",width = 25,command=lambda:[company_details_obj()])
    company_details_btn.place(relx = 0.475, rely = 0.41, anchor = CENTER)

def company_details_obj():
    company_details_frame= Frame(root,width=1670,height=1060)
    company_details_frame.grid(row=0,column=1)
    company_details_frame.propagate(0)

    #Company Name
    company_name_lbl=Label(company_details_frame,text="Company Name",font=book_antiqua)
    company_name_lbl.place(relx = 0.1, rely = 0.2, anchor = NW)

    company_name_tb=Entry(company_details_frame,font=arial,border=4)
    company_name_tb.place(relx = 0.2, rely = 0.2, anchor = NW)

    #Company Adress
    company_adress_lbl=Label(company_details_frame,text="Company Adress",font=book_antiqua)
    company_adress_lbl.place(relx = 0.1, rely = 0.24, anchor = NW)

    company_adress_tb=Entry(company_details_frame,font=arial,border=4)
    company_adress_tb.place(relx = 0.2, rely = 0.24, anchor = NW)

    #Company GSTIN
    company_gstin_lbl=Label(company_details_frame,text="Company GSTIN",font=book_antiqua)
    company_gstin_lbl.place(relx = 0.1, rely = 0.28, anchor = NW)

    company_gstin_tb=Entry(company_details_frame,font=arial,border=4)
    company_gstin_tb.place(relx = 0.2, rely = 0.28, anchor = NW)

    #Company Adress
    company_contact_number_lbl=Label(company_details_frame,text="Company Adress",font=book_antiqua)
    company_contact_number_lbl.place(relx = 0.1, rely = 0.32, anchor = NW)

    company_contact_number_tb=Entry(company_details_frame,font=arial,border=4)
    company_contact_number_tb.place(relx = 0.2, rely = 0.32, anchor = NW)

    #Update BUtton and message
    add_update_btn=Button(company_details_frame,text="Add/Update Details",width = 25,border=4,command=lambda:[details_updated_obj()])
    add_update_btn.place(relx = 0.1, rely = 0.38, anchor = NW)

    def details_updated_obj():
        if company_name_tb.get() =="" or company_adress_tb.get() =="" or company_gstin_tb.get() =="" or company_contact_number_tb.get() =="":
            message_lbl=Label(company_details_frame,text='Enter All Fields',font=book_antiqua,fg="#2ea307")
            message_lbl.place(relx = 0.1, rely = 0.42, anchor = NW)
        else:
            message_lbl=Label(company_details_frame,text='Details Updated',font=book_antiqua,fg="#2ea307")
            message_lbl.place(relx = 0.1, rely = 0.42, anchor = NW)

def billing_obj():
    billing_frame=Frame(root,width=1670,height=1060)
    billing_frame.grid(row=0,column=1)
    billing_frame.propagate(0)

    billing_lbl=Label(billing_frame,text="Billing",font=book_antiqua_size18)
    billing_lbl.place(relx = 0.4, rely = 0.065, anchor = NW)
    
    #Customer Name
    billing_customer_name_lbl=Label(billing_frame,text="Customer Name",font=book_antiqua)
    billing_customer_name_lbl.place(relx = 0.04, rely = 0.14, anchor = NW)

    billing_customer_name_tb=Entry(billing_frame,font=arial,border=4,width=30)
    billing_customer_name_tb.place(relx = 0.115, rely = 0.14, anchor = NW)

    #Customer Mobile NUmber
    billing_mobile_lbl=Label(billing_frame,text="Mobile",font=book_antiqua)
    billing_mobile_lbl.place(relx = 0.31, rely = 0.14, anchor = NW)

    billing_mobile_tb=Entry(billing_frame,font=arial,border=4)
    billing_mobile_tb.place(relx = 0.345, rely = 0.14, anchor = NW)

    #Bill Number
    billing_bill_number_lbl=Label(billing_frame,text="Bill Number",font=book_antiqua)
    billing_bill_number_lbl.place(relx = 0.5, rely = 0.14, anchor = NW)

    billing_bill_number_tb=Entry(billing_frame,font=arial,border=4)
    billing_bill_number_tb.place(relx = 0.555, rely = 0.14, anchor = NW)

    #Item Code TextBox
    billing_item_code_tb=Entry(billing_frame,font=arial,border=4,width=16)
    billing_item_code_tb.place(relx = 0.03, rely = 0.22, anchor = NW)
    billing_item_code_tb.insert(0, 'Item Code')
    billing_item_code_tb.bind("<FocusIn>", lambda args: billing_item_code_tb.delete('0', 'end'))

    #Item Name TextBox
    billing_item_name_tb=Entry(billing_frame,font=arial,border=4,width=28)
    billing_item_name_tb.place(relx = 0.12, rely = 0.22, anchor = NW)
    billing_item_name_tb.insert(0, 'Item Name')
    billing_item_name_tb.bind("<FocusIn>", lambda args: billing_item_name_tb.delete('0', 'end'))

    #Quantity TextBox
    billing_quantity_tb=Entry(billing_frame,font=arial,border=4,width=10)
    billing_quantity_tb.place(relx = 0.275, rely = 0.22, anchor = NW)
    billing_quantity_tb.insert(0, 'Quantity')
    billing_quantity_tb.bind("<FocusIn>", lambda args: billing_quantity_tb.delete('0', 'end'))

    #Add Button
    billing_add_update_btn=Button(billing_frame,text="Add",width = 21,border=4,command=lambda:[])
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


    #Delete Button
    delete_btn=Button(billing_frame,text="Delete",width = 15,border=4,command=lambda:[])
    delete_btn.place(relx = 0.0275, rely = 0.71, anchor = NW)

    #Total Gst Label
    total_cgst_lbl=Label(billing_frame,text="Total CGST",font=book_antiqua)
    total_cgst_lbl.place(relx = 0.41, rely = 0.71, anchor = NW)

    total_cgst_lbl2=Label(billing_frame,text="RS.00%",font=book_antiqua)
    total_cgst_lbl2.place(relx = 0.465, rely = 0.71, anchor = NW)

    #Total Sgst Label
    total_sgst_lbl=Label(billing_frame,text="Total SGST",font=book_antiqua)
    total_sgst_lbl.place(relx = 0.41, rely = 0.735, anchor = NW)

    total_sgst_lbl2=Label(billing_frame,text="RS.00%",font=book_antiqua)
    total_sgst_lbl2.place(relx = 0.465, rely = 0.735, anchor = NW)

    #Total
    total_lbl=Label(billing_frame,text="RS.000000",font=book_antiqua_size18)
    total_lbl.place(relx = 0.66, rely = 0.715, anchor = NW)

    #Save And Print Button
    save_print_button=Button(billing_frame,text="Save & Print",width = 16,height=2,border=4,command=lambda:[])
    save_print_button.place(relx = 0.66, rely = 0.755, anchor = NW)

def purchase_obj():
    purchase_frame= Frame(root,width=1670,height=1060)
    purchase_frame.grid(row=0,column=1)
    purchase_frame.propagate(0)

    purchase_details_lbl=Label(purchase_frame,text="Purchase Details",font=book_antiqua_size18)
    purchase_details_lbl.place(relx = 0.4, rely = 0.065, anchor = NW)

    #Dealer name
    dealer_name_lbl=Label(purchase_frame,text="Dealer Name",font=book_antiqua)
    dealer_name_lbl.place(relx = 0.04, rely = 0.14, anchor = NW)

    dealer_name_tb=Entry(purchase_frame,font=arial,border=4,width=25)
    dealer_name_tb.place(relx = 0.105, rely = 0.14, anchor = NW)
    

    #Dealer Gstin
    dealer_gstin_lbl=Label(purchase_frame,text="GSTIN",font=book_antiqua)
    dealer_gstin_lbl.place(relx = 0.265, rely = 0.14, anchor = NW)

    dealer_gstin_tb=Entry(purchase_frame,font=arial,border=4)
    dealer_gstin_tb.place(relx = 0.3, rely = 0.14, anchor = NW)

    #Purchase Date
    purchase_date_lbl=Label(purchase_frame,text="Date",font=book_antiqua)
    purchase_date_lbl.place(relx = 0.43, rely = 0.14, anchor = NW)

    today = date.today()
    purchase_date_tb = DateEntry(purchase_frame, width= 16,height=0, background= "grey", foreground= "white",bd=4, maxdate=today)
    purchase_date_tb.place(relx = 0.455, rely = 0.1405, anchor = NW)

    #Purchase INvoice Number
    invoice_number_lbl=Label(purchase_frame,text="Invoice Number",font=book_antiqua)
    invoice_number_lbl.place(relx = 0.55, rely = 0.14, anchor = NW)

    invoice_number_tb=Entry(purchase_frame,font=arial,border=4)
    invoice_number_tb.place(relx = 0.62, rely = 0.14, anchor = NW)

    #Purchase Item Code TextBox
    purchase_item_code_tb=Entry(purchase_frame,font=arial,border=4,width=14)
    purchase_item_code_tb.place(relx = 0.03, rely = 0.22, anchor = NW)
    purchase_item_code_tb.insert(0, 'Item Code')
    purchase_item_code_tb.bind("<FocusIn>", lambda args: purchase_item_code_tb.delete('0', 'end'))

    #Purchase Item Name TextBox
    purchase_item_name_tb=Entry(purchase_frame,font=arial,border=4,width=28)
    purchase_item_name_tb.place(relx = 0.11, rely = 0.22, anchor = NW)
    purchase_item_name_tb.insert(0, 'Item Name')
    purchase_item_name_tb.bind("<FocusIn>", lambda args: purchase_item_name_tb.delete('0', 'end'))

    #Purchase Quantity TextBox
    purchase_quantity_tb=Entry(purchase_frame,font=arial,border=4,width=10)
    purchase_quantity_tb.place(relx = 0.266, rely = 0.22, anchor = NW)
    purchase_quantity_tb.insert(0, 'Quantity')
    purchase_quantity_tb.bind("<FocusIn>", lambda args: purchase_quantity_tb.delete('0', 'end'))

    #Purchase Price
    purchase_price_tb=Entry(purchase_frame,font=arial,border=4,width=10)
    purchase_price_tb.place(relx = 0.325, rely = 0.22, anchor = NW)
    purchase_price_tb.insert(0, 'Price')
    purchase_price_tb.bind("<FocusIn>", lambda args: purchase_price_tb.delete('0', 'end'))


    #Purchase Add Button
    purchase_add_update_btn=Button(purchase_frame,text="Add",width = 21,border=4,command=lambda:[])
    purchase_add_update_btn.place(relx = 0.384, rely = 0.22, anchor = NW)

    #Purchase Delete Button
    purchase_delete_btn=Button(purchase_frame,text="Delete",width = 21,border=4,command=lambda:[])
    purchase_delete_btn.place(relx = 0.0275, rely = 0.71, anchor = NW)

    #Purchase Total
    purchase_total_lbl=Label(purchase_frame,text="RS.000000",font=book_antiqua_size18)
    purchase_total_lbl.place(relx = 0.4, rely = 0.715, anchor = NW)

    #Purchase save
    purchase_print_button=Button(purchase_frame,text="Save",width = 16,height=2,border=4,command=lambda:[])
    purchase_print_button.place(relx = 0.4, rely = 0.755, anchor = NW)


    #treeview element
    purchase_tree_view= Treeview(purchase_frame,selectmode='browse',height=23)
    purchase_tree_view.place(relx = 0.03, rely = 0.25, anchor = NW)

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

def customer_detail_obj():
    customer_detail_frame=Frame(root,width=1670,height=1060)
    customer_detail_frame.grid(row=0,column=1)
    customer_detail_frame.propagate(0)

    customer_detail_customer_details_lbl=Label(customer_detail_frame,text="Customer Details",font=book_antiqua_size18)
    customer_detail_customer_details_lbl.place(relx = 0.4, rely = 0.065, anchor = NW)
    
    #customer_detail_ Customer Name
    customer_detail_customer_name_lbl=Label(customer_detail_frame,text="Customer Name",font=book_antiqua)
    customer_detail_customer_name_lbl.place(relx = 0.04, rely = 0.14, anchor = NW)

    customer_detail_customer_name_tb=Entry(customer_detail_frame,font=arial,border=4,width=30)
    customer_detail_customer_name_tb.place(relx = 0.115, rely = 0.14, anchor = NW)

    #customer_detail_ Customer Mobile NUmber
    customer_detail_mobile_lbl=Label(customer_detail_frame,text="Mobile",font=book_antiqua)
    customer_detail_mobile_lbl.place(relx = 0.31, rely = 0.14, anchor = NW)

    customer_detail_mobile_tb=Entry(customer_detail_frame,font=arial,border=4)
    customer_detail_mobile_tb.place(relx = 0.345, rely = 0.14, anchor = NW)

    #customer_detail_ Bill Number
    customer_detail_bill_number_lbl=Label(customer_detail_frame,text="Bill Number",font=book_antiqua)
    customer_detail_bill_number_lbl.place(relx = 0.5, rely = 0.14, anchor = NW)

    customer_detail_bill_number_tb=Entry(customer_detail_frame,font=arial,border=4)
    customer_detail_bill_number_tb.place(relx = 0.555, rely = 0.14, anchor = NW)

    #customer_detail add button
    customer_detail_add_btn=Button(customer_detail_frame,text="Add",width = 25,border=4,command=lambda:[])
    customer_detail_add_btn.place(relx = 0.69, rely = 0.14, anchor = NW)

    #customer_detail_ refresh btn
    customer_detail_refresh_btn=Button(customer_detail_frame,text="Delete",width = 15,border=4,command=lambda:[])
    customer_detail_refresh_btn.place(relx = 0.03, rely = 0.67, anchor = NW)

    #customer_detail_ Delete btn
    customer_detail_delete_btn=Button(customer_detail_frame,text="Refresh",width = 15,border=4,command=lambda:[])
    customer_detail_delete_btn.place(relx = 0.11, rely = 0.67, anchor = NW)

    #customer_detail_ Edit btn
    customer_detail_edit_btn=Button(customer_detail_frame,text="Edit",width = 15,border=4,command=lambda:[])
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
    customer_detail_tree_view.heading("3",text="Mobile Number")

def item_obj():
    item_frame= Frame(root,width=1670,height=1060)
    item_frame.grid(row=0,column=1)
    item_frame.propagate(0)

    item_lbl=Label(item_frame,text="Add Items",font=book_antiqua_size18)
    item_lbl.place(relx = 0.4, rely = 0.065, anchor = NW)

    #item refresh btn
    item_refresh_btn=Button(item_frame,text="Delete",width = 15,border=4,command=lambda:[])
    item_refresh_btn.place(relx = 0.03, rely = 0.67, anchor = NW)

    #item Delete btn
    item_delete_btn=Button(item_frame,text="Refresh",width = 15,border=4,command=lambda:[])
    item_delete_btn.place(relx = 0.11, rely = 0.67, anchor = NW)

    #item Edit btn
    item_edit_btn=Button(item_frame,text="Edit",width = 15,border=4,command=lambda:[])
    item_edit_btn.place(relx = 0.19, rely = 0.67, anchor = NW)

    item_add_btn=Button(item_frame,text="Add",width = 15,border=4,command=lambda:[])
    item_add_btn.place(relx = 0.4, rely = 0.67, anchor = NW)

    #Id auto gen label
    item_id_lbl=Label(item_frame,text="ID-Auto Gen",font=book_antiqua)
    item_id_lbl.place(relx = 0.03, rely = 0.17, anchor = NW)

    #Item Name TextBox
    item_name_tb=Entry(item_frame,font=arial,border=4,width=26)
    item_name_tb.place(relx = 0.094, rely = 0.17, anchor = NW)
    item_name_tb.insert(0, 'Item Name')
    item_name_tb.bind("<FocusIn>", lambda args: item_name_tb.delete('0', 'end'))

    #Quantity TextBox
    item_quantity_tb=Entry(item_frame,font=arial,border=4,width=14)
    item_quantity_tb.place(relx = 0.239, rely = 0.17, anchor = NW)
    item_quantity_tb.insert(0, 'Stock')
    item_quantity_tb.bind("<FocusIn>", lambda args: item_quantity_tb.delete('0', 'end'))

    #Price TextBox
    item_price_tb=Entry(item_frame,font=arial,border=4,width=13)
    item_price_tb.place(relx = 0.32, rely = 0.17, anchor = NW)
    item_price_tb.insert(0, 'Price')
    item_price_tb.bind("<FocusIn>", lambda args: item_price_tb.delete('0', 'end'))

    #Selling Price
    selling_price_tb=Entry(item_frame,font=arial,border=4,width=14)
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

def dealer_obj():
    dealer_frame= Frame(root,width=1670,height=1060)
    dealer_frame.grid(row=0,column=1)
    dealer_frame.propagate(0)

    dealer_lbl=Label(dealer_frame,text="Dealer Details",font=book_antiqua_size18)
    dealer_lbl.place(relx = 0.4, rely = 0.065, anchor = NW)

    #dealer Name
    dealer_name_lbl=Label(dealer_frame,text="Dealer Name",font=book_antiqua)
    dealer_name_lbl.place(relx = 0.04, rely = 0.14, anchor = NW)

    dealer_name_tb=Entry(dealer_frame,font=arial,border=4,width=20)
    dealer_name_tb.place(relx = 0.115, rely = 0.14, anchor = NW)

    #dealer GSTIN Number
    dealer_gstin_number_lbl=Label(dealer_frame,text="GSTIN No",font=book_antiqua)
    dealer_gstin_number_lbl.place(relx = 0.25, rely = 0.14, anchor = NW)

    dealer_gstin_number_tb=Entry(dealer_frame,font=arial,border=4)
    dealer_gstin_number_tb.place(relx = 0.3, rely = 0.14, anchor = NW)

    #dealer Address
    dealer_address_lbl=Label(dealer_frame,text="Address",font=book_antiqua)
    dealer_address_lbl.place(relx = 0.429, rely = 0.14, anchor = NW)

    dealer_address_tb=Entry(dealer_frame,font=arial,border=4)
    dealer_address_tb.place(relx = 0.475, rely = 0.14, anchor = NW)

    #dealer Contact
    dealer_contact_number_lbl=Label(dealer_frame,text="Contact Number",font=book_antiqua)
    dealer_contact_number_lbl.place(relx = 0.0385, rely = 0.19, anchor = NW)

    dealer_contact_number_tb=Entry(dealer_frame,font=arial,border=4)
    dealer_contact_number_tb.place(relx = 0.115, rely = 0.19, anchor = NW)

    #dealer add button
    dealer_add_btn=Button(dealer_frame,text="Add",width = 15,border=4,command=lambda:[])
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
    dealer_refresh_btn=Button(dealer_frame,text="Delete",width = 15,border=4,command=lambda:[])
    dealer_refresh_btn.place(relx = 0.04, rely = 0.7, anchor = NW)

    #dealer Delete btn
    dealer_delete_btn=Button(dealer_frame,text="Refresh",width = 15,border=4,command=lambda:[])
    dealer_delete_btn.place(relx = 0.12, rely = 0.7, anchor = NW)

    #dealer Edit btn
    dealer_edit_btn=Button(dealer_frame,text="Edit",width = 15,border=4,command=lambda:[])
    dealer_edit_btn.place(relx = 0.2, rely = 0.7, anchor = NW)

def report_obj():
    report_frame= Frame(root,width=1670,height=1060)
    report_frame.grid(row=0,column=1)
    report_frame.propagate(0)

    

menu_frame_obj()
#company_details_obj()
report_obj()
root.mainloop()