import tkinter as tk

farby = ['green', 'red', 'blue', 'orange']
skratky = ['z', 'c', 'm', 'o']
stvorce = []

# funkcia ktora spracuje kliknutie
def vyber(event):
    id_studenta = entry.get()

    # ak je policko prazdne
    if id_studenta == "":
        return

    kliknute = canvas.find_overlapping(event.x, event.y, event.x + 1, event.y + 1)

    # prejdeme 4 stvorce
    for i in range(4):
        if stvorce[i] in kliknute:
            pismeno = skratky[i]

            # zapiseme do suboru
            subor = open('vyber_jedla.txt', 'a')
            subor.write(id_studenta + " " + pismeno + "\n")
            subor.close()
            print("Zapísané:", id_studenta, pismeno)


win = tk.Tk()
canvas = tk.Canvas(win, width=450, height=350, bg='white')
canvas.pack()

# vymazeme subor
open('vyber_jedla.txt', 'w').close()

canvas.create_text(225, 40, text="VÝBER JEDLA", font="Arial 25 bold", fill="red")

for i in range(4):
    stvorce.append(canvas.create_rectangle(30 + i * 100, 80, 120 + i * 100, 200, fill=farby[i]))

canvas.create_text(225, 230, text="kód študenta:")
entry = tk.Entry(win)
canvas.create_window(225, 260, window=entry)

# prepojenie kliknutia
canvas.bind('<Button-1>', vyber)

win.mainloop()