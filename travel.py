import tkinter as tk
from tkinter import messagebox

#Dictionary for base travel cost

DESTINATION={
    "Kerela":9500,
    "Tamilnadu":9000,
    "karnataka":8000,
    "Andhra Pradesh":8000,
    "Rajastan":8000,
    "Himachal Pradesh":9500,
    "Pondicherry":9000
}

#extra cost based mode of transport
TRAVEL_MODE_COST= {
    "Flight": 2000,
    "Train":1000
}

def calculate_cost():
    name= name_entry.get()
    destination= destination_var.get()
    mode= mode_var.get()
    if not name:
        messagebox.showerror("Error", "Please enter your name.")
        return
    if destination==""or mode=="":
        messagebox.showerror("Error", "Please select destination and travel mode.")
        return
    
    cost= DESTINATION[destination]+TRAVEL_MODE_COST[mode]
    result= f"Hi {name}, Your estimated travel cost to {destination} by {mode} is Rs{cost}."
    messagebox.showinfo("Travel Estimate", result)


#create main window
root= tk.Tk()
root.title("Basic Travelling App")

root.geometry("350x300")

#widgets
tk.Label(root, text="Welocme to TravelBay", font=("Helvetica",16)).pack(pady=10)

tk.Label(root,text="Enter your name:").pack()
name_entry=tk.Entry(root)

name_entry.pack()
tk.Label(root,text="Choose Destination:").pack()

destination_var=tk.StringVar()
destination_menu=tk.OptionMenu(root, destination_var,*DESTINATION.keys())
destination_menu.pack()

tk.Label(root,text="Select Travel Mode:").pack()
mode_var=tk.StringVar()
tk.Radiobutton(root, text="Flight", variable=mode_var, value="Flight").pack()
tk.Radiobutton(root,text="Train", variable=mode_var, value="Train").pack()

tk.Button(root, text="Calculate Cost", command=calculate_cost).pack(pady=10)


#run the app

root.mainloop()

