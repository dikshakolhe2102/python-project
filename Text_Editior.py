from tkinter import *
from tkinter import ttk,filedialog
from PIL import Image, ImageTk
import os
# ================= Window =================
win = Tk()
win.title("Text Editor")
win.geometry("800x500")

# ============= Get Relative Path =================
Base_dir = os.path.dirname(os.path.abspath(__file__))

# ================= Notebook =================
notebook = ttk.Notebook(win)
notebook.pack(expand=True, fill="both")

# ================= Images ===================
icons={}
icons["folder"] = ImageTk.PhotoImage(Image.open(os.path.join(Base_dir,"Images","open_folder.jpeg")).resize((16,16)))
icons["file"] = ImageTk.PhotoImage(Image.open(os.path.join(Base_dir,"Images","open_file.jpeg")).resize((16,16)))
icons["exit"] = ImageTk.PhotoImage(Image.open(os.path.join(Base_dir,"Images","exit.jpeg")).resize((16,16)))
icons["cut"] = ImageTk.PhotoImage(Image.open(os.path.join(Base_dir,"Images","cut.jpeg")).resize((16,16)))
icons["copy"] = ImageTk.PhotoImage(Image.open(os.path.join(Base_dir,"Images","paste.jpeg")).resize((16,16)))
icons["paste"] = ImageTk.PhotoImage(Image.open(os.path.join(Base_dir,"Images","copy.jpeg")).resize((16,16)))
icons["clear"] = ImageTk.PhotoImage(Image.open(os.path.join(Base_dir,"Images","clear_all.jpeg")).resize((16,16)))
icons["Open_file"] = ImageTk.PhotoImage(Image.open(os.path.join(Base_dir,"Images","file.jpeg")).resize((16,16)))
icons["redo"] = ImageTk.PhotoImage(Image.open(os.path.join(Base_dir,"Images","redo.jpeg")).resize((16,16)))
icons["undo"] = ImageTk.PhotoImage(Image.open(os.path.join(Base_dir,"Images","undo.jpeg")).resize((16,16)))
icons["Zoom_in"] = ImageTk.PhotoImage(Image.open(os.path.join(Base_dir,"Images","zoom_out.jpeg")).resize((16,16)))
icons["Zoom_out"] = ImageTk.PhotoImage(Image.open(os.path.join(Base_dir,"Images","zoom_minus.jpeg")).resize((16,16)))
icons["Zoom_restore"] = ImageTk.PhotoImage(Image.open(os.path.join(Base_dir,"Images","restore.jpeg")).resize((16,16)))
icons["Zoom"] = ImageTk.PhotoImage(Image.open(os.path.join(Base_dir,"Images","Zoom.jpeg")).resize((16,16)))
icons["new_file"] = ImageTk.PhotoImage(Image.open(os.path.join(Base_dir,"Images","new_file.jpeg")).resize((16,16)))
icons["close"] = ImageTk.PhotoImage(Image.open(os.path.join(Base_dir,"Images","Close.jpeg")).resize((16,16)))
icons["Bold"] = ImageTk.PhotoImage(Image.open(os.path.join(Base_dir,"Images","Bold.jpeg")).resize((16,16)))
icons["Italic"] = ImageTk.PhotoImage(Image.open(os.path.join(Base_dir,"Images","Italic.jpeg")).resize((16,16)))
icons["Underline"] = ImageTk.PhotoImage(Image.open(os.path.join(Base_dir,"Images","Underline.jpeg")).resize((16,16)))


# ================= Variables =================
tab_count = 0
font_size = 12
wrap_var = IntVar(value=1)

# ================= Helper =================
def update_status():
    tab = get_current_tab()
    if not tab:
        return
    line, column = tab.text.index(INSERT).split(".")
    status.config(text=f"File:{tab.file.split('/')[-1]if tab.file else 'Untitled'} | Line: {line} | Column: {column}")


def get_current_tab():
    tab_id = notebook.select()
    return notebook.nametowidget(tab_id)

def get_current_text():
    tab = get_current_tab()
    return tab.text



# ================= Tabs =================
def new_tab(event=None):
    global tab_count
    tab_count += 1

    tab = Frame(notebook)
    notebook.add(tab, text=f"Untitled {tab_count}")
    notebook.select(tab)

    text = Text(tab, wrap=WORD, undo=True)
    text.pack(side=LEFT, fill=BOTH, expand=True)
    text.tag_configure("bold", font=("Arial", font_size, "bold"))
    text.tag_configure("italic", font=("Arial", font_size, "italic"))
    text.tag_configure("underline", font=("Arial", font_size, "underline"))

    scroll = Scrollbar(tab, command=text.yview)
    scroll.pack(side=RIGHT, fill=Y)
    text.config(yscrollcommand=scroll.set)
    tab.text = text
    tab.file=None
    text.bind("<KeyRelease>", lambda e: update_status())
    text.bind("<ButtonRelease>", lambda e: update_status())

def close_tab(event=None):
    if len(notebook.tabs()) == 1:
        return
    notebook.forget(notebook.select())

# ================= File =================
def open_file():
    path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if path:
        text = get_current_text()
        with open(path, "r") as f:
            text.delete(1.0, END)
            text.insert(END, f.read())
        notebook.tab(get_current_tab(), text=path.split("/")[-1])

def open_folder():
    folder_path = filedialog.askdirectory(title="Select Folder")
    if not folder_path:
        return

    file_path = filedialog.askopenfilename(
        initialdir=folder_path,
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:
        text = get_current_text()
        with open(file_path, "r") as f:
            text.delete(1.0, END)
            text.insert(END, f.read())

        notebook.tab(get_current_tab(), text=file_path.split("/")[-1])


def save_file(event=None):
    text = get_current_text()
    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if path:
        with open(path, "w") as f:
            f.write(text.get(1.0, END))
        notebook.tab(get_current_tab(), text=path.split("/")[-1])

# ================= Edit =================
def undo(): get_current_text().edit_undo()
def redo(): get_current_text().edit_redo()
def cut():
    text = get_current_text()
    win.clipboard_clear()
    win.clipboard_append(text.get(SEL_FIRST, SEL_LAST))
    text.delete(SEL_FIRST, SEL_LAST)

def copy():
    text = get_current_text()
    win.clipboard_clear()
    win.clipboard_append(text.get(SEL_FIRST, SEL_LAST))

def paste():
    get_current_text().insert(INSERT, win.clipboard_get())

def clear_all():
    get_current_text().delete(1.0, END)

# ================= View Menu =================
status = Label(win, text="Ready", anchor=W)
status.pack(side=BOTTOM, fill=X)
show_status = IntVar(value=1)

def toggle_status():
    if show_status.get():
        status.pack(side=BOTTOM, fill=X)
    else:
        status.pack_forget()

def zoom_in():
    global font_size
    font_size += 1
    get_current_text().config(font=("Arial", font_size))

def zoom_out():
    global font_size
    if font_size > 6:
        font_size -= 1
        get_current_text().config(font=("Arial", font_size))

def zoom_reset():
    global font_size
    font_size = 12
    get_current_text().config(font=("Arial", font_size))

def toggle_wrap():
    text = get_current_text()
    if wrap_var.get():
        text.config(wrap=WORD)
    else:
        text.config(wrap=NONE)

def make_bold():
    text = get_current_text()
    try:
        text.tag_add("bold", SEL_FIRST, SEL_LAST)
    except:
        pass

def make_italic():
    text = get_current_text()
    try:
        text.tag_add("italic", SEL_FIRST, SEL_LAST)
    except:
        pass

def make_underline():
    text = get_current_text()
    try:
        text.tag_add("underline", SEL_FIRST, SEL_LAST)
    except:
        pass



# ================= Theme =================
def apply_theme(theme_name):
    if theme_name not in themes:
        return

    t = themes[theme_name]

    for tab_id in notebook.tabs():
        tab = notebook.nametowidget(tab_id)
        tab.text.config(
            bg=t["bg"],
            fg=t["fg"],
            insertbackground=t["insert"],
            selectbackground="#264f78",
            selectforeground="white"
        )
    status.config(bg=t["bg"], fg=t["fg"])

def change_theme():
    apply_theme(theme.get())




# ================= Menu =================
menubar = Menu(win)

# ================= File Menu =================
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="New Tab", accelerator="Ctrl+N",image=icons["new_file"],compound='left', command=new_tab)
file_menu.add_command(label="Open File", accelerator="Ctrl+O",image=icons["Open_file"],compound='left',command=open_file)
file_menu.add_command(label="Open Folder" , accelerator="Ctrl+F",image=icons["folder"],compound='left', command=open_folder)
file_menu.add_command(label="Save", accelerator="Ctrl+S",image=icons["file"],compound='left',command=save_file)
file_menu.add_command(label="Close Tab", accelerator="Ctrl+W",image=icons["close"],compound='left',command=close_tab)
file_menu.add_separator()
file_menu.add_command(label="Exit",image=icons["exit"],compound='left',command=win.destroy)
menubar.add_cascade(label="File", menu=file_menu)

# ================= Edit Menu =================
edit_menu = Menu(menubar, tearoff=0)
edit_menu.add_command(label="Undo", accelerator="Ctrl+Z",image=icons["undo"],compound='left', command=undo)
edit_menu.add_command(label="Redo", accelerator="Ctrl+Y",image=icons["redo"],compound='left', command=redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", accelerator="Ctrl+X",image=icons["cut"],compound='left', command=cut)
edit_menu.add_command(label="Copy", accelerator="Ctrl+C",image=icons["copy"],compound='left', command=copy)
edit_menu.add_command(label="Paste", accelerator="Ctrl+V",image=icons["paste"],compound='left', command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="Clear All",image=icons["clear"],compound='left', command=clear_all)
menubar.add_cascade(label="Edit", menu=edit_menu)

# ================= View Menu =================
view_menu = Menu(menubar, tearoff=0)

# ----- Zoom Submenu -----
zoom_menu = Menu(view_menu, tearoff=0)
zoom_menu.add_command(label="Zoom in", accelerator="Ctrl+Plus",image=icons["Zoom_in"],compound='left', command=zoom_in)
zoom_menu.add_command(label="Zoom out", accelerator="Ctrl+Minus",image=icons["Zoom_out"],compound='left', command=zoom_out)
zoom_menu.add_command(label="Restore default zoom", accelerator="Ctrl+0",image=icons["Zoom_restore"],compound='left',command=zoom_reset)

view_menu.add_cascade(label="Zoom",image=icons["Zoom"],compound='left', menu=zoom_menu)

# ----- Status Bar -----
view_menu.add_checkbutton(
    label="Status bar",
    variable=show_status,
    command=toggle_status
)

# ----- Word Wrap -----
view_menu.add_checkbutton(
    label="Word wrap",
    variable=wrap_var,
    command=toggle_wrap
)

menubar.add_cascade(label="View", menu=view_menu)


# ================= Theme Menu =================
themes = {
    "VS Code Dark": {
        "bg": "#1e1e1e",
        "fg": "#d4d4d4",
        "insert": "white"
    },
    "VS Code Light": {
        "bg": "#ffffff",
        "fg": "#333333",
        "insert": "black"
    },
    "Monokai": {
        "bg": "#272822",
        "fg": "#f8f8f2",
        "insert": "#f8f8f2"
    },
    "Dracula": {
        "bg": "#282a36",
        "fg": "#f8f8f2",
        "insert": "#f8f8f2"
    },
    "Solarized Dark": {
        "bg": "#002b36",
        "fg": "#93a1a1",
        "insert": "#93a1a1"
    },
    "Solarized Light": {
        "bg": "#fdf6e3",
        "fg": "#657b83",
        "insert": "#657b83"
    },
    "One Dark Pro": {
        "bg": "#282c34",
        "fg": "#abb2bf",
        "insert": "#abb2bf"
    },
    "Night Owl": {
        "bg": "#011627",
        "fg": "#d6deeb",
        "insert": "#d6deeb"
    },
    "Nord": {
        "bg": "#2e3440",
        "fg": "#d8dee9",
        "insert": "#d8dee9"
    },
    "Ayu Dark": {
        "bg": "#0f1419",
        "fg": "#e6e1cf",
        "insert": "#e6e1cf"
    },
    "Ayu Light": {
        "bg": "#fafafa",
        "fg": "#5c6166",
        "insert": "#5c6166"
    },
    "Gruvbox Dark": {
        "bg": "#282828",
        "fg": "#ebdbb2",
        "insert": "#ebdbb2"
    },
    "Tokyo Night": {
        "bg": "#1a1b26",
        "fg": "#c0caf5",
        "insert": "#c0caf5"
    }
}

theme = StringVar(value="Light")

theme_menu = Menu(menubar, tearoff=0)

for theme_name in themes:
    theme_menu.add_radiobutton(label=theme_name,variable=theme,value=theme_name,command=change_theme)
menubar.add_cascade(label="Theme", menu=theme_menu)
win.config(menu=menubar)


# ============== Right Click ================
popup = Menu(win, tearoff=0)

popup.add_command(label="Bold",image=icons["Bold"], compound='left', command=make_bold)
popup.add_command(label="Italic",image=icons["Italic"], compound='left', command=make_italic)
popup.add_command(label="Underline",image=icons["Underline"], compound='left', command=make_underline)

popup.add_separator()

popup.add_command(label="Undo", image=icons["undo"], compound='left', command=undo)
popup.add_command(label="Redo", image=icons["redo"], compound='left', command=redo)

popup.add_separator()

popup.add_command(label="Cut", image=icons["cut"], compound='left', command=cut)
popup.add_command(label="Copy", image=icons["copy"], compound='left', command=copy)
popup.add_command(label="Paste", image=icons["paste"], compound='left', command=paste)
def show_popup(event):
    popup.tk_popup(event.x_root,event.y_root) 
win.bind("<Button-3>",show_popup)

# ================= Shortcuts =================
win.bind("<Control-n>", new_tab)
win.bind("<Control-o>", lambda e: open_file())
win.bind("<Control-f>", lambda e: open_folder())
win.bind("<Control-s>", save_file)
win.bind("<Control-w>", close_tab)
win.bind("<Control-z>", lambda e: undo())
win.bind("<Control-y>", lambda e: redo())
win.bind("<Control-x>", lambda e: cut())
win.bind("<Control-c>", lambda e: copy())
win.bind("<Control-v>", lambda e: paste())

# ================= Start =================
new_tab()
apply_theme(theme.get())
win.mainloop()
