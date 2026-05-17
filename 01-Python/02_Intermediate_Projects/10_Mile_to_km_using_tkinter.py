from tkinter import *


def mile_to_km():
    miles = float(mile_input.get())
    kms = miles * 1.609
    km_result_label["text"] = f"{kms}"

window = Tk()
window.minsize(width=500, height=300)
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


mile_input = Entry(width=10)
mile_input.grid(column=1, row=0)
mile = mile_input.get()


mile_label= Label(text="Miles")
mile_label.grid(column=2, row=0)


is_equal_label = Label(text= "mile_to_km")
is_equal_label.grid(column=0, row=1)


km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


calculate_button = Button(text="Convert", command= mile_to_km)
calculate_button.config(bg="yellow")
calculate_button.grid(column=1, row=2)

window.mainloop()