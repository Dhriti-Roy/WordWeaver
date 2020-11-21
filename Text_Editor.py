import tkinter as tk                                                                    
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os
import datetime

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('TEXT EDITOR')

def func():
    pass
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#                                                MAIN MENU
#                                               o==========o

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


main_menu = tk.Menu()

#                                                 Tool bar >>

tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill = tk.X)

# ^^                                              Buttons:

# 1.>> new file button

new_icon = tk.PhotoImage( file = 'images/new.png')
new_btn = ttk.Button(tool_bar, image=new_icon)
new_btn.grid(row=0, column=1, padx=3)

# 2.>> open file button

open_icon = tk.PhotoImage( file = 'images/open.png')
open_btn = ttk.Button(tool_bar, image=open_icon)
open_btn.grid(row=0, column=2, padx=3)

# 3.>> undo button

undo_icon = tk.PhotoImage( file = 'images/undo.png')
undo_btn = ttk.Button(tool_bar, image=undo_icon)
undo_btn.grid(row=0, column=3, padx=3)

# 4.>> redo button

redo_icon = tk.PhotoImage( file = 'images/redo.png')
redo_btn = ttk.Button(tool_bar, image=redo_icon)
redo_btn.grid(row=0, column=4, padx=3)


# 5.>> font box

font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar,width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=5, padx=5)

# 6.>> size box

size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar,width=14, textvariable = size_var, state = 'readonly')
font_size['values'] = tuple(range(8,81))
font_size.current(4)
font_size.grid(row=0, column=6, padx=5)  

# 7.>> bold button

bold_icon =tk.PhotoImage(file ='images/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=7, padx=3)

# 8.>> italic button

italic_icon =tk.PhotoImage(file ='images/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=8, padx=3)

# 9.>> underline button

underline_icon =tk.PhotoImage(file ='images/underline.png')
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=9, padx=3)

# 10.>> font color button

font_color_icon= tk.PhotoImage(file='images/colour.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=10, padx=3)

# 11.>> align left

align_left_icon = tk.PhotoImage(file='images/align-left .png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0,column=11,padx=3)

# 12.>> align center

align_center_icon = tk.PhotoImage(file='images/align-centery.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0,column=12 ,padx=3)

# 13.>> align right

align_right_icon = tk.PhotoImage(file='images/align-right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0,column=13 ,padx=3)

# 14.>> highlight

highlight_icon= tk.PhotoImage(file='images/highlighter2.png')
highlight_btn = ttk.Button(tool_bar, image=highlight_icon)
highlight_btn.grid(row=0, column=14, padx=3)

# 15. date/time button

date_icon= tk.PhotoImage(file='images/calendar.png')
date_btn = ttk.Button(tool_bar, image=date_icon)
date_btn.grid(row=0, column=15, padx=3)


#                                                  TEXT EDITOR 


text_editor = tk.Text(main_application , undo=True)
text_editor.config(wrap='word', relief=tk.FLAT)

#                                                   Scroll Bar >>

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)



#                                            Functionality

# 1.>> font & size  functionality

current_font_family ='Arial'
current_font_size = 12

def change_font(main_application):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))
font_box.bind("<<ComboboxSelected>>", change_font)

def change_size(main_application):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))
font_size.bind("<<ComboboxSelected>>", change_size)


# 2.>>  bold button functionality

def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
bold_btn.configure(command=change_bold)


# 3.>> italic button functionality

def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'roman'))
italic_btn.configure(command=change_italic)


# 4.>> underline functionality

def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline']==1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
underline_btn.configure(command=change_underline)


# 5.>> font color functionality

def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
font_color_btn.configure(command=change_font_color)


# 6.>> left align functionality

def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')
align_left_btn.configure(command=align_left)    


# 7.>> center align functionality

def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')
align_center_btn.configure(command=align_center)    


# 8.>> right align functionality

def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')
align_right_btn.configure(command=align_right)  



text_editor.configure(font=('Arial',12))



#                                               Status Bar >>

status_bar = ttk.Label(main_application, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)
text_change = False

def changed(even=None):
    global text_change
    if text_editor.edit_modified():
        text_change = True
        words = len(text_editor.get(1.0,'end-1c').split())
        characters = len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text=f'Character : {characters} Words : {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>', changed)


#                                         MAIN MENU FUNCTIONALITY

url = ''

#                                        ^^  1. FILE FUNCTIONALITY :

#                                        >> new file functionality :

def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)

new_btn.configure(command=new_file)    

# open file functionality :
def open_file(even=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'),('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))        
 


#                                       >> open folder functionality:

open_btn.configure(command=open_file)    

def open_folder(even=None):
    global url
    url =filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Folder', filetypes=(('Text Folder', '*.txt'),('All floders', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))        


#                                          >> save functionality :

def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url,'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt' , filetypes=(('Text File', '*.txt'),('All files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return        


#                                          >> save as functionality :

def save_as_file(event=None):
    global url
    try:
        if url:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt' , filetypes=(('Text File', '*.txt'),('All files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt' , filetypes=(('Text File', '*.txt'),('All files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()    
    except:
        return        


#                                           >>  exit functionality :

def exit_file(event=None):
    global url, text_change
    try:
        if text_change:
            msgbox = messagebox.askyesnocancel('Warning','Do you want to save current file ?')
            if msgbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url,'w', encoding='utf-8')as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt' , filetypes=(('Text File', '*.txt'),('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif msgbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return                     
exit_icon = tk.PhotoImage(file='images/logout.png')

        
#                                        >>  new window functionality :

def new_window():
    pass


#                                               FILE MENU :

file_menu= tk.Menu(main_menu,tearoff=0)
file_menu.add_command(label='New File' , command=new_file , accelerator='Ctrl+N' )
file_menu.add_command(label='New Window', command=new_window , accelerator='Ctrl+Shift+N')
file_menu.add_separator()
file_menu.add_command(label='Open File', command=open_file , accelerator='Ctrl+O')
file_menu.add_command(label='Open Folder', command=open_folder, accelerator='Ctrl+k')
file_menu.add_separator()
file_menu.add_command(label='Save File', command= save_file , accelerator='Ctrl+S')
file_menu.add_command(label='Save As', command=save_as_file , accelerator='Ctrl+Shift+S')
file_menu.add_separator()
file_menu.add_command(label='Exit ', accelerator='Ctrl+Q' , image= exit_icon, compound=tk.RIGHT, command=exit_file)

main_menu.add_cascade(label='File', menu=file_menu)




#                                 ^^  2. EDIT MENU & EDIT FUNCTIONALITY :
 
edit_menu= tk.Menu(main_menu, tearoff=0)
edit_menu.add_command(label='Undo', command=lambda:text_editor.event_generate("<Control z>"), accelerator='Ctrl+Z' )
edit_menu.add_command(label='Redo', command=lambda:text_editor.event_generate("<Control y>"), accelerator='Ctrl+Y' )
edit_menu.add_separator()
edit_menu.add_command(label='Cut', command=lambda:text_editor.event_generate("<Control x>"), accelerator='Ctrl+X' )
edit_menu.add_command(label='Copy', command=lambda:text_editor.event_generate("<Control c>"), accelerator='Ctrl+C' )
edit_menu.add_command(label='Paste', command=lambda:text_editor.event_generate("<Control v>"), accelerator='Ctrl+V' )
main_menu.add_cascade(label='Edit', menu=edit_menu, accelerator='Ctrl+N' )
edit_menu.add_separator()
edit_menu.add_command(label='Clear All', command=lambda:text_editor.delete(1.0, tk.END), accelerator='Ctrl+Alt+X' )


#                                    ^^ 3.  VIEW FUNCTIONALITY :

#                                    >> replace/find functionality :

def replace_func(event=None):
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    def cancel_replace():
        find_dialogue.destroy()
    
    find_dialogue= tk.Toplevel()
    find_dialogue.geometry('450x200+500+200')
    find_dialogue.title('Replace')
    find_dialogue.resizable(0,0)
 
    find_frame = ttk.LabelFrame(find_dialogue)
    find_frame.pack(pady=10)

    text_find_label = ttk.Label(find_frame, text='Word :      ')
    text_replace_label = ttk.Label(find_frame, text='Replace word : ')

    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    replace_button = ttk.Button(find_frame, text='Replace', command= replace)
    find_replace_button = ttk.Button(find_frame, text='Find', command= search_word)
    cancel_replace_button = ttk.Button(find_frame, text='Cancel', command= cancel_replace)

    text_find_label.grid(row=0, column=0, padx=4 , pady=4)
    text_replace_label.grid(row=1, column=0, padx=4 , pady=4)
    
    find_input.grid(row=0, column=1, padx=4 , pady=4)
    replace_input.grid(row=1, column=1, padx=4 , pady=4)

    replace_button.grid(row=2, column=2, padx=4 , pady=4)
    find_replace_button.grid(row=0, column=2, padx=4, pady=4)
    cancel_replace_button.grid(row=3, column=2, padx=4 , pady=4)

    find_dialogue.mainloop()



#                                 >> search word functionality :

def search_word(event=None):

    def search():
        word = search_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos , stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match',foreground='purple', background='pink')

    def cancel_search():
        search_dialogue.destroy()

    search_dialogue= tk.Toplevel()
    search_dialogue.geometry('400x150+500+200')
    search_dialogue.title('Find')
    search_dialogue.resizable(0,0)
    search_frame = ttk.LabelFrame(search_dialogue)
    search_frame.pack(pady=20) 
    text_search_label = ttk.Label(search_frame, text='Enter Word :')
    search_input = ttk.Entry(search_frame, width=30)
    search_button = ttk.Button(search_frame, text='Find', command= search)
    cancel_search_button = ttk.Button( search_frame, text='Cancel', command= cancel_search)
    text_search_label.grid(row=0, column=0, padx=4 , pady=4)
    search_input.grid(row=1, column=0, padx=4 , pady=4)
    search_button.grid(row=2, column=1, padx=1 , pady=1)
    cancel_search_button.grid(row=2 , column=2 , padx=1 , pady=1)
    search_dialogue.mainloop()
    
highlight_btn.configure(command=search_word)      


#                                      >> date functionality :

def date():
    x = datetime.datetime.now()
    msg_dialogue = tk.Tk()
    msg_dialogue.geometry('250x100+60+60')
    msg_dialogue.title('Date/Time')
    msg_dialogue.resizable(0,0)
    msg_frame = ttk.LabelFrame(msg_dialogue)
    msg_frame.pack(pady=20)
    msg_label = ttk.Label(msg_frame, text=x)
    msg_label.grid(row=0, column=0, padx=4 , pady=4)
    msg_dialogue.mainloop()
date_btn.configure(command=date)
   

#                                        >> go to lines  functionality

def go_to_line():
    
    def go_to():
        global url
        if url:
            with open(url, 'a+') as f:
                f.seek(0)
                f1 = f.readlines()
                line_no = int (goto_input.get())
                i = 0
                while i < len(f1):
                    print(f1[line_no])
                    break

    def cancel_goto():
        goto_dialogue.destroy()

    goto_dialogue = tk.Tk()
    goto_dialogue.geometry('500x170+500+200')
    goto_dialogue.title('Go To Line')
    goto_dialogue.resizable(0,0)
    goto_frame = ttk.LabelFrame(goto_dialogue)
    goto_frame.pack(pady=15)
    goto_search_label = ttk.Label(goto_frame, text='Enter Line Number : ')
    goto_input = ttk.Entry(goto_frame, width=30)
    goto_button = ttk.Button(goto_frame, text='Go To Line', command= go_to)
    goto_button.grid(row=2, column=1, padx=3, pady=0)
    goto_button = ttk.Button(goto_frame, text='Cancel', command=cancel_goto)
    goto_button.grid(row=2, column=2, padx=3 ,pady=0)
    goto_search_label.grid(row=0, column=0, padx=4 , pady=4)
    goto_input.grid(row=1, column=0, padx=4 , pady=4)

    goto_dialogue.mainloop()



#                                             VIEW MENU :

view_menu= tk.Menu(main_menu, tearoff=0)
view_menu.add_command(label='Go To', command= go_to_line, accelerator='Ctrl+G')
view_menu.add_command(label='Select All', command=lambda:text_editor.event_generate("<Control a>") , accelerator='Ctrl+A')
view_menu.add_separator()
view_menu.add_command(label='Search', command= search_word, accelerator='Ctrl+Shift+F')
view_menu.add_command(label='Replace Word', command= replace_func, accelerator='Ctrl+Shift+R')
view_menu.add_separator()
view_menu.add_command(label='Date', command= date, accelerator='F5')
main_menu.add_cascade(label='View', menu=view_menu)



#                                 4. ^^  COLOR THEME : 

light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')

color_theme= tk.Menu(main_menu, tearoff=0)

theme_choice= tk.StringVar()
color_icons = (light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)


# >>   COLOR CODE

color_dict = {
    'Light Default' : ('#000000','#ffffff'),
    'Light Plus' : ('#474747','#e0e0e0'),
    'Dark' : ('#c4c4c4','#2d2d2d'),
    'Red' : ('#2d2d2d','#ffe8e8'),
    'Monokai' : ('#d3b774','#474747'),
    'Night Blue' : ('#ededed','#6b9dc2')
}

# >> change theme functionality

def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)
count = 0
for i in color_dict:
    color_theme.add_radiobutton(label = i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command=change_theme)
    count +=1


main_menu.add_cascade(label='Color Theme', menu=color_theme)


#                                             ^^ ABOUT :

#                                      >> About functionality :

def aboutus():
    about_dialogue= tk.Toplevel()
    about_dialogue.geometry('150x100+60+60')
    about_dialogue.title('About us')
    about_dialogue.resizable(0,0)
    about_frame = ttk.LabelFrame(about_dialogue, text='About us')
    about_frame.pack(pady=20)
    about_label = ttk.Label(about_frame, text='Name - Dhriti Roy ')
    about_label.grid(row=0, column=0, padx=4 , pady=4)
    about_dialogue.mainloop()

#                                      About Menu:

about_menu= tk.Menu(main_menu, tearoff=0)
about_menu.add_command(label='About', command=aboutus)
main_menu.add_cascade(label='About', menu=about_menu)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

main_application.config(menu=main_menu)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#                                   Bind shortcut keys:

main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-Shift-n>", new_window)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-k>", open_folder)
main_application.bind("<Control-s>", save_file )
main_application.bind("<Control-Shift-s>", save_as_file )
main_application.bind("<Control-q>", exit_file )
main_application.bind("<Control-Shift-f>", search_word )
main_application.bind("<Control-Shift-r>", replace_func )

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

main_application.mainloop()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
