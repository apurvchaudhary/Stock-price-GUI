
# coding: utf-8

# In[181]:


import tkinter as tk
from iexfinance import get_historical_data
import seaborn as sns                     
from datetime import datetime              
import matplotlib.pyplot as plt           
import numpy as np                        
def dataframe(company):       #defining a function with parameter company(for company value to get data) & title(for mentioning on title) 
    start=entry_field1.get()
    start=datetime.strptime(start,'%Y-%m-%d')
    end=entry_field2.get()
    end=datetime.strptime(end,'%Y-%m-%d')
    df =get_historical_data(company, start, end, output_format='pandas') #getting data from iexfinance library to df
    c=df['open']  #assigning opening stocks prices to varibale c  likewise for b,d,a                               
    b=df['high']  
    d=df['low']
    a=df['close']
    sns.set()      #showing graph of values passed from the func dataframe from seaborn (hereafter we will be using many func from seaborn library)
    sns.set_style("darkgrid") 
    sns.set(rc={'figure.figsize':(14.7,8.27)}) #setting size of graph
    ax=plt.subplot(111)  #plotting subplot for mentioning legends
    c.plot(label='Opening Price',color='blue') #plotting graph from matplotlib library likewise b,d,a
    b.plot(label='Highest Price',color='g')    
    d.plot(label='Lowest Price',color='r')
    a.plot(label='Closing Price',color='c')
    plt.title('Stock Prices of :'+ str(company))   #plotting title name and value(argument) is getting from title parameter what we defined in func
    plt.xlabel(entry_field1.get() + " to " + entry_field2.get() ) #setting labels x and y names
    plt.ylabel('Price in USD(US Dollars)')
    ax.legend()                             #calling legend to mention in graph
    plt.show()   


# In[182]:


window = tk.Tk()

#title
window.title("APURV CHAUDHARY © 2018 GUI")

#gui size
window.geometry("600x500")

#functions
def display():
    company=var.get()
    disp=dataframe(company)
    dis=tk.Text(master=window,height=18,width=16)
    dis.grid(row=8, sticky="s")
    dis.insert(tk.END,disp)
    graph = FigureCanvasTkAgg(fig, master=app)
    canvas = graph.get_tk_widget()
    canvas.grid(row=8, column=0, rowspan = 1, padx =10, pady =5)



#label
prompt =  tk.Label(text="APURV'S STOCK PRICE  GENERATOR!!", bg="Red", pady=2, font=("Goudy Stout",10), height=1, width=40)
prompt.grid(column=0, row=0)

#entry fiel1
prompt1=tk.Label(text="Starting Date i.e YYYY-MM-DD")
prompt1.grid(row=1, rowspan=1, sticky="w")
entry_field1 = tk.Entry()
entry_field1.grid(row=2, rowspan=1,sticky="w")

#ENTRY FIELD 2
prompt2=tk.Label(text="Ending Date i.e YYYY-MM-DD")
prompt2.grid(row=3, rowspan=1, sticky="w")
entry_field2 = tk.Entry()
entry_field2.grid(row=4, rowspan=1, sticky="w")

#option menu
var = tk.StringVar(window)
var.set("Company")
option = tk.OptionMenu(window,var,"MSFT","FB","NFLX","AMZN","AAPL")
option.grid(row=5,rowspan=1, stick="W")

#button
button1 = tk.Button(text="Submit",command=display)
button1.grid(row=7,rowspan=1, sticky="w")

window.mainloop()

