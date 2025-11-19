import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

options = ["Opcja 1", "Opcja 2", "Opcja specjalna", "Opcja 4"]

HEADER_INDEX = 0

DEFAULT_FG = "black"
DEFAULT_BG = "white"


def show_list(event=None):
    x = label.winfo_rootx()
    y = label.winfo_rooty() + label.winfo_height()
    top.geometry(f"+{x}+{y}")
    top.deiconify()


def hide_list(event=None):
    widget = root.winfo_containing(root.winfo_pointerx(), root.winfo_pointery())
    if widget not in (label, top, listbox):
        top.withdraw()


def on_select(event):
    i = listbox.curselection()[0]

    if i == HEADER_INDEX:
        listbox.selection_clear(0, tk.END)
        return

    text = listbox.get(i)
    label.config(text=text)
    apply_item_colors_to_label(i)
    top.withdraw()


def block_header_click(event):
    index = listbox.nearest(event.y)
    if index == HEADER_INDEX:
        return "break"


def apply_item_colors_to_label(index):
    """Pobiera fg/bg z Listboxa i ustawia w Label."""
    fg = listbox.itemcget(index, "fg")
    bg = listbox.itemcget(index, "bg")

    if not fg:
        fg = DEFAULT_FG
    if not bg:
        bg = DEFAULT_BG

    label.config(fg=fg, bg=bg)


# -----------------------------
# "Entry" → Label
# -----------------------------
label = tk.Label(
    root,
    text=options[0],
    width=25,
    anchor="w",
    relief="solid",
    bd=1,
    bg=DEFAULT_BG,
    fg=DEFAULT_FG,
)
label.pack(pady=20)

label.bind("<Enter>", show_list)
label.bind("<Leave>", hide_list)

# -----------------------------
# Popup lista
# -----------------------------
top = tk.Toplevel(root)
top.overrideredirect(True)
top.withdraw()

listbox = tk.Listbox(top)
listbox.pack()

# Nagłówek — nieklikalny
listbox.insert(tk.END, "move to:")
listbox.itemconfig(0, {"fg": "gray"})

# Pozostałe opcje
for i, opt in enumerate(options, start=1):
    listbox.insert(tk.END, opt)
    if opt == "Opcja specjalna":
        listbox.itemconfig(i, {"fg": "red"})  # kolor specjalny

listbox.bind("<<ListboxSelect>>", on_select)
listbox.bind("<Button-1>", block_header_click)

top.bind("<Leave>", hide_list)
listbox.bind("<Leave>", hide_list)

root.mainloop()
