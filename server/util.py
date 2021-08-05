import pickle
import json
import numpy as np
import tkinter as tk
import os
from flask import Flask, request, jsonify, render_template
 

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations
    print(os.listdir("d:\BangloreHomePrices\server"))
    with open("d:\BangloreHomePrices\server\columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open("D:\BangloreHomePrices\Banglore_home_prices_model.pickle", 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    
    return __locations
    

def get_data_columns():
    return __data_columns

'''
def ask():
    location = input('enter location: ')
    area = int(input('enter area: '))
    bhk = int(input('no of bed: '))
    bath = int(input('no of bath: '))
    price = get_estimated_price(location,area,bhk,bath)
    print(price)
'''
class ps_wn():
        def __init__(self):
                self.p=0
                self.root=tk.Tk()
                self.root.geometry('500x500')
                self.label_ = tk.Label(self.root, text= "Banglore Price Prediction",font=("bold",14))
                self.label_.place(x=150,y=10)

                self.label_1 = tk.Label(self.root, text= "estimated price" ,bg="yellow",font=("bold",14)) 
                self.label_1.place(x=100,y=400)

                #area window
                label_1 = tk.Label(self.root, text= "Area : ",font=("bold",14))
                label_1.place(x=10,y=145)
                self.entry = tk.Entry(self.root)
                self.entry.place(x=150,y=150)
                
                label_1 = tk.Label(self.root, text= "Location : ",font=("bold",14))
                label_1.place(x=10,y=200)

                #location window
                with open("d:\BangloreHomePrices\server\columns.json", "r") as f:
                        
                        __data_columns = json.load(f)['data_columns']
                        self.__locations = __data_columns[3:]
                        
                self.options = self.__locations
                
                # datatype of menu text
                self.clicked = tk.StringVar()
                  
                # initial menu text
                self.clicked.set( "select location" )
                  
                # Create Dropdown menu
                drop = tk.OptionMenu( self.root , self.clicked , *self.options )
                drop.place(x=150,y=205)

                #bhk window
                
                label_1 = tk.Label(self.root, text= "BHK : ",font=("bold",14))
                label_1.place(x=10,y=255)
                self.entry_1 = tk.Entry(self.root)
                self.entry_1.place(x=150,y=260)

                #bath window

                label_1 = tk.Label(self.root, text= "Bath : ",font=("bold",14))
                label_1.place(x=10,y=310)
                self.entry_2 = tk.Entry(self.root)
                self.entry_2.place(x=150,y=315)


  
                                
                #starting
                self.entry.focus_set()
                self.root.bind('<Return>', self.ck)
                self.root.mainloop()

        def ck (self,event):
                a = self.entry.get()
                l = self.clicked.get()
                bh = int(self.entry_1.get())
                ba = int(self.entry_2.get())

                self.price = get_estimated_price(l,a,bh,ba)
                self.label_1.destroy()
                self.label_1 = tk.Label(self.root, text= str(self.price) ,bg="yellow",font=("bold",14)) 
                self.label_1.place(x=100,y=400)


load_saved_artifacts()
a = ps_wn()

'''
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    #ask()

   
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('malleshpalya', 1000, 3, 3))  # other location
   
'''




'''
app = Flask(__name__)

@app.route('/')
@app.route('/home') 
def home():
      return render_template("app.html")

@app.route('/predict_home_price')
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    print(total_sqft)
    print(location)
    print(bhk)
    print(bath)

    price= get_estimated_price(location, total_sqft, bhk, bath)
    print(price)
    
    return render_template("app.html",price = price)


@app.route("/predict")
def predict():
    title = request.args.get('title')
    rcmd=recommendations(title)
    m = rcmd[0]
    r = rcmd[1]
    a = rcmd[2]
    d = rcmd[3]
    s = rcmd[4]
    return render_template('recommend.html', title=title, m=m,r=r,a=a,d=d,s=s)

if __name__ == '__main__':
    app.run()
'''