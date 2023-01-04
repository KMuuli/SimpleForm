from tkinter import *

from Circle import Circle


# def return_pressed(event):
      #  calculate()


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def calculate(event):
    # print("Button clicked")  # Test!
    radius = user_input.get()   # radius is string
    # print(radius)  # Test!
    if is_float(radius):
        user_input.delete(0, END)  # Clear input
        radius = float(radius)  # now is radius float
        circle = Circle(radius)
        txt_field["state"] = "normal"  # can change field
        txt_field.delete("1.0", END)  # Clear txt_field line 1 to end
        txt_field.insert(END, "Radius: " + str(circle.radius) + "\n" + "Diameter: " + str(circle.get_diameter()) + "\n"
                         + "Area: " + str(circle.get_area()) + "\n" + "Perimeter: " + str(circle.get_perimeter()) + "\n")
        txt_field["state"] = "disabled"  # can change field

        # print("Number")  # Test
    # else:
        # print("Error")  # Test


# Main window properties
window = Tk()   # Create main window
window.title("Geometry - Circle")  # Title text
# window.geometry("400x500")  # width=400 height=500
window.resizable(False, False)  # True width, False height

# Frames
frame_top = Frame(window, bg="#89CFF0", height=50)
frame_top.pack(fill="both")  # "both" variant 1

frame_bottom = Frame(window, bg="#90EE90", height=50)
frame_bottom.pack(fill=BOTH)  # BOTH VARIANT 2

# First line in frame top
lbl = Label(frame_top, text="Circle radius", bg="#89CFF0")
lbl.pack(side=LEFT)

user_input = Entry(frame_top)
user_input.pack(side=LEFT)
user_input.focus()

btn_calc = Button(frame_top, text="Calculate", command=lambda: calculate(0))
btn_calc.pack(side=LEFT, padx=2, pady=2)



# second line, one big textfield

txt_field = Text(frame_bottom, state=DISABLED)
txt_field.pack(side=LEFT, padx=2, pady=2)

# Bind Entry key
# window.bind("<Return>", return_pressed)
window.bind("<Return>", lambda event: calculate(event))

# No MVC last line
window.mainloop()
