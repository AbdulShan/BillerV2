#All necessary Packages
from tkinter import messagebox, ttk, Button, Frame, Label, Scrollbar, Toplevel, PhotoImage, BOTTOM, LEFT, RIGHT, CENTER, X, Y, Tk, Entry, NW, END, Text
from tkinter.ttk import Style, Treeview
from tkcalendar import DateEntry
from asyncio.windows_events import NULL
import datetime
import sqlite3
from os import path, mkdir
import fpdf
from json import dumps, loads

#font
book_antiqua=("Helvetica Neue Light",12,"normal")
arial=('Arial', 12)
book_antiqua_size18=("Book Antiqua",18,"bold")

frame_color='#242729'

element_color='white'
entry_box_color='#666869'

menu_button_color='#0b5a8c'
frame_button_color='#165a72'

tree_view_color_bg='#242729'
tree_view_color_fg='#242729'

selection_color='darkblue'

menu_button_height=4

def make_directory(directory_name):
    try:
        mkdir('{}'.format(directory_name))
    except FileExistsError:
        print('file exists')

make_directory('Billed Bills')
make_directory('JSON Files')
make_directory('Database')
make_directory('LOGO')
make_directory('GIT')

#date and time, sorting date into dd/mm/yyyy
date=datetime.date.today()
datesorted=date.strftime("%d-%m-%Y")

#Bill Number Counter
def read_counter(filename):
    #reads the Bill number from the counter.json file
    if path.exists("JSON Files/{}.json".format(filename)):
            if filename=='company_details' or 'cleaner' or 'bool_for_cleaner':
                return loads(open("JSON Files/{}.json".format(filename), "r").read())
            
def bill_num(filename):
    if path.exists("JSON Files/{}.json".format(filename)):
        if filename=='bill_number':
                    return loads(open("JSON Files/{}.json".format(filename), "r").read()) + 1 if path.exists("JSON Files/{}.json".format(filename)) else 0
    
def write_counter(filename,data_to_write):
    #writes/saves the Bill Number in counter.json file
    with open("JSON Files/{}.json".format(filename), "w") as f:
        f.write(dumps(data_to_write))

#bill_number = read_counter('bill_number')

def scroll_bar(frame_name,widget):
    if frame_name=='menu_frame':
        v = Scrollbar(widget, orient = 'vertical')
        v.pack(side = LEFT, fill = Y)
    else:
        h = Scrollbar(widget, orient = 'horizontal')
        h.pack(side = BOTTOM, fill = X)
        v = Scrollbar(widget,orient = 'vertical')
        v.pack(side = RIGHT, fill = Y)

    #t = Text(widget, width = 15, height = 15, wrap = NONE,xscrollcommand = h.set,yscrollcommand = v.set)

#Tkinter window configs
if "__main__"==__name__:
    root=Tk()
    root.title("Billing App")
    root.iconbitmap('LOGO/logo.png')
    #get your Windows width/height, set size to full window
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    #wont allow to resize window, and full screen when opening
    root.resizable(False,False)
    root.state('zoomed')

def openeditwindow():
    global editwindow
    editwindow = Toplevel(root)
    editwindow.grab_set()
    editwindow.title("Edit")
    editwindow.geometry('%dx%d+%d+%d' % (332, 140, 800, 400))
    editwindow.resizable(False,False)

    #Logo
menu_frame= Frame(root,bg="#161719",width=250,height=1060)
menu_frame.grid(row=0,column=0)
menu_frame.propagate(0)

img=PhotoImage(file='LOGO/logo.png')
image = Label(menu_frame,image=img)

style = Style(root)
style.theme_use("clam")
style.configure("Treeview", background=tree_view_color_bg,fieldbackground=tree_view_color_fg, foreground="white")

def clear_all(treeview_name):
        for item in treeview_name.get_children():
            treeview_name.delete(item)

def selected_item_from_treeview(treeview_name,treeview_name_string):
    curItem = treeview_name.focus()
    treeview_name.item(curItem)
    selected_items =treeview_name.item(curItem)
    if treeview_name_string=='purchase_tree_view' or 'item_tree_view':
        for key, value in selected_items.items():
            if key == 'values':
                selected_treeview_item=value[0]
                return selected_treeview_item

def delete_previous_frame(frame_name,frame_var):
    if frame_name=='company_details_frame':
        code='{}.destroy()'.format(frame_var)
        exec(code)
    elif frame_name=='purchase_frame':
        code='{}.destroy()'.format(frame_var)
        exec(code)
    elif frame_name=='dealer_frame':
        code='{}.destroy()'.format(frame_var)
        exec(code)
    elif frame_name=='item_frame':
        code='{}.destroy()'.format(frame_var)
        exec(code)
    elif frame_name=='report_frame':
        code='{}.destroy()'.format(frame_var)
        exec(code)
    elif frame_name=='billing_frame':
        code='{}.destroy()'.format(frame_var)
        exec(code)
    else:
        print()

def menu_frame_obj():
    image.place(relx = 0.45, rely = 0.075, anchor = CENTER)

    global company_details_btn,purchase_btn,dealer_btn,item_btn,reports_btn,billing_btn
    company_details_btn=Button(menu_frame,text="Company",width = 25,height=menu_button_height,fg=element_color,bg=menu_button_color,command=lambda:[company_details_obj()])
    purchase_btn=Button(menu_frame,text="Purchased Items",width = 25,fg=element_color,height=menu_button_height,bg=menu_button_color,command=lambda:[purchase_obj()])
    dealer_btn=Button(menu_frame,text="Dealer",width = 25,fg=element_color,height=menu_button_height,bg=menu_button_color,command=lambda:[dealer_obj()])    
    '''customer_btn=Button(menu_frame,text="Customer",width = 25,fg=element_color,bg=menu_button_color,command=lambda:[customer_detail_obj()])
    customer_btn.place(relx = 0.475, rely = 0.35, anchor = CENTER)'''

    item_btn=Button(menu_frame,text="Items",width = 25,fg=element_color,height=menu_button_height,bg=menu_button_color,command=lambda:[item_obj()])
    reports_btn=Button(menu_frame,text="Reports",width = 25,fg=element_color,height=menu_button_height,bg=menu_button_color,command=lambda:[report_obj()])
    billing_btn=Button(menu_frame,text="Billing",width = 25,fg=element_color,height=menu_button_height,bg=menu_button_color,command=lambda:[billing_obj()])

    def place_menu(clicks):
        y=0.3+clicks
        add=0.075
        company_details_btn.place(relx = 0.475, rely = y, anchor = CENTER)
        y+=add
        purchase_btn.place(relx = 0.475, rely = y, anchor = CENTER)
        y+=add
        dealer_btn.place(relx = 0.475, rely = y, anchor = CENTER)
        y+=add
        item_btn.place(relx = 0.475, rely = y, anchor = CENTER)
        y+=add
        reports_btn.place(relx = 0.475, rely = y, anchor = CENTER)
        y+=add
        billing_btn.place(relx = 0.475, rely = y, anchor = CENTER)
    place_menu(-0.1)
    '''top_scrollbar= Button(menu_frame,text="v",width=2,fg=element_color,bg=menu_button_color,command=lambda:[place_menu(0.1)])
    top_scrollbar.place(relx = 0.95, rely = 0.5, anchor = CENTER)
    bottom_scrollbar=Button(menu_frame,text="^",width=2,fg=element_color,bg=menu_button_color,command=lambda:[place_menu(-0.1)])
    bottom_scrollbar.place(relx = 0.95, rely = 0.4, anchor = CENTER)'''

def company_details_obj():
    company_details_btn.config(state='disabled',bg='darkblue')
    purchase_btn.config(state='normal',bg=menu_button_color)
    dealer_btn.config(state='normal',bg=menu_button_color)
    item_btn.config(state='normal',bg=menu_button_color)
    reports_btn.config(state='normal',bg=menu_button_color)
    billing_btn.config(state='normal',bg=menu_button_color)

    r=read_counter('cleaner')
    if read_counter('bool_for_cleaner')=='True':
        delete_previous_frame('company_details_frame',r)
    write_counter('cleaner','company_details_frame')
    write_counter('bool_for_cleaner','True')

    global company_details_frame
    company_details_frame= Frame(root,width=1670,height=1060,bg=frame_color)
    company_details_frame.grid(row=0,column=1)
    company_details_frame.propagate(0)

    #Company Name
    company_name_lbl=Label(company_details_frame,text="Company Name",font=book_antiqua,bg=frame_color,fg=element_color)
    company_name_lbl.place(relx = 0.1, rely = 0.1, anchor = NW)

    company_name_tb=Entry(company_details_frame,fg=element_color,bg=entry_box_color,font=arial,border=4)
    company_name_tb.place(relx = 0.2, rely = 0.1, anchor = NW)

    #Company Adress
    company_adress_lbl=Label(company_details_frame,text="Company Adress",font=book_antiqua,bg=frame_color,fg=element_color)
    company_adress_lbl.place(relx = 0.1, rely = 0.14, anchor = NW)

    company_adress_tb=Entry(company_details_frame,fg=element_color,bg=entry_box_color,font=arial,border=4)
    company_adress_tb.place(relx = 0.2, rely = 0.14, anchor = NW)

    #Company GSTIN
    company_gstin_lbl=Label(company_details_frame,text="Company GSTIN",font=book_antiqua,bg=frame_color,fg=element_color)
    company_gstin_lbl.place(relx = 0.1, rely = 0.18, anchor = NW)

    company_gstin_tb=Entry(company_details_frame,fg=element_color,bg=entry_box_color,font=arial,border=4)
    company_gstin_tb.place(relx = 0.2, rely = 0.18, anchor = NW)

    #Company Adress
    company_contact_number_lbl=Label(company_details_frame,text="Company Contact",font=book_antiqua,bg=frame_color,fg=element_color)
    company_contact_number_lbl.place(relx = 0.1, rely = 0.22, anchor = NW)

    company_contact_number_tb=Entry(company_details_frame,fg=element_color,bg=entry_box_color,font=arial,border=4)
    company_contact_number_tb.place(relx = 0.2, rely = 0.22, anchor = NW)

    #Edit Button and message
    edit_btn=Button(company_details_frame,fg=element_color,bg=frame_button_color,text="Edit Details",width = 20,border=4,command=lambda:[enable_company__text_box(),add_btn.config(state='normal')])
    edit_btn.place(relx = 0.1, rely = 0.28, anchor = NW)

    #Update Button and message
    add_btn=Button(company_details_frame,fg=element_color,bg=frame_button_color,text="Update Details",width = 20,border=4,command=lambda:[details_updated_obj(),edit_btn.config(state='normal')])
    add_btn.place(relx = 0.205, rely = 0.28, anchor = NW)

    style.configure("TCombobox", fg= element_color, bg= entry_box_color)
    category_tb=ttk.Combobox(company_details_frame,values='',font=arial,width=13)
    category_tb.place(relx = 0.1, rely = 0.4, anchor = NW)

    try:
        con=sqlite3.connect("Database/Store_Data.sql")
        cur=con.cursor()
        cur.execute("SELECT category,tax FROM category_tax_details ORDER BY tax ASC")
        row=cur.fetchall()
        category_list=[]
        for i in row:
            category_list.append(i)
        category_tb.configure(values=category_list)
        con.close()
    except sqlite3.Error as err:
            print("Error - ",err)

    #for combox and autofill
    def callback(*args):
        pos=int(category_tb.current())
        item_no_array=[]
        item_name_array=[]
        for j in category_list:
            item_no_array.append(j[0])
            item_name_array.append(j[1])
        category_tb.delete(0,END)
        gst_tb.delete(0,END)
        category_tb.insert(0,item_no_array[pos])
        gst_tb.insert(0,item_name_array[pos])

    category_tb.bind('<<ComboboxSelected>>', callback)

    #gst
    category=Label(company_details_frame,text="Categories",font=book_antiqua,bg=frame_color,fg=element_color)
    category.place(relx = 0.1, rely = 0.37, anchor = NW)

    gst=Label(company_details_frame,text="GST",font=book_antiqua,bg=frame_color,fg=element_color)
    gst.place(relx = 0.22, rely = 0.37, anchor = NW)

    gst_tb=Entry(company_details_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=12)
    gst_tb.place(relx = 0.22, rely = 0.4, anchor = NW)

    #Update Button Tax
    save_tax=Button(company_details_frame,fg=element_color,bg=frame_button_color,text="Save/Update Tax",width = 20,border=4,height=2,command=lambda:[update_tax_details()])
    save_tax.place(relx = 0.3, rely = 0.385, anchor = NW)

    delete_tax=Button(company_details_frame,fg=element_color,bg=frame_button_color,text="Delete Tax",width = 20,border=4,height=2,command=lambda:[delete_tax_details()])
    delete_tax.place(relx = 0.4, rely = 0.385, anchor = NW)

    def update_tax_details():
        if category_tb.get() =="" or gst_tb.get() =="":
            messagebox.showerror(title='Error', message="Enter All Fields")
        elif any(not ch.isdigit() for ch in gst_tb.get()):
            messagebox.showerror(title='Error', message="GST \ncannot have Letter or special charecter")
        elif any(not ch.isalpha() for ch in category_tb.get()):
            messagebox.showerror(title='Error', message="CATEGORY \ncannot have Number or special charecter")
        else:
            try:
                con=sqlite3.connect("Database/Store_Data.sql")
                cur=con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS category_tax_details(category varchar(20) PRIMARY KEY NOT NULL,tax int(2) NOT NULL)")
                cur.execute("INSERT INTO category_tax_details(category,tax)VALUES('{}',{})".format(category_tb.get(),gst_tb.get()))
                con.commit()
                con.close()
                messagebox.showinfo(title='Sucess', message="Deatils Updated")
                company_details_frame.destroy()
                company_details_obj()
            except sqlite3.Error as err:
                print("Error - ",err)
        
    def delete_tax_details():
        if category_tb.get() =="" or gst_tb.get() =="":
            messagebox.showerror(title='Error', message="Enter All Fields")
        elif any(not ch.isdigit() for ch in gst_tb.get()):
            messagebox.showerror(title='Error', message="GST \ncannot have Letter or special charecter")
        elif any(not ch.isalpha() for ch in category_tb.get()):
            messagebox.showerror(title='Error', message="CATEGORY \ncannot have Number or special charecter")
        else:
            try:
                con=sqlite3.connect("Database/Store_Data.sql")
                cur=con.cursor()
                cur.execute("DELETE FROM category_tax_details WHERE category='{}' AND tax={}".format(category_tb.get(),gst_tb.get()))
                con.commit()
                con.close()
                messagebox.showinfo(title='Sucess', message="{} TAX Deleted".format(category_tb.get()))
                company_details_frame.destroy()
                company_details_obj()
            except sqlite3.Error as err:
                print("Error - ",err)


    def enable_company__text_box():
        company_name_tb.config(state='normal')
        company_adress_tb.config(state='normal')
        company_gstin_tb.config(state='normal')
        company_contact_number_tb.config(state='normal')
        edit_btn.config(state='disabled')
        

    def disable_company__text_box():
        company_name_tb.config(state='disabled')
        company_adress_tb.config(state='disabled')
        company_gstin_tb.config(state='disabled')
        company_contact_number_tb.config(state='disabled')
        add_btn.config(state='disabled')
        edit_btn.config(state='normal')

    def details_updated_obj():
        if company_name_tb.get() =="" or company_adress_tb.get() =="" or company_gstin_tb.get() =="" or company_contact_number_tb.get() =="":
            messagebox.showerror(title='Error', message="Enter All Fields")
        elif any(not ch.isdigit() for ch in company_contact_number_tb.get()):
            messagebox.showerror(title='Error', message="Contact Number \ncannot have Letter or special charecter")
        elif len(company_contact_number_tb.get()) >10:
            messagebox.showerror(title='Error', message="Contact Number Must be\n less than 10 Digits")
        elif len(company_gstin_tb.get()) !=15:
            messagebox.showerror(title='Error', message="GSTIN Number Must be\n 15 Digits")
        else:
            messagebox.showinfo(title='Sucess', message="Details Updated")
            #stores company data in company_details.json file
            company={'company_name':(company_name_tb.get()),'company_address':(company_adress_tb.get()),'company_gstin':(company_gstin_tb.get())
            ,'company_contact':(company_contact_number_tb.get())}
            write_counter('company_details',company)
            disable_company__text_box()
            

    if path.exists("JSON Files/company_details.json"):
        enable_company__text_box()
        current_company_details=read_counter('company_details')
        company_name_tb.insert(0,current_company_details['company_name'])
        company_adress_tb.insert(0,current_company_details['company_address'])
        company_gstin_tb.insert(0,current_company_details['company_gstin'])
        company_contact_number_tb.insert(0,current_company_details['company_contact'])
        disable_company__text_box()
    
    disable_company__text_box()

def purchase_obj():
    company_details_btn.config(state='normal',bg=menu_button_color)
    purchase_btn.config(state='disabled',bg=selection_color)
    dealer_btn.config(state='normal',bg=menu_button_color)
    item_btn.config(state='normal',bg=menu_button_color)
    reports_btn.config(state='normal',bg=menu_button_color)
    billing_btn.config(state='normal',bg=menu_button_color)

    r=read_counter('cleaner')
    delete_previous_frame('purchase_frame',r)
    write_counter('cleaner','purchase_frame')
    global purchase_frame
    purchase_frame= Frame(root,width=1670,height=1060,bg=frame_color)
    purchase_frame.grid(row=0,column=1)
    purchase_frame.propagate(0)

    purchase_details_lbl=Label(purchase_frame,text="Purchased Products",font=book_antiqua_size18,bg=frame_color,fg=element_color)
    purchase_details_lbl.place(relx = 0.4, rely = 0.008, anchor = NW)

    #Dealer name
    dealer_name_lbl=Label(purchase_frame,text="Dealer Name",font=book_antiqua,bg=frame_color,fg=element_color)
    dealer_name_lbl.place(relx = 0.04, rely = 0.075, anchor = NW)

    dealer_name_tb=Entry(purchase_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=20)
    dealer_name_tb.place(relx = 0.105, rely = 0.075, anchor = NW)

    #Dealer Gstin
    dealer_gstin_lbl=Label(purchase_frame,text="GSTIN",font=book_antiqua,bg=frame_color,fg=element_color)
    dealer_gstin_lbl.place(relx = 0.265, rely = 0.075, anchor = NW)

    dealer_gstin_tb=Entry(purchase_frame,fg=element_color,bg=entry_box_color,font=arial,border=4)
    dealer_gstin_tb.place(relx = 0.305, rely = 0.075, anchor = NW)

    #Purchase Date
    purchase_date_lbl=Label(purchase_frame,text="Date",font=book_antiqua,bg=frame_color,fg=element_color)
    purchase_date_lbl.place(relx = 0.37, rely = 0.162, anchor = NW)

    #date
    today = date.today()
    purchase_date= DateEntry(purchase_frame, width= 16,height=0, background= "grey", foreground= "white",bd=4, maxdate=today)
    purchase_date.place(relx = 0.40, rely = 0.162, anchor = NW)

    #dealer Address
    purchase_dealer_address_lbl=Label(purchase_frame,text="Address",font=book_antiqua,bg=frame_color,fg=element_color)
    purchase_dealer_address_lbl.place(relx = 0.06, rely = 0.12, anchor = NW)

    purchase_dealer_address_tb=Text(purchase_frame, width=20, height=3,fg=element_color,bg=entry_box_color,font=arial,border=4)
    purchase_dealer_address_tb.place(relx = 0.105, rely = 0.12, anchor = NW)

    #dealer contact
    purchase_dealer_contact_lbl=Label(purchase_frame,text="Contact",font=book_antiqua,bg=frame_color,fg=element_color)
    purchase_dealer_contact_lbl.place(relx = 0.262, rely = 0.12, anchor = NW)

    purchase_dealer_contact_tb=Entry(purchase_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=20)
    purchase_dealer_contact_tb.place(relx = 0.305, rely = 0.12, anchor = NW)
    
    #Purchase Item Code TextBox
    style.configure("TCombobox", fg= element_color, bg= entry_box_color)
    purchase_item_code_tb=ttk.Combobox(purchase_frame,values='',font=arial,width=13)
    purchase_item_code_tb.place(relx = 0.03, rely = 0.202, anchor = NW)
    
    try:
        con=sqlite3.connect("Database/Store_Data.sql")
        cur=con.cursor()
        cur.execute("SELECT item_id,item_name FROM item_purchase_details ORDER BY item_id ASC")
        row=cur.fetchall()
        item_codes=[]
        for i in row:
            item_codes.append(i)
        purchase_item_code_tb.configure(values=item_codes)
        con.close()
    except sqlite3.Error as err:
            print("Error - ",err)

    #for combox and autofill
    def callback(*args):
        pos=int(purchase_item_code_tb.current())
        item_no_array=[]
        item_name_array=[]
        for j in item_codes:
            item_no_array.append(j[0])
            item_name_array.append(j[1])
        purchase_item_code_tb.delete(0,END)
        purchase_item_name_tb.delete(0,END)
        purchase_item_code_tb.insert(0,item_no_array[pos])
        purchase_item_name_tb.insert(0,item_name_array[pos])
    
    purchase_item_code_tb.bind('<<ComboboxSelected>>', callback)
    
    #Purchase Item Name TextBox
    purchase_item_name_tb=Entry(purchase_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=28)
    purchase_item_name_tb.place(relx = 0.11, rely = 0.198, anchor = NW)

    #Purchase Quantity TextBox
    purchase_quantity_tb=Entry(purchase_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=10)
    purchase_quantity_tb.place(relx = 0.266, rely = 0.198, anchor = NW)

    #Purchase Price
    purchase_price_tb=Entry(purchase_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=10)
    purchase_price_tb.place(relx = 0.325, rely = 0.198, anchor = NW)

    #Purchase Add Button
    purchase_add_update_btn=Button(purchase_frame,fg=element_color,bg=frame_button_color,text="Add",width = 21,border=4,command=lambda:[check_entry_condition()])
    purchase_add_update_btn.place(relx = 0.384, rely = 0.198, anchor = NW)

    #Purchase Delete Button
    purchase_delete_btn=Button(purchase_frame,fg=element_color,bg=frame_button_color,text="Delete",width = 21,border=4,command=lambda:[delete_purchase_item()])
    purchase_delete_btn.place(relx = 0.03, rely = 0.575, anchor = NW)

    #clear all button
    purchase_clearall_btn=Button(purchase_frame,fg=element_color,bg=frame_button_color,text="clear All",width = 21,border=4,command=lambda:[delete_all_purchase_item()])
    purchase_clearall_btn.place(relx = 0.13, rely = 0.575, anchor = NW)
    
    #Purchase Total
    purchase_total_lbl=Label(purchase_frame,text="0000.00",font=book_antiqua_size18,bg=frame_color,fg=element_color)
    purchase_total_lbl.place(relx = 0.41, rely = 0.575, anchor = NW)

    #Purchase save
    purchase_print_button=Button(purchase_frame,fg=element_color,bg=frame_button_color,text="Save",width = 16,height=2,border=4,command=lambda:[save_purchase_data_to_database()])
    purchase_print_button.place(relx = 0.32, rely = 0.575, anchor = NW)


    def check_entry_condition():
        if len(dealer_name_tb.get()) ==0 or len(purchase_dealer_address_tb.get(1.0, END)) ==0 or len(purchase_dealer_contact_tb.get()) ==0 or len(purchase_item_code_tb.get()) ==0 or len(purchase_item_name_tb.get()) ==0 or len(purchase_quantity_tb.get()) ==0 or len(purchase_price_tb.get()) ==0:
            messagebox.showerror(title='Error', message="Enter All Fields)")
        #elif any(ch.isdigit() or not ch.isalnum() for ch in dealer_name_tb.get()):
            #messagebox.showerror(title='Error', message="Dealer Name \ncannot have number or special charecter")
        elif any(not ch.isdigit() for ch in purchase_dealer_contact_tb.get()):
            messagebox.showerror(title='Error', message="Contact Number \ncannot have Letter or special charecter")
        elif len(purchase_dealer_contact_tb.get())!=10:
            messagebox.showerror(title='Error', message="Contact Number \nmust be 10 Digits")
        elif len(dealer_gstin_tb.get())!=15:
            messagebox.showerror(title='Error', message="GSTIN Number \nmust Have 15 Charecters")
        elif any(not ch.isdigit() for ch in purchase_item_code_tb.get()):
            messagebox.showerror(title='Error', message="Item Code \ncannot have Letter or special charecter")
        elif any(ch.isalpha() for ch in purchase_quantity_tb.get()):
            messagebox.showerror(title='Error', message="Quantity \ncannot have Letter or special charecter")
        elif float(purchase_quantity_tb.get())<=0:
            messagebox.showerror(title='Error', message="Invalid Quantity")
        elif any(ch.isalpha() for ch in purchase_price_tb.get()):
            messagebox.showerror(title='Error', message="Price \ncannot have Letter or special charecter")
        elif float(purchase_price_tb.get())<=0:
            messagebox.showerror(title='Error', message="Invalid Price")
        else:
            add_purchase_item()
    
    def add_purchase_item():
        #invoice_number=int(invoice_number_tb.get())
        dealer_name=dealer_name_tb.get()
        dealer_gstin=dealer_gstin_tb.get()
        purchase_dealer_address=purchase_dealer_address_tb.get(1.0, END)
        purchase_dealer_contact=purchase_dealer_contact_tb.get()
        
        global dealer_data
        dealer_data={'dealer_name':dealer_name,'dealer_gstin':dealer_gstin,'purchase_dealer_address':purchase_dealer_address,'purchase_dealer_contact':purchase_dealer_contact}
        
        purchase_item_code=int(purchase_item_code_tb.get())
        date=purchase_date.get_date()
        purchase_item_name=purchase_item_name_tb.get()
        purchase_quantity=float(purchase_quantity_tb.get())
        purchase_price=float(purchase_price_tb.get())
        purchase_total=purchase_quantity*purchase_price
        try:
            con=sqlite3.connect("Database/Store_Data.sql")
            cur=con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS temp_item_purchase_details(item_id int(8) PRIMARY KEY NOT NULL,date date NOT NULL,item_name varchar(25) NOT NULL,purchase_quantity FLOAT NOT NULL,buying_price FLOAT NOT NULL,total_price FLOAT NOT NULL)")

            cur.execute("INSERT INTO temp_item_purchase_details(item_id,date,item_name,purchase_quantity,buying_price,total_price)VALUES({},'{}','{}',{:.2f},{:.2f},{:.2f}) ON CONFLICT (item_id) DO UPDATE SET purchase_quantity=purchase_quantity+{:.2f},buying_price={:.2f},item_name='{}' returning item_id".format(purchase_item_code,date,purchase_item_name,purchase_quantity,purchase_price,float(purchase_total),float(purchase_quantity),float(purchase_price),purchase_item_name))
            id_to_update=cur.fetchall()
            cur.execute("UPDATE temp_item_purchase_details SET total_price=purchase_quantity*buying_price where item_id={}".format(id_to_update[0][0]))


            cur.execute("SELECT item_id,item_name,purchase_quantity,buying_price,total_price FROM temp_item_purchase_details ORDER BY item_id ASC")
            row=cur.fetchall()
            clear_all(purchase_tree_view)
            for i in row:
                purchase_tree_view.insert("", 'end', text ="L1",values =(i[0],i[1],i[2],i[3],i[4]))
            cur.execute("SELECT SUM(total_price) FROM temp_item_purchase_details")
            total=cur.fetchall()
            if len(total)<1:
                purchase_total_lbl.configure(text="0000.00")
            else:
                purchase_total_lbl.configure(text="{:.2f}".format(float(total[0][0])))
            con.commit()
            con.close()
        except sqlite3.Error as err:
            print("Error - ",err)
            error_message=str(err)
            print(error_message[0:24])
            if error_message[0:24]=='UNIQUE constraint failed':
                messagebox.showerror(title='Error', message="Item Code cannot repeat")
            con.close()

    def delete_purchase_item():
        selected_treeview_item=selected_item_from_treeview(purchase_tree_view,'purchase_tree_view')
        temp=messagebox.askquestion('Delete Product', 'Are you sure you want to Delete')
        if temp=='yes':
            try:
                con=sqlite3.connect("Database/Store_Data.sql")
                cur=con.cursor()
                cur.execute("DELETE FROM temp_item_purchase_details where item_id={}".format(selected_treeview_item))
                cur.execute("SELECT item_id,item_name,purchase_quantity,buying_price,total_price FROM temp_item_purchase_details ORDER BY item_id ASC")
                row=cur.fetchall()
                clear_all(purchase_tree_view)
                for i in row:
                    purchase_tree_view.insert("", 'end', text ="L1",values =(i[0],i[1],i[2],i[3],i[4]))
                cur.execute("SELECT SUM(total_price) FROM temp_item_purchase_details")
                total=cur.fetchall()
                print(len(total))
                print(total)
                if str(total[0][0])=='None':
                    purchase_total_lbl.configure(text="0000.00")
                else:
                    purchase_total_lbl.configure(text="{:.2f}".format(float(total[0][0])))
                con.commit()
                con.close()
            except sqlite3.Error as err:
                print("Error - ",err)

    def delete_all_purchase_item():
        temp=messagebox.askquestion('Delete Product', 'Are you sure you want to Clear All')
        if temp=='yes':
            clear_all(purchase_tree_view)
            try:
                con=sqlite3.connect("Database/Store_Data.sql")
                cur=con.cursor()
                cur.execute("drop table temp_item_purchase_details")
                cur.execute("CREATE TABLE IF NOT EXISTS temp_item_purchase_details(item_id int(8) PRIMARY KEY NOT NULL,date date NOT NULL,item_name varchar(25) NOT NULL,purchase_quantity FLOAT NOT NULL,buying_price FLOAT NOT NULL,total_price FLOAT NOT NULL)")
                purchase_total_lbl.configure(text="0000.00")
                con.commit()
                con.close()
            except sqlite3.Error as err:
                print("Error - ",err)

    def save_purchase_data_to_database():
            try:
                con=sqlite3.connect("Database/Store_Data.sql")
                cur=con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS dealer_purchase_details(dealer_name varchar(20) NOT NULL,dealer_gstin varchar(20),dealer_address varchar(30) NOT NULL,dealer_contact int(12) NOT NULL)")
                cur.execute("CREATE TABLE IF NOT EXISTS item_purchase_details(item_id int(8) PRIMARY KEY NOT NULL,date date NOT NULL,item_name varchar(25) NOT NULL,purchase_quantity REAL NOT NULL,buying_price REAL NOT NULL,total_price REAL NOT NULL,selling_price REAL,item_category varchar(20))")
                cur.execute("SELECT * from temp_item_purchase_details")
                row=cur.fetchall()
                for i in row:
                    cur.execute("INSERT INTO item_purchase_details(item_id,date,item_name,purchase_quantity,buying_price,total_price)VALUES({},'{}','{}',{:.2f},{:.2f},{:.2f}) ON CONFLICT (item_id) DO UPDATE SET purchase_quantity=purchase_quantity+{:.2f},buying_price={:.2f} returning item_id".format(i[0],i[1],i[2],i[3],i[4],i[5],i[3],i[4]))
                    id_to_update=cur.fetchall()
                    cur.execute("UPDATE item_purchase_details SET total_price=purchase_quantity*buying_price where item_id={}".format(id_to_update[0][0]))
                
                cur.execute("INSERT OR REPLACE INTO dealer_purchase_details(dealer_name,dealer_gstin,dealer_address,dealer_contact)VALUES('{}','{}','{}',{})".format(dealer_data['dealer_name'],dealer_data['dealer_gstin'],dealer_data['purchase_dealer_address'],dealer_data['purchase_dealer_contact']))
                messagebox.showinfo(title='Saved', message="Products Added to inventory")
                con.commit()
                con.close()
                delete_all_purchase_item()
            except sqlite3.Error as err:
                print("Error - ",err)
                messagebox.showerror(title='Error', message="No Data to Save")

    #treeview element
    purchase_tree_view= Treeview(purchase_frame,selectmode='browse',height=17)
    purchase_tree_view.place(relx = 0.03, rely = 0.225, anchor = NW)

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
    purchase_tree_view.heading("1",text="Item Id")
    purchase_tree_view.heading("2",text="Item Name")
    purchase_tree_view.heading("3",text="Quantity")
    purchase_tree_view.heading("4",text="Price")
    purchase_tree_view.heading("5",text="Total")

    con=sqlite3.connect("Database/Store_Data.sql")
    cur=con.cursor()
    cur.execute("drop table temp_item_purchase_details")
    cur.execute("CREATE TABLE IF NOT EXISTS temp_item_purchase_details(item_id int(8) PRIMARY KEY NOT NULL,date date NOT NULL,item_name varchar(25) NOT NULL,purchase_quantity FLOAT NOT NULL,buying_price FLOAT NOT NULL,total_price FLOAT NOT NULL)")
    con.commit()
    con.close()

def dealer_obj():
    company_details_btn.config(state='normal',bg=menu_button_color)
    purchase_btn.config(state='normal',bg=menu_button_color)
    dealer_btn.config(state='disabled',bg=selection_color)
    item_btn.config(state='normal',bg=menu_button_color)
    reports_btn.config(state='normal',bg=menu_button_color)
    billing_btn.config(state='normal',bg=menu_button_color)

    r=read_counter('cleaner')
    delete_previous_frame('dealer_frame',r)
    write_counter('cleaner','dealer_frame')
    global dealer_frame
    dealer_frame= Frame(root,width=1670,height=1060,bg=frame_color)
    dealer_frame.grid(row=0,column=1)
    dealer_frame.propagate(0)

    dealer_lbl=Label(dealer_frame,text="Dealer Details",font=book_antiqua_size18,bg=frame_color,fg=element_color)
    dealer_lbl.place(relx = 0.4, rely = 0.008, anchor = NW)

    #dealer Name
    dealer_name_lbl=Label(dealer_frame,text="Dealer Name",font=book_antiqua,bg=frame_color,fg=element_color)
    dealer_name_lbl.place(relx = 0.04, rely = 0.075, anchor = NW)

    dealer_name_tb=Entry(dealer_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=20)
    dealer_name_tb.place(relx = 0.105, rely = 0.075, anchor = NW)

    '''#dealer search button
    dealer_search_btn=Button(dealer_frame,fg=element_color,bg=frame_button_color,text="Search",width = 15,border=4,command=lambda:[])
    dealer_search_btn.place(relx = 0.25, rely = 0.075, anchor = NW)'''

    #item treeview element
    global dealer_tree_view
    dealer_tree_view= Treeview(dealer_frame,selectmode='browse',height=17)
    dealer_tree_view.place(relx = 0.04, rely = 0.175, anchor = NW)

    products={}
    def Scankey(event):
        #val stores the selected value
        val = event.widget.get()
        if len(val)==1 or len(val)==0:
            clear_all(dealer_tree_view)
            dealer_info()
        else:
            name_data = {}
            for key,value in products.items():
                if val.lower() in key.lower():
                    name_data[key]=value
                    Update(name_data)

    #updates into treeview
    def Update(data):
        for item in dealer_tree_view.get_children():
            dealer_tree_view.delete(item)
        for key, value in data.items():
            dealer_tree_view.insert("",'end',text="L1",values=(key, value[1],value[2],value[3]))

    def dealer_info():
        try:
            con=sqlite3.connect("Database/Store_Data.sql")
            cur=con.cursor()
            
            cur.execute("SELECT dealer_name,dealer_contact,dealer_address,dealer_gstin from dealer_purchase_details ORDER BY dealer_name ASC")
            row=cur.fetchall()
            for i in row:
                products[i[0]]=[i[2],i[1],i[2],i[3]]
                dealer_tree_view.insert("", 'end', text ="L1", values=(i[0],i[1],i[2],i[3]))
            con.close()
        except sqlite3.Error as err:
            print("Error - ",err)
    
    def delete_dealer_info():
        curItem = dealer_tree_view.focus()
        dealer_tree_view.item(curItem)
        selected_items =dealer_tree_view.item(curItem)
        for key, value in selected_items.items():
            if key == 'values':
                selected_treeview_item1=value[1]
        try:
            con=sqlite3.connect("Database/Store_Data.sql")
            cur=con.cursor()
            cur.execute("DELETE FROM dealer_purchase_details where dealer_contact='{}'".format(selected_treeview_item1))
            con.commit()
            cur.execute("SELECT dealer_name,dealer_contact,dealer_address,dealer_gstin from dealer_purchase_details ORDER BY dealer_name ASC")
            row=cur.fetchall()
            clear_all(dealer_tree_view)
            for i in row:
                dealer_tree_view.insert("", 'end', text ="L1",values =(i[0],i[1],i[2],i[3]))
            con.commit()
            con.close()
        except sqlite3.Error as err:
            print("Error - ",err)
    

    #verticle scrollbar
    #vertical_scrollbar=Scrollbar(billing_frame,orient="vertical",command=tree_view.yview)
    #vertical_scrollbar.place(relx = 0.03, rely = 0.3, anchor = NW)
    #tree_view.configure(xscrollcommand=vertical_scrollbar.set)

    #Definning number of columns
    dealer_tree_view["columns"]=("1","2","3","4")

    #defining heading
    dealer_tree_view["show"]='headings'

    #modifying the size of the columns
    dealer_tree_view.column("1",width=210)
    dealer_tree_view.column("2",width=110)
    dealer_tree_view.column("3",width=260)
    dealer_tree_view.column("4",width=110)

    #assigning heading name
    dealer_tree_view.heading("1",text="Name")
    dealer_tree_view.heading("2",text="Contact")
    dealer_tree_view.heading("3",text="Address")
    dealer_tree_view.heading("4",text="GSTIN No")

    #dealer refresh btn
    dealer_delete_btn=Button(dealer_frame,fg=element_color,bg=frame_button_color,text="Delete",width = 15,border=4,command=lambda:[delete_dealer_info()])
    dealer_delete_btn.place(relx = 0.04, rely = 0.524, anchor = NW)

    #dealer Edit btn
    dealer_edit_btn=Button(dealer_frame,fg=element_color,bg=frame_button_color,text="Edit",width = 15,border=4,command=lambda:[edit_dealer_info()])
    dealer_edit_btn.place(relx = 0.12, rely = 0.524, anchor = NW)

    #Show details btn
    dealer_show_details_btn=Button(dealer_frame,fg=element_color,bg=frame_button_color,text="Refresh",width = 16,border=4,command=lambda:[])
    dealer_show_details_btn.place(relx = 0.38, rely = 0.524, anchor = NW)

    dealer_info()
    dealer_name_tb.bind('<Key>', Scankey)

    def edit_dealer_info():
        curItem = dealer_tree_view.focus()
        dealer_tree_view.item(curItem)
        selected_items =dealer_tree_view.item(curItem)
        for key, value in selected_items.items():
            if key == 'values':
                dealer_name=value[0]
                dealer_contact=value[1]
                dealer_address=value[2]
                dealer_gstin=value[3]
        openeditwindow()
        edit_frame= Frame(editwindow,bg="#161719",width=500,height=500)
        edit_frame.grid(row=0,column=0)

        dealer_name_lbl=Label(edit_frame,text="Dealer Name",font=book_antiqua,bg=frame_color,fg=element_color,width=15)
        dealer_name_lbl.grid(row=0,column=0)
        dealer_name_tb=Entry(edit_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=20)
        dealer_name_tb.insert(0,dealer_name)
        dealer_name_tb.grid(row=0,column=1)

        dealer_contact_lbl=Label(edit_frame,text="Dealer Contact",font=book_antiqua,bg=frame_color,fg=element_color)
        dealer_contact_lbl.grid(row=1,column=0)
        dealer_contact_tb=Entry(edit_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=20)
        dealer_contact_tb.insert(0,dealer_contact)
        dealer_contact_tb.grid(row=1,column=1)

        dealer_address_lbl=Label(edit_frame,text="Dealer Address",font=book_antiqua,bg=frame_color,fg=element_color)
        dealer_address_lbl.grid(row=2,column=0)
        dealer_address_tb=Entry(edit_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=20)
        dealer_address_tb.insert(0,dealer_address)
        dealer_address_tb.grid(row=2,column=1)

        dealer_gstin_lbl=Label(edit_frame,text="Dealer Gstin",font=book_antiqua,bg=frame_color,fg=element_color)
        dealer_gstin_lbl.grid(row=3,column=0)
        dealer_gstin_tb=Entry(edit_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=20)
        dealer_gstin_tb.insert(0,dealer_gstin)
        dealer_gstin_tb.grid(row=3,column=1)

        #Save Button
        dealer_save_btn=Button(edit_frame,fg=element_color,bg=frame_button_color,text="Save",width = 16,border=4,command=lambda:[edited_item()])
        dealer_save_btn.grid(row=4,column=1)
        
        def disable_event():
            pass
        editwindow.protocol("WM_DELETE_WINDOW", disable_event)

        def edited_item():
            if any(not ch.isdigit() for ch in dealer_contact_tb.get()):
                messagebox.showerror(title='Error', message="Contact Number \ncannot have Letter or special charecter")
            elif len(dealer_contact_tb.get())!=10:
                messagebox.showerror(title='Error', message="Contact Number \nmust be 10 Digits")
            elif len(dealer_gstin_tb.get())!=15:
                messagebox.showerror(title='Error', message="GSTIN Number \nmust Have 15 Charecters")
            else:
                try:
                    con=sqlite3.connect("Database/Store_Data.sql")
                    cur=con.cursor()
                    cur.execute("DELETE from dealer_purchase_details where dealer_name='{}' and dealer_gstin='{}'".format(dealer_name,dealer_gstin))
                    con.commit()
                    cur.execute("INSERT INTO dealer_purchase_details(dealer_name,dealer_gstin,dealer_address,dealer_contact)VALUES('{}','{}','{}',{})".format(dealer_name_tb.get(),dealer_gstin_tb.get(),dealer_address_tb.get(),int(dealer_contact_tb.get())))
                    con.commit()
                    con.close()
                    editwindow.destroy()
                except sqlite3.Error as err:
                    print("Error - ",err)
                dealer_frame.destroy()
                dealer_obj()

def item_obj():
    company_details_btn.config(state='normal',bg=menu_button_color)
    purchase_btn.config(state='normal',bg=menu_button_color)
    dealer_btn.config(state='normal',bg=menu_button_color)
    item_btn.config(state='disabled',bg=selection_color)
    reports_btn.config(state='normal',bg=menu_button_color)
    billing_btn.config(state='normal',bg=menu_button_color)

    r=read_counter('cleaner')
    delete_previous_frame('item_frame',r)
    write_counter('cleaner','item_frame')
    global item_frame
    item_frame= Frame(root,width=1670,height=1060,bg=frame_color)
    item_frame.grid(row=0,column=1)
    item_frame.propagate(0)

    item_id_tb=Entry(item_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=11)

    #Item Name TextBox
    item_name_tb=Entry(item_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=21)

    #Quantity TextBox
    item_quantity_tb=Entry(item_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=12)

    #Category
    style.configure("TCombobox", fg= element_color, bg= entry_box_color)
    item_category_tb=ttk.Combobox(item_frame,values='',font=arial,width=12,state="readonly")

    #Price
    item_price_tb=Entry(item_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=12)

    #Selling Price
    selling_price_tb=Entry(item_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=12)

    def edit_item_placement():
        item_id_tb.place(relx = 0.03, rely = 0.12, anchor = NW)
        item_name_tb.place(relx = 0.0925, rely = 0.12, anchor = NW)
        item_quantity_tb.place(relx = 0.209, rely = 0.12, anchor = NW)
        item_category_tb.place(relx = 0.278, rely = 0.123, anchor = NW)
        try:
            con=sqlite3.connect("Database/Store_Data.sql")
            cur=con.cursor()
            cur.execute("SELECT category FROM category_tax_details ORDER BY category ASC")
            row=cur.fetchall()
            category_list=[]
            for i in row:
                category_list.append(i)
            item_category_tb.configure(values=category_list)
            con.close()
        except sqlite3.Error as err:
            print("Error - ",err)

        #for combox and autofill
        def callback(*args):
            pos=int(item_category_tb.current())
            item_no_array=[]
            item_name_array=[]
            for j in category_list:
                item_no_array.append(j[0])
                item_name_array.append(j[1])
            item_category_tb.delete(0,END)
            item_category_tb.insert(0,item_no_array[pos])
        
        item_category_tb.bind('<<ComboboxSelected>>', callback)

        item_price_tb.place(relx = 0.355, rely = 0.12, anchor = NW)
        selling_price_tb.place(relx = 0.42, rely = 0.12, anchor = NW)


    #Filter by name
    item_search_lbl=Label(item_frame,text="Search",font=book_antiqua,bg=frame_color,fg=element_color)
    item_search_lbl.place(relx = 0.04, rely = 0.07, anchor = NW)

    item_search_tb=Entry(item_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=20)
    item_search_tb.place(relx = 0.095, rely = 0.07, anchor = NW)

    item_lbl=Label(item_frame,text="Search\Edit Items",font=book_antiqua_size18,bg=frame_color,fg=element_color)
    item_lbl.place(relx = 0.4, rely = 0.008, anchor = NW)

    #item refresh btn
    item_delete_btn=Button(item_frame,fg=element_color,bg=frame_button_color,text="Delete",width = 15,border=4,command=lambda:[delete_item_info()])
    item_delete_btn.place(relx = 0.03, rely = 0.496, anchor = NW)

    #item Edit btn
    item_edit_btn=Button(item_frame,fg=element_color,bg=frame_button_color,text="Edit",width = 15,border=4,command=lambda:[edit_item_info()])
    item_edit_btn.place(relx = 0.11, rely = 0.496, anchor = NW)

    #item Save btn
    item_refresh_btn=Button(item_frame,fg=element_color,bg=frame_button_color,text="Refresh",width = 15,border=4,command=lambda:[])
    item_refresh_btn.place(relx = 0.422, rely = 0.496, anchor = NW)

    #item treeview element
    item_tree_view= Treeview(item_frame,selectmode='browse',height=17)
    item_tree_view.place(relx = 0.03, rely = 0.148, anchor = NW)

    #verticle scrollbar
    #vertical_scrollbar=Scrollbar(billing_frame,orient="vertical",command=tree_view.yview)
    #vertical_scrollbar.place(relx = 0.03, rely = 0.3, anchor = NW)
    #tree_view.configure(xscrollcommand=vertical_scrollbar.set)

    #Definning number of columns
    item_tree_view["columns"]=("1","2","3","4","5","6")

    #defining heading
    item_tree_view["show"]='headings'

    #modifying the size of the columns
    item_tree_view.column("1",width=100)
    item_tree_view.column("2",width=200)
    item_tree_view.column("3",width=110)
    item_tree_view.column("4",width=130)
    item_tree_view.column("5",width=114)
    item_tree_view.column("6",width=114)

    #assigning heading name
    item_tree_view.heading("1",text="Id")
    item_tree_view.heading("2",text="Item Name")
    item_tree_view.heading("3",text="Stock")
    item_tree_view.heading("4",text="Category")
    item_tree_view.heading("5",text="Price")
    item_tree_view.heading("6",text="Selling Price")

    item={}
    def Scankey2(event):
        #val stores the selected value
        val = event.widget.get()
        if len(val)==1 or len(val)==0:
            clear_all(item_tree_view)
            item_info()
        else:
            name_data = {}
            for key,value in item.items():
                print(item)
                if val.lower() in key.lower():
                    name_data[key]=value
                    Update2(name_data)

    #updates into treeview
    def Update2(data):
        for item in item_tree_view.get_children():
            item_tree_view.delete(item)
        for key, value in data.items():
            item_tree_view.insert("",'end',text="L1",values=(value[0], key,value[1],value[2],value[3],value[4]))
    
    def item_info():
        try:
            con=sqlite3.connect("Database/Store_Data.sql")
            cur=con.cursor()
            cur.execute("SELECT item_id,item_name,purchase_quantity,item_category,buying_price,selling_price from item_purchase_details ORDER BY item_id ASC")
            row=cur.fetchall()
            print(row)
            for i in row:
                item[i[1]]=[i[0],i[2],i[3],i[4],i[5]]
                item_tree_view.insert("", 'end', text ="L1", values=(i[0],i[1],i[2],i[3],i[4],i[5]))
            con.close()
        except sqlite3.Error as err:
            print("Error - ",err)
    item_info()
    item_search_tb.bind('<Key>', Scankey2)

    def delete_item_info():
        selected_treeview_item=selected_item_from_treeview(item_tree_view,'item_tree_view')
        print(selected_treeview_item)
        try:
            con=sqlite3.connect("Database/Store_Data.sql")
            cur=con.cursor()
            cur.execute("DELETE FROM item_purchase_details where item_id={}".format(selected_treeview_item))
            con.commit()
            cur.execute("SELECT item_id,item_name,purchase_quantity,item_category,buying_price,selling_price from item_purchase_details ORDER BY item_id ASC")
            row=cur.fetchall()
            clear_all(item_tree_view)
            for i in row:
                item_tree_view.insert("", 'end', text ="L1",values =(i[0],i[1],i[2],i[3],i[4],i[5]))
            con.commit()
            con.close()
        except sqlite3.Error as err:
            print("Error - ",err)
    
    def clear_all_tb(event):
        item_id_tb.delete(0,END)
        item_name_tb.delete(0,END)
        item_quantity_tb.delete(0,END)
        item_category_tb.delete(0,END)
        item_price_tb.delete(0,END)
        selling_price_tb.delete(0,END)

    def edit_item_info():
        curItem = item_tree_view.focus()
        item_tree_view.item(curItem)
        selected_items =item_tree_view.item(curItem)
        for key, value in selected_items.items():
            if key == 'values':
                item_id=value[0]
                item_name=value[1]
                item_stock=value[2]
                item_category=value[3]
                item_price=value[4]
                item_selling_price=value[5]
            print(value)
        item_tree_view.configure(selectmode='none')

        edit_item_placement()
        item_id_tb.insert(0,item_id)
        item_name_tb.insert(0,item_name)
        item_quantity_tb.insert(0,item_stock)
        item_category_tb.configure(state='normal')
        item_category_tb.insert(0,item_category)
        item_category_tb.configure(state='readonly')
        item_price_tb.insert(0,item_price)
        selling_price_tb.insert(0,item_selling_price)

        item_id_tb.bind('<Button-1>',clear_all_tb)
        
        #Update Button
        item_update_btn=Button(item_frame,fg=element_color,bg=frame_button_color,text="Update",width = 16,height=2,border=4,command=lambda:[item_update()])
        item_update_btn.place(relx = 0.492, rely = 0.118, anchor = NW)

        def item_update():
            if any(not ch.isdigit() for ch in item_id_tb.get()):
                messagebox.showerror(title='Error', message="Item Id \ncannot have Letter or special charecter")
            elif int(item_id_tb.get())<1:
                messagebox.showerror(title='Error', message="Item Id \ncannot be less than 0")

            elif any(ch.isalpha() for ch in item_quantity_tb.get()):
                messagebox.showerror(title='Error', message="Item Stock \ncannot have Letter")
            elif float(item_quantity_tb.get())<0:
                messagebox.showerror(title='Error', message="Item Stock \ncannot be less than 0")

            elif any(ch.isalpha() for ch in item_price_tb.get()):
                messagebox.showerror(title='Error', message="Item Price \ncannot have Letter")
            elif float(item_price_tb.get())<0:
                messagebox.showerror(title='Error', message="Item Price \ncannot be less than 0")

            elif any(ch.isalpha() for ch in selling_price_tb.get()):
                messagebox.showerror(title='Error', message="Selling Price \ncannot have Letter")
            elif float(selling_price_tb.get())<float(item_price_tb.get()):
                messagebox.showerror(title='Error', message="Selling Price \ncannot be less than Buying price")
            else:
                try:
                    con=sqlite3.connect("Database/Store_Data.sql")
                    cur=con.cursor()
                    total_of_edited_item=float(item_price_tb.get())*float(item_quantity_tb.get())
                    cur.execute("INSERT OR REPLACE INTO item_purchase_details(item_id,date,item_name,purchase_quantity,buying_price,item_category,selling_price,total_price)VALUES({},'{}','{}',{},{},'{}',{},{})".format(int(item_id_tb.get()),datesorted,item_name_tb.get(),float(item_quantity_tb.get()),float(item_price_tb.get()),item_category_tb.get(),float(selling_price_tb.get()),float(total_of_edited_item)))
                    con.commit()
                    con.close()
                except sqlite3.Error as err:
                    print("Error - ",err)
                item_frame.destroy()
                item_obj()


def report_obj():
    company_details_btn.config(state='normal',bg=menu_button_color)
    purchase_btn.config(state='normal',bg=menu_button_color)
    dealer_btn.config(state='normal',bg=menu_button_color)
    item_btn.config(state='normal',bg=menu_button_color)
    reports_btn.config(state='disabled',bg=selection_color)
    billing_btn.config(state='normal',bg=menu_button_color)

    r=read_counter('cleaner')
    delete_previous_frame('report_frame',r)
    write_counter('cleaner','report_frame')
    global report_frame
    report_frame= Frame(root,width=1670,height=1060,bg=frame_color)
    report_frame.grid(row=0,column=1)
    report_frame.propagate(0)

    report_lbl=Label(report_frame,text="Report",font=book_antiqua_size18,bg=frame_color,fg=element_color)
    report_lbl.place(relx = 0.4, rely = 0.065, anchor = NW)

    #Filter
    report_filter_lbl=Label(report_frame,text="Search",font=book_antiqua,bg=frame_color,fg=element_color)
    report_filter_lbl.place(relx = 0.04, rely = 0.15, anchor = NW)

    report_filter_tb=Entry(report_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=15)
    report_filter_tb.place(relx = 0.07, rely = 0.15, anchor = NW)

    #from date
    report_date_lbl=Label(report_frame,text="From",font=book_antiqua,bg=frame_color,fg=element_color)
    report_date_lbl.place(relx = 0.04, rely = 0.19, anchor = NW)
    
    today = date.today()
    report_from_date_tb = DateEntry(report_frame, width= 16,height=0, background= "grey", foreground= "white",bd=4, maxdate=today)
    report_from_date_tb.place(relx = 0.07, rely = 0.19, anchor = NW)

    #to date
    report_date_lbl=Label(report_frame,text="To",font=book_antiqua,bg=frame_color,fg=element_color)
    report_date_lbl.place(relx = 0.16, rely = 0.19, anchor = NW)
    
    report_to_date_tb = DateEntry(report_frame, width= 16,height=0, background= "grey", foreground= "white",bd=4, maxdate=today)
    report_to_date_tb.place(relx = 0.177, rely = 0.19, anchor = NW)

    #Search btn
    report_filter_btn=Button(report_frame,fg=element_color,bg=frame_button_color,text="Filter",width = 16,border=4,command=lambda:[report_filter()])
    report_filter_btn.place(relx = 0.27, rely = 0.19, anchor = NW)
    
    #Show details btn
    report_show_details_btn=Button(report_frame,fg=element_color,bg=frame_button_color,text="Show Details",width = 16,border=4,command=lambda:[])
    report_show_details_btn.place(relx = 0.365, rely = 0.19, anchor = NW)

    #treeview element
    report_tree_view= Treeview(report_frame,selectmode='browse',height=17)
    report_tree_view.place(relx = 0.03, rely = 0.23, anchor = NW)

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

    reports_tv={}
    def Scankey3(event):
        #val stores the selected value
        val = event.widget.get()
        if len(val)==1 or len(val)==0:
            clear_all(report_tree_view)
            report_info()
        else:
            name_data = {}
            for key,value in reports_tv.items():
                if val.lower() in key.lower():
                    name_data[key]=value
                    Update3(name_data)

    #updates into treeview
    def Update3(data):
        for reports_tv in report_tree_view.get_children():
            report_tree_view.delete(reports_tv)
        for key, value in data.items():
            report_tree_view.insert("",'end',text="L1",values=(value[0],value[1], key,value[2],value[3]))

    def report_info():
        try:
            con=sqlite3.connect("Database/Store_Data.sql")
            cur=con.cursor()
            cur.execute("SELECT bill_number,bill_date,customer_name,mobile_number,amount FROM customer_details ORDER BY bill_date ASC")
            report=cur.fetchall()
            for i in report:
                report_tree_view.insert("", 'end', text ="L1",values =(i[0],i[1],i[2],i[3],i[4]))
                reports_tv[i[2]]=[i[0],i[1],i[3],i[4]]
            con.close()
        except sqlite3.Error as err:
            print("Error - ",err)
    
    def report_filter():
        clear_all(report_tree_view)
        try:
            con=sqlite3.connect("Database/Store_Data.sql")
            cur=con.cursor()
            from_date=report_from_date_tb.get_date().strftime("%d-%m-%Y")
            to_date=report_to_date_tb.get_date().strftime("%d-%m-%Y")
            cur.execute("SELECT bill_number,bill_date,customer_name,mobile_number,amount FROM customer_details WHERE bill_date BETWEEN '{}' and '{}' ORDER BY bill_date".format(from_date,to_date))
            report=cur.fetchall()
            for i in report:
                report_tree_view.insert("", 'end', text ="L1",values =(i[0],i[1],i[2],i[3],i[4]))
            con.close()
        except sqlite3.Error as err:
            print("Error - ",err)


    report_info()
    report_filter_tb.bind('<Key>', Scankey3)

def billing_obj():
    company_details_btn.config(state='normal',bg=menu_button_color)
    purchase_btn.config(state='normal',bg=menu_button_color)
    dealer_btn.config(state='normal',bg=menu_button_color)
    item_btn.config(state='normal',bg=menu_button_color)
    reports_btn.config(state='normal',bg=menu_button_color)
    billing_btn.config(state='disabled',bg=selection_color)

    r=read_counter('cleaner')
    delete_previous_frame('billing_frame',r)
    write_counter('cleaner','billing_frame')
    global billing_frame
    billing_frame=Frame(root,width=1670,height=1060,bg=frame_color)
    billing_frame.grid(row=0,column=1)
    billing_frame.propagate(0)

    billing_lbl=Label(billing_frame,text="Billing",font=book_antiqua_size18,bg=frame_color,fg=element_color)
    billing_lbl.place(relx = 0.4, rely = 0.008, anchor = NW)
    
    #Customer Name
    billing_customer_name_lbl=Label(billing_frame,text="Customer Name",font=book_antiqua,bg=frame_color,fg=element_color)
    billing_customer_name_lbl.place(relx = 0.04, rely = 0.075, anchor = NW)

    billing_customer_name_tb=Entry(billing_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=20)
    billing_customer_name_tb.place(relx = 0.115, rely = 0.075, anchor = NW)

    #Customer Mobile NUmber
    billing_mobile_lbl=Label(billing_frame,text="Mobile",font=book_antiqua,bg=frame_color,fg=element_color)
    billing_mobile_lbl.place(relx = 0.24, rely = 0.075, anchor = NW)

    billing_mobile_tb=Entry(billing_frame,font=arial,fg=element_color,bg=entry_box_color,border=4,width=17)
    billing_mobile_tb.place(relx = 0.275, rely = 0.075, anchor = NW)

    #Bill Number
    billing_bill_number_lbl=Label(billing_frame,text="Bill Number",font=book_antiqua,bg=frame_color,fg=element_color)
    billing_bill_number_lbl.place(relx = 0.385, rely = 0.075, anchor = NW)

    billing_bill_number_tb=Entry(billing_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=10)
    billing_bill_number_tb.place(relx = 0.44, rely = 0.075, anchor = NW)

    #billed date
    today = date.today()
    billing_billed_date = DateEntry(billing_frame, width= 16,height=0, background= "grey", foreground= "white",bd=4, maxdate=today)
    billing_billed_date.place(relx = 0.515, rely = 0.077, anchor = NW)

    #Item Code TextBox
    billing_item_code_tb=Entry(billing_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=10,state='disabled')
    billing_item_code_tb.place(relx = 0.03, rely = 0.15, anchor = NW)

    #Item Name TextBox
    style.configure("TCombobox", fg= element_color, bg= entry_box_color)
    billing_item_name_tb=ttk.Combobox(billing_frame,values='',font=arial,width=20,state='readonly')
    billing_item_name_tb.place(relx = 0.0925, rely = 0.1535, anchor = NW)

    #category cb
    billing_category_tb=Entry(billing_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=14,state='disabled')
    billing_category_tb.place(relx = 0.214, rely = 0.15, anchor = NW)

    #item Price
    billing_price_tb=Entry(billing_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=9,state='disabled')
    billing_price_tb.place(relx = 0.344, rely = 0.15, anchor = NW)

    #item TAX
    billing_tax_tb=Entry(billing_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=8,state='disabled')
    billing_tax_tb.place(relx = 0.396, rely = 0.15, anchor = NW)
    
    try:
        con=sqlite3.connect("Database/Store_Data.sql")
        cur=con.cursor()
        cur.execute("SELECT item_id,item_name FROM item_purchase_details ORDER BY item_id ASC")
        row=cur.fetchall()
        item_codes=[]
        for i in row:
            item_codes.append(i)
        billing_item_name_tb.configure(values=item_codes)
        con.commit()
        con.close()
    except sqlite3.Error as err:
            print("Error - ",err)

    #for combox and autofill
    def callback(*args):
        pos=int(billing_item_name_tb.current())
        item_no_array=[]
        item_name_array=[]
        for j in item_codes:
            item_no_array.append(j[0])
            item_name_array.append(j[1])

        try:
            con=sqlite3.connect("Database/Store_Data.sql")
            cur=con.cursor()
            cur.execute("SELECT item_category,selling_price FROM item_purchase_details where item_id={}".format(item_no_array[pos]))
            row=cur.fetchall()
            if (row[0][0] is None) or (row[0][1] is None):
                messagebox.showerror(title='Error', message="Category Not Set\n Set the Category First")
                billing_item_code_tb.configure(state='normal')
                billing_item_name_tb.configure(state='normal')
                billing_category_tb.configure(state='normal')
                billing_price_tb.configure(state='normal')
                billing_tax_tb.configure(state='normal')
                billing_price_tb.delete(0,END)
                billing_item_name_tb.delete(0,END)
                billing_category_tb.delete(0,END)
                billing_item_code_tb.delete(0,END)
                billing_tax_tb.delete(0,END)
                billing_price_tb.configure(state='disabled')
                billing_item_code_tb.configure(state='disabled')
                billing_item_name_tb.configure(state='disabled')
                billing_category_tb.configure(state='disabled')
                billing_tax_tb.configure(state='disabled')
            else:
                cur.execute("SELECT tax FROM category_tax_details where category='{}'".format(row[0][0]))
                tax=cur.fetchall()
                billing_item_code_tb.configure(state='normal')
                billing_item_name_tb.configure(state='normal')
                billing_category_tb.configure(state='normal')
                billing_price_tb.configure(state='normal')
                billing_tax_tb.configure(state='normal')
                billing_price_tb.delete(0,END)
                billing_item_code_tb.delete(0,END)
                billing_item_name_tb.delete(0,END)
                billing_category_tb.delete(0,END)
                billing_tax_tb.delete(0,END)
                billing_item_code_tb.insert(0,item_no_array[pos])
                billing_item_name_tb.insert(0,item_name_array[pos])
                billing_category_tb.insert(0,row[0][0])
                billing_price_tb.insert(0,row[0][1])
                billing_tax_tb.insert(0,tax[0][0])
                billing_item_code_tb.configure(state='disabled')
                billing_item_name_tb.configure(state='readonly')
                billing_category_tb.configure(state='disabled')
                billing_price_tb.configure(state='disabled')
                billing_tax_tb.configure(state='disabled')
            con.close()
        except sqlite3.Error as err:
            print("Error - ",err)
    
    billing_item_name_tb.bind('<<ComboboxSelected>>', callback)

    #Quantity TextBox
    billing_quantity_tb=Entry(billing_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=8)
    billing_quantity_tb.place(relx = 0.294, rely = 0.15, anchor = NW)

    #Discount TextBox
    billing_discount_tb=Entry(billing_frame,fg=element_color,bg=entry_box_color,font=arial,border=4,width=10)
    billing_discount_tb.place(relx = 0.444, rely = 0.15, anchor = NW)
    
    #Add Button
    billing_add_update_btn=Button(billing_frame,fg=element_color,bg=frame_button_color,text="Add",width = 16,border=4,command=lambda:[check_entry_condition()])
    billing_add_update_btn.place(relx = 0.503, rely = 0.15, anchor = NW)

    #treeview element
    billing_tree_view= Treeview(billing_frame,selectmode='browse',height=17)
    billing_tree_view.place(relx = 0.03, rely = 0.18, anchor = NW)

    #verticle scrollbar
    #vertical_scrollbar=Scrollbar(billing_frame,orient="vertical",command=tree_view.yview)
    #vertical_scrollbar.place(relx = 0.03, rely = 0.3, anchor = NW)
    #tree_view.configure(xscrollcommand=vertical_scrollbar.set)

    #Definning number of columns
    billing_tree_view["columns"]=("1","2","3","4","5","6","7","8")

    #defining heading
    billing_tree_view["show"]='headings'

    #modifying the size of the columns
    billing_tree_view.column("1",width=100)
    billing_tree_view.column("2",width=200)
    billing_tree_view.column("3",width=140)
    billing_tree_view.column("4",width=80)
    billing_tree_view.column("5",width=90)
    billing_tree_view.column("6",width=80)
    billing_tree_view.column("7",width=100)
    billing_tree_view.column("8",width=120)

    #assigning heading name
    billing_tree_view.heading("1",text="ItemCode")
    billing_tree_view.heading("2",text="Item Name")
    billing_tree_view.heading("3",text="Category")
    billing_tree_view.heading("4",text="Quantity")
    billing_tree_view.heading("5",text="Price")
    billing_tree_view.heading("6",text="TAX")
    billing_tree_view.heading("7",text="Discount")
    billing_tree_view.heading("8",text="Total")

    billing_tree_view.insert("", 0, "item", text="item")

    #Delete Button
    delete_btn=Button(billing_frame,fg=element_color,bg=frame_button_color,text="Delete",width = 15,border=4,command=lambda:[delete_purchase_item()])
    delete_btn.place(relx = 0.028, rely = 0.53, anchor = NW)

    clear_btn=Button(billing_frame,fg=element_color,bg=frame_button_color,text="Clear All",width = 15,border=4,command=lambda:[delete_all_sold_item()])
    clear_btn.place(relx = 0.101, rely = 0.53, anchor = NW)

    Total_discount_lbl=Label(billing_frame,text="Total Discount",font=book_antiqua,bg=frame_color,fg=element_color)
    Total_discount_lbl.place(relx = 0.2, rely = 0.53, anchor = NW)
    Total_discount_lbl2=Label(billing_frame,text="Rs 00.00",font=book_antiqua,bg=frame_color,fg=element_color)
    Total_discount_lbl2.place(relx = 0.28, rely = 0.53, anchor = NW)

    Total_tax_lbl=Label(billing_frame,text="Total Tax ",font=book_antiqua,bg=frame_color,fg=element_color)
    Total_tax_lbl.place(relx = 0.2, rely = 0.55, anchor = NW)
    Total_tax_lbl2=Label(billing_frame,text="Rs 00.00",font=book_antiqua,bg=frame_color,fg=element_color)
    Total_tax_lbl2.place(relx = 0.28, rely = 0.55, anchor = NW)

    Total_items_lbl=Label(billing_frame,text="Total Items ",font=book_antiqua,bg=frame_color,fg=element_color)
    Total_items_lbl.place(relx = 0.2, rely = 0.57, anchor = NW)
    Total_items_lbl2=Label(billing_frame,text="Rs 00",font=book_antiqua,bg=frame_color,fg=element_color)
    Total_items_lbl2.place(relx = 0.28, rely = 0.57, anchor = NW)

    #Save And Print Button
    save_print_button=Button(billing_frame,fg=element_color,bg=frame_button_color,text="Save & Print",width = 13,height=2,border=4,command=lambda:[save_sold_data_to_database(),invoice_number_update()])
    save_print_button.place(relx = 0.44, rely = 0.535, anchor = NW)

    #get all data
    def invoice_number_update():
        billing_bill_number=bill_num('bill_number')
        if path.exists('JSON Files/bill_number.json'):
            write_counter('bill_number',billing_bill_number)
            billing_bill_number_tb.config(state='normal')
            billing_bill_number_tb.delete(0,END)
            billing_bill_number_tb.insert(0,billing_bill_number)
            billing_bill_number_tb.config(state='disabled')
        else:
            write_counter('bill_number',1000)
            billing_bill_number_tb.config(state='normal')
            billing_bill_number_tb.delete(0,END)
            billing_bill_number_tb.insert(0,1000)
            billing_bill_number_tb.config(state='disabled')
    invoice_number_update()

    #Total
    total_lbl=Label(billing_frame,text="0000.00",font=book_antiqua_size18,bg=frame_color,fg=element_color)
    total_lbl.place(relx = 0.51, rely = 0.535, anchor = NW)
    
    def check_entry_condition():
        if len(billing_customer_name_tb.get()) ==0 or len(billing_item_code_tb.get()) ==0 or len(billing_item_name_tb.get()) ==0 or len(billing_quantity_tb.get()) ==0 or len(billing_bill_number_tb.get()) ==0:
            messagebox.showerror(title='Error', message="Enter All Fields")

        elif int(billing_item_code_tb.get())<1:
            messagebox.showerror(title='Error', message="Item Id \ncannot be less than 0")

        elif any(ch.isdigit() or not ch.isalnum() for ch in billing_customer_name_tb.get()):
            messagebox.showerror(title='Error', message="Customer Name \ncannot have number or special charecter")
        elif any(not ch.isdigit() for ch in billing_mobile_tb.get()):
            messagebox.showerror(title='Error', message="Mobile Number \ncannot have Letter or special charecter")
        elif len(billing_mobile_tb.get())!=10:
            messagebox.showerror(title='Error', message="Mobile Number \nmust be 10 Digits")
        elif any(not ch.isdigit() for ch in billing_item_code_tb.get()):
            messagebox.showerror(title='Error', message="Item Code \ncannot have Letter or special charecter")
        elif float(billing_item_code_tb.get())<=0:
            messagebox.showerror(title='Error', message="Invalid Item Code")
        elif any(ch.isalpha() for ch in billing_quantity_tb.get()):
            messagebox.showerror(title='Error', message="Quantity \ncannot have Letter")
        elif float(billing_quantity_tb.get())<=0:
            messagebox.showerror(title='Error', message="Invalid Item Quantity")
        else:
            print()
            tax_amount=(float(billing_tax_tb.get())*float(billing_price_tb.get()))/100
            discount_amount=(float(billing_discount_tb.get())*(float(tax_amount)+float(billing_price_tb.get())))/100
            product_price_after_tax=float(billing_price_tb.get())+float(tax_amount)
            product_price_overall=product_price_after_tax*float(billing_quantity_tb.get())
            total_amount=product_price_overall-discount_amount

            global customer_data
            customer_data={'customer_name':billing_customer_name_tb.get(),'customer_mobile':int(billing_mobile_tb.get()),'customer_bill_number':int(billing_bill_number_tb.get())}

            try:
                con=sqlite3.connect("Database/Store_Data.sql")
                cur=con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS temp_item_sold_details(sold_item_id int(8) PRIMARY KEY NOT NULL,sold_item_name varchar(25) NOT NULL,sold_quantity FLOAT NOT NULL,sold_price FLOAT NOT NULL,sold_category varchar(20),sold_gst FLOAT,sold_discount FLOAT,total_price FLOAT)")
                
                cur.execute("SELECT purchase_quantity from item_purchase_details where item_id={}".format(int(billing_item_code_tb.get())))
                stock=cur.fetchall()
                if stock[0][0]>0:
                    cur.execute("INSERT INTO temp_item_sold_details(sold_item_id,sold_item_name,sold_quantity,sold_price,sold_category,sold_gst,sold_discount,total_price)VALUES({},'{}',{:.2f},{:.2f},'{}',{:.2f},{:.2f},{:.2f}) ON CONFLICT (sold_item_id) DO UPDATE SET sold_quantity=sold_quantity+{:.2f},sold_discount={:.2f} returning sold_item_id".format(int(billing_item_code_tb.get()),billing_item_name_tb.get(),float(billing_quantity_tb.get()),float(billing_price_tb.get()),billing_category_tb.get(),float(tax_amount),float(discount_amount),float(total_amount),float(billing_quantity_tb.get()),float(discount_amount)))
                    id_to_update=cur.fetchall()
                    cur.execute("SELECT sold_quantity FROM temp_item_sold_details where sold_item_id={}".format(id_to_update[0][0]))
                    updated_quantity=cur.fetchall()
                    cur.execute("UPDATE temp_item_sold_details SET total_price=({}*(sold_price+sold_gst))-sold_discount where sold_item_id={:.2f}".format(float(updated_quantity[0][0]),id_to_update[0][0]))
                    con.commit()
                    cur.execute("SELECT sold_item_id,sold_item_name,sold_category,sold_quantity,sold_price,sold_gst,sold_discount,total_price FROM temp_item_sold_details ORDER BY sold_item_id ASC")
                    row=cur.fetchall()
                    clear_all(billing_tree_view)
                    for i in row:
                        billing_tree_view.insert("", 'end', text ="L1",values =(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
                    cur.execute("SELECT SUM(total_price) FROM temp_item_sold_details")
                    total=cur.fetchall()
                    cur.execute("SELECT * FROM temp_item_sold_details")
                    total_products=cur.fetchall()
                    cur.execute("SELECT SUM(sold_discount) FROM temp_item_sold_details")
                    total_discount=cur.fetchall()
                    cur.execute("SELECT SUM(sold_gst) FROM temp_item_sold_details")
                    total_tax=cur.fetchall()
                    con.commit()
                    if len(total)<1:
                        total_lbl.configure(text="0000.00")
                        Total_discount_lbl2.configure(text="Rs 00.00")
                        Total_tax_lbl2.configure(text="Rs 00.00")
                        Total_items_lbl2.configure(text="Rs 00")
                    else:
                        total_lbl.configure(text="{:.2f}".format(float(total[0][0])))
                        Total_discount_lbl2.configure(text="Rs {:.2f}".format(float(total_discount[0][0])))
                        Total_tax_lbl2.configure(text="Rs {:.2f}".format(float(total_tax[0][0])))
                        Total_items_lbl2.configure(text="Rs {}".format(len(total_products)))
                    con.commit()
                    cur.execute("UPDATE item_purchase_details SET purchase_quantity=purchase_quantity-{:.2f} where item_id={}".format(float(billing_quantity_tb.get()),int(billing_item_code_tb.get())))
                    
                    cur.execute("SELECT purchase_quantity FROM item_purchase_details WHERE item_id={}".format(int(billing_item_code_tb.get())))
                    updated_stock=cur.fetchall()
                    if updated_stock[0][0]<0:
                        con.rollback()
                        messagebox.showerror(title='Error', message="Stock Empty\ only '{}' stock left".format(stock[0][0]))
                    con.commit()
                    con.close()
            except sqlite3.Error as err:
                print("Error - ",err)
                error_message=str(err)
                print(error_message[0:24])
                if error_message[0:24]=='UNIQUE constraint failed':
                    messagebox.showerror(title='Error', message="Item Code cannot repeat")
                con.close()

    def delete_all_sold_item():
        temp=messagebox.askquestion('Delete Product', 'Are you sure you want to Clear All')
        if temp=='yes':
            clear_all(billing_tree_view)
            try:
                con=sqlite3.connect("Database/Store_Data.sql")
                cur=con.cursor()
                cur.execute("drop table temp_item_sold_details")
                cur.execute("CREATE TABLE IF NOT EXISTS temp_item_sold_details(sold_item_id int(8) PRIMARY KEY NOT NULL,sold_item_name varchar(25) NOT NULL,sold_quantity FLOAT NOT NULL,sold_price FLOAT NOT NULL,sold_category varchar(20),sold_gst FLOAT,sold_discount FLOAT,total_price FLOAT)")
                total_lbl.configure(text="0000.00")
                Total_discount_lbl2.configure(text="Rs 00.00")
                Total_tax_lbl2.configure(text="Rs 00.00")
                Total_items_lbl2.configure(text="Rs 00")
                con.commit()
                con.close()
            except sqlite3.Error as err:
                print("Error - ",err)

    def delete_purchase_item():
        selected_treeview_item=selected_item_from_treeview(billing_tree_view,'purchase_tree_view')
        temp=messagebox.askquestion('Delete Product', 'Are you sure you want to Delete')
        if temp=='yes':
            try:
                con=sqlite3.connect("Database/Store_Data.sql")
                cur=con.cursor()
                cur.execute("DELETE FROM temp_item_sold_details where sold_item_id={}".format(selected_treeview_item))
                cur.execute("SELECT sold_item_id,sold_item_name,sold_category,sold_quantity,sold_price,sold_gst,sold_discount,total_price FROM temp_item_sold_details ORDER BY sold_item_id ASC")
                row=cur.fetchall()

                #fixing to be done
                curItem = billing_tree_view.focus()
                billing_tree_view.item(curItem)
                selected_items1 =billing_tree_view.item(curItem)
                print(selected_items1)
                for key, value in selected_items1.items():
                    if key == 'values':
                        selected_treeview_item3=value[3]

                clear_all(billing_tree_view)
                for i in row:
                    billing_tree_view.insert("", 'end', text ="L1",values =(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
                cur.execute("SELECT SUM(total_price) FROM temp_item_sold_details")
                total=cur.fetchall()
                cur.execute("SELECT * FROM temp_item_sold_details")
                total_products=cur.fetchall()
                cur.execute("SELECT SUM(sold_discount) FROM temp_item_sold_details")
                total_discount=cur.fetchall()
                cur.execute("SELECT SUM(sold_gst) FROM temp_item_sold_details")
                total_tax=cur.fetchall()
                if str(total[0][0])=='None':
                    total_lbl.configure(text="0000.00")
                    Total_discount_lbl2.configure(text="Rs 00.00")
                    Total_tax_lbl2.configure(text="Rs 00.00")
                    Total_items_lbl2.configure(text="Rs 00")
                else:
                    total_lbl.configure(text="{:.2f}".format(float(total[0][0])))
                    Total_discount_lbl2.configure(text="Rs {:.2f}".format(float(total_discount[0][0])))
                    Total_tax_lbl2.configure(text="Rs {:.2f}".format(float(total_tax[0][0])))
                    Total_items_lbl2.configure(text="Rs {}".format(len(total_products)))

                cur.execute("UPDATE item_purchase_details SET purchase_quantity=purchase_quantity+{:.2f} where item_id={}".format(float(selected_treeview_item3),selected_treeview_item))
                #####
                con.commit()
                con.close()
            except sqlite3.Error as err:
                print("Error - ",err)
    def pdf_output():
        pdf= fpdf.FPDF()
        pdf.add_page()

        def pdf_arial():
            pdf.set_font("Arial", size = 12)

        def pdf_arial_bold():
            pdf.set_font("Arial",style="B", size = 12)

        #invoice
        pdf.set_font("Times",style="BU", size = 55)
        pdf.cell(93, 28, txt = "INVOICE",ln = 2, align = 'L', border=0)
        


        #celspacer
        def cellspacer():
            pdf.cell(30, 7,ln = 0, align = 'L', border=0)

        def cellspacer_bottom():
            pdf.cell(30, 5,ln = 1, align = 'L', border=0)


        #row1
        pdf.set_font("Arial",style="B", size = 12)
        pdf.cell(30, 5, txt = "Bill Number",ln = 0, align = 'L', border=0)
        cellspacer()
        pdf.cell(30, 5, txt = "Date of Issue",ln = 1, align = 'L', border=0)

        #row2
        pdf_arial()
        pdf.cell(30, 7, txt = "{}".format(int(billing_bill_number_tb.get())),ln = 0, align = 'L', border=0)
        cellspacer()
        pdf.cell(30, 7, txt = "{}".format(datesorted),ln = 1, align = 'L', border=0)

        #row3
        cellspacer_bottom()

        #row4
        pdf_arial_bold()
        pdf.cell(30, 5, txt = "Billed To",ln = 0, align = 'L', border=0)
        cellspacer()
        pdf.cell(30, 5, txt = "The-Mart",ln = 1, align = 'L', border=0)

        #row5
        pdf_arial()
        pdf.cell(30, 7, txt = "{}".format(billing_customer_name_tb.get()),ln = 0, align = 'L', border=0)
        cellspacer()
        pdf.cell(30, 7, txt = "{}".format("5th Street"),ln = 1, align = 'L', border=0)
        cellspacer()
        cellspacer()
        pdf.cell(30, 7, txt = "{}".format("#company mail"),ln = 1, align = 'L', border=0)
        cellspacer()
        cellspacer()
        pdf.cell(30, 7, txt = "{}".format("#contact number"),ln = 1, align = 'L', border=0)
        cellspacer_bottom()
        cellspacer_bottom()
        pdf_arial_bold()
        pdf.cell(10, 7, txt = "{}".format("no."),ln = 0, align = 'L', border=0)
        pdf.cell(30, 7, txt = "{}".format("Item Name"),ln = 0, align = 'L', border=0)
        pdf.cell(30, 7, txt = "{}".format("Units/Kg"),ln = 0, align = 'L', border=0)
        pdf.cell(30, 7, txt = "{}".format("Unit Cost"),ln = 0, align = 'L', border=0)
        pdf.cell(30, 7, txt = "{}".format("Tax"),ln = 0, align = 'L', border=0)
        pdf.cell(30, 7, txt = "{}".format("Discount"),ln = 0, align = 'L', border=0)
        pdf.cell(30, 7, txt = "{}".format("Amount"),ln = 1, align = 'L', border=0)
        pdf.line(11, 99, 187, 99)

        cellspacer_bottom()
        try:
                con=sqlite3.connect('Database/Store_Data.sql')
                cur=con.cursor()
                cur.execute("SELECT ROWID,sold_item_name,sold_quantity,sold_price,sold_gst,sold_discount,total_price FROM temp_item_sold_details ORDER BY ROWID ASC")
                rec=cur.fetchall()
                for i in rec:
                    number_of_items=len(rec)
                    pdf_arial()
                    pdf.cell(10, 7, txt = "{}".format(i[0]),ln = 0, align = 'L', border=0)
                    pdf.cell(30, 7, txt = "{}".format(i[1]),ln = 0, align = 'L', border=0)
                    pdf.cell(30, 7, txt = "{}".format(i[2]),ln = 0, align = 'L', border=0)
                    pdf.cell(30, 7, txt = "{}".format(i[3]),ln = 0, align = 'L', border=0)
                    pdf.cell(30, 7, txt = "{}".format(i[4]),ln = 0, align = 'L', border=0)
                    pdf.cell(30, 7, txt = "{}".format(i[5]),ln = 0, align = 'L', border=0)
                    pdf.cell(30, 7, txt = "{}".format(i[6]),ln = 1, align = 'L', border=0)
                cur.execute("SELECT SUM(total_price) FROM temp_item_sold_details")
                total_pdf=cur.fetchall()
                cur.execute("SELECT SUM(sold_discount) FROM temp_item_sold_details")
                total_discount=cur.fetchall()
                cur.execute("SELECT SUM(sold_gst) FROM temp_item_sold_details")
                total_gst=cur.fetchall()
                con.commit()
                con.close()
        except sqlite3.Error as err:
            print("Error: ",err)

        pdf.cell(30, 7, txt = "{}".format("-----------------------------------------------------------------------------------------------------------------------------"),ln = 1, align = 'L', border=0)
        pdf.cell(10, 7,ln = 0, align = 'L', border=0)
        cellspacer()
        cellspacer()
        cellspacer()
        cellspacer()
        pdf_arial_bold()
        pdf.cell(30, 7, txt = "{}".format("Total"),ln = 0, align = 'L', border=0)
        pdf_arial()
        pdf.cell(30, 7, txt = "{}".format(total_pdf[0][0]),ln = 1, align = 'L', border=0)
        pdf_arial_bold()
        
        pdf.cell(30, 7, txt = "{}".format("Total Discount"),ln = 0, align = 'L', border=0)
        pdf_arial()
        pdf.cell(10, 7,ln = 0, align = 'L', border=0)
        pdf.cell(30, 7, txt = "{}".format(total_discount[0][0]),ln = 1, align = 'L', border=0)
        pdf_arial_bold()
        
        pdf.cell(30, 7, txt = "{}".format("Total Tax"),ln = 0, align = 'L', border=0)
        pdf_arial()
        pdf.cell(10, 7,ln = 0, align = 'L', border=0)
        pdf.cell(30, 7, txt = "{}".format(total_gst[0][0]),ln = 0, align = 'L', border=0)
        make_directory('Billed Bills')
        pdf.output("Billed Bills/{}.pdf".format(billing_bill_number_tb.get()))
    
    def save_sold_data_to_database():
            try:
                con=sqlite3.connect("Database/Store_Data.sql")
                cur=con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS customer_details(customer_name varchar(20) NOT NULL,mobile_number int(10),bill_number int(8) NOT NULL,bill_date date,amount FLOAT)")
                cur.execute("CREATE TABLE IF NOT EXISTS item_sold_details(bill_number int(8),sold_item_name varchar(25),sold_quantity FLOAT,sold_price FLOAT ,sold_category varchar(20),sold_gst FLOAT,sold_discount FLOAT,total_price FLOAT)")
                cur.execute("SELECT * from temp_item_sold_details ORDER BY sold_item_name ASC")
                row=cur.fetchall()
                cur.execute("SELECT SUM(total_price) FROM temp_item_sold_details")
                total=cur.fetchall()
                for i in row:
                    cur.execute("INSERT INTO item_sold_details(bill_number,sold_item_name,sold_quantity,sold_price,sold_category,sold_gst,sold_discount,total_price)VALUES({},'{}',{:.2f},{:.2f},'{}',{:.2f},{:.2f},{:.2f})".format(int(billing_bill_number_tb.get()),i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
                    id_to_update=cur.fetchall()
                    #cur.execute("UPDATE item_purchase_details SET total_price=purchase_quantity*buying_price where item_id={}".format(id_to_update[0][0]))
                
                cur.execute("INSERT INTO customer_details(bill_number,bill_date,customer_name,mobile_number,amount)VALUES({},'{}','{}',{},{})".format(customer_data['customer_bill_number'],datesorted,customer_data['customer_name'],customer_data['customer_mobile'],float(total[0][0])))
                messagebox.showinfo(title='Saved', message="Products Added to inventory")
                pdf_output()
                cur.execute("drop table temp_item_sold_details")
                con.commit()
                con.close()
                delete_all_sold_item()
            except sqlite3.Error as err:
                print("Error - ",err)
                messagebox.showerror(title='Error', message="No Data to Save")
    
    con=sqlite3.connect("Database/Store_Data.sql")
    cur=con.cursor()
    cur.execute("drop table if exists temp_item_sold_details")
    cur.execute("CREATE TABLE IF NOT EXISTS temp_item_sold_details(sold_item_id int(8) PRIMARY KEY NOT NULL,sold_item_name varchar(25) NOT NULL,sold_quantity FLOAT NOT NULL,sold_price FLOAT NOT NULL,sold_category varchar(20),sold_gst FLOAT,sold_discount FLOAT,total_price FLOAT,updated_price FLOAT)")
    con.commit()
    con.close()

menu_frame_obj()
def onclose():
    write_counter('bool_for_cleaner','False')
    root.destroy()

write_counter('cleaner','company_details_frame')
company_details_obj()
write_counter('bool_for_cleaner','False')
root.protocol("WM_DELETE_WINDOW", onclose)
root.mainloop()
