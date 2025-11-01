import tkinter as tk

def datsubmit():
    input_data = inputtxt.get("1.0", "end-1c")
    print(input_data)

#creates the main window
window = tk.Tk()
#set the size of overall window
window.geometry("300x300")
#set the title for the GUI
window.title("STM32 Flasher")


#Label the window
greet = tk.Label(window, text="Enter text")
#To show the widget
greet.pack(pady=10)

#Display the text colum
inputtxt = tk.Text(window, height = 10,
                width = 25,
                bg = "light yellow")
inputtxt.pack()

#when the button is pressed, It will execute the datsubmit function
btn_submit = tk.Button(
    master=window,
    text="Submit",
    anchor="center",
    background="green",
    command=datsubmit
)
btn_submit.pack(pady=10)

window.mainloop()
