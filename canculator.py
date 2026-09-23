import customtkinter as ctk

root = ctk.CTk()
root.title("Canculator")
root.geometry("700x800")
root.resizable(width=False, height=False)

label1 = ctk.CTkLabel(root, text="", font=("Arial", 60, "bold"), width=680, height=100, fg_color="white", text_color="black", corner_radius=10)
label1.place(x=10, y=10)

def add_number(number):
    current_number = label1.cget("text")

    if current_number == "":
      label1.configure(text=str(number))
    else:
        label1.configure(text=current_number + str(number))

def example():
        text = label1.cget("text")

        if not text:
            return



        if "+" in text:
            parts = text.split("+")
            result = float(parts[0]) + float(parts[1])
        elif "-" in text:
            parts = text.split("-")
            result = float(parts[0]) - float(parts[1])
        elif "*" in text:
            parts = text.split("*")
            result = float(parts[0]) * float(parts[1])
        elif "/" in text:
            parts = text.split("/")
            result = float(parts[0]) / float(parts[1])
        else:
            return

        if result.is_integer():
            result = int(result)

        label1.configure(text=str(result))

def delete():
    current_number = label1.cget("text")

    new_text = current_number[:-1]
    label1.configure(text=new_text)

button1 = ctk.CTkButton(root, text="1", font=("Arial", 35, "bold"), width=150, height=130, command=lambda: add_number(1))
button1.place(x=30, y=130)

button2 = ctk.CTkButton(root, text="2", font=("Arial", 35, "bold"), width=150, height=130, command=lambda: add_number(2))
button2.place(x=200, y=130)

button3 = ctk.CTkButton(root, text="3", font=("Arial", 35, "bold"), width=150, height=130, command=lambda: add_number(3))
button3.place(x=370, y=130)

button4 = ctk.CTkButton(root, text="4", font=("Arial", 35, "bold"), width=150, height=130, command=lambda: add_number(4))
button4.place(x=30, y=290)

button5 = ctk.CTkButton(root, text="5", font=("Arial", 35, "bold"), width=150, height=130, command=lambda: add_number(5))
button5.place(x=200, y=290)

button6 = ctk.CTkButton(root, text="6", font=("Arial", 35, "bold"), width=150, height=130, command=lambda: add_number(6))
button6.place(x=370, y=290)

button7 = ctk.CTkButton(root, text="7", font=("Arial", 35, "bold"), width=150, height=130, command=lambda: add_number(7))
button7.place(x=30, y=450)

button8 = ctk.CTkButton(root, text="8", font=("Arial", 35, "bold"), width=150, height=130, command=lambda: add_number(8))
button8.place(x=200, y=450)

button9 = ctk.CTkButton(root, text="9", font=("Arial", 35, "bold"), width=150, height=130, command=lambda: add_number(9))
button9.place(x=370, y=450)

button0 = ctk.CTkButton(root, text="0", font=("Arial", 35, "bold"), width=150, height=130, command=lambda: add_number(0))
button0.place(x=200, y=610)

button10 = ctk.CTkButton(root, text="/", font=("Arial", 45, "bold"), width=120, height=110, command=lambda: add_number("/"))
button10.place(x=540, y=130)

button11 = ctk.CTkButton(root, text="*", font=("Arial", 45, "bold"), width=120, height=110, command=lambda: add_number("*"))
button11.place(x=540, y=260)

button12 = ctk.CTkButton(root, text="-", font=("Arial", 45, "bold"), width=120, height=110, command=lambda: add_number("-"))
button12.place(x=540, y=390)

button12 = ctk.CTkButton(root, text="+", font=("Arial", 45, "bold"), width=120, height=110, command=lambda: add_number("+"))
button12.place(x=540, y=520)

button12 = ctk.CTkButton(root, text="=", font=("Arial", 45, "bold"), width=120, height=110, command=example)
button12.place(x=540, y=650)

button13 = ctk.CTkButton(root, text="#", font=("Arial", 45, "bold"), width=120, height=110, command=delete)
button13.place(x=45, y=620)

root.mainloop()

