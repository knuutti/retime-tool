from tkinter import *
import pyperclip
import calculate
import parse
import format

def main():

    def paste_start_frame():

        paste_frame(start_cmt, start_frame)

        return

    def paste_end_frame():

        paste_frame(end_cmt, end_frame)
        
        return

    def paste_frame(cmt, frame):
        clipboard = pyperclip.paste()

        if clipboard.isnumeric():

            frame_value = int(clipboard)
            frame.set(frame_value)
            cmt.set(frame.get() / fps.get())

        else:

            cmt.set(parse.parse_cmt(clipboard))
            frame.set(calculate.get_frame(cmt.get(), fps.get()))

        update_values()

        return

    def copy_slygold():
        
        pyperclip.copy(slygolds_time_label.cget('text'))
        
        return

    def update_values(*args):

        # One of the frames is missing
        if start_frame.get() == -1 or end_frame.get() == -1:
            slygolds_time_label.config(text='-')
            total_time_label.config(text='-')

            if start_frame.get() == -1:
                start_frame_label.config(text='-')
            else:
                start_frame_label.config(text=start_frame.get())
            if end_frame.get() == -1:
                end_frame_label.config(text='-')
            else:
                end_frame_label.config(text=end_frame.get())

        # Computing the total time
        else:
            modifier_value = parse.get_modifier_value(modifier.get())

            start_frame.set(calculate.get_frame(start_cmt.get(), fps.get()))
            start_frame_label.config(text=start_frame.get())

            end_frame.set(calculate.get_frame(end_cmt.get(), fps.get()))
            end_frame_label.config(text=end_frame.get())

            total_time.set((end_frame.get()-start_frame.get())/fps.get() + modifier_value)
            total_time_label.config(text=format.format_total_time(total_time.get()))
            slygolds_time_label.config(text=format.format_slygolds_time(total_time.get()))

        return

    # Clear all the data (except FPS)
    def clear_all():
        start_frame.set(-1)
        end_frame.set(-1)
        modifier.set('')
        start_cmt.set(.0)
        end_cmt.set(.0)

        update_values()

        return


    # Configuring the window
    window = Tk()
    window.title('Speedrun Retime Tool')
    window.resizable(0,0)
    window.attributes('-topmost', True) # window always on top
    window.configure(background = '#121a22')
    #window.iconbitmap(r'slygolds.ico')

    window.bind_all('<1>', lambda event:event.widget.focus_set()) # entries lose focus when clicked elsewhere

    fps_options = [
        25,
        30,
        50,
        60
        # TODO 
        # could make this to read values from 
        # settings file instead of hard coding
    ]
    start_frame = IntVar()
    start_cmt = DoubleVar()
    end_frame = IntVar()
    end_cmt = DoubleVar()
    fps = IntVar()
    modifier = StringVar()
    total_time = DoubleVar()

    # Defining the variables
    start_frame.set(-1)
    end_frame.set(-1)
    fps.set(60) 
    modifier.set('')

    # Whenever a value changes, update the total time
    fps.trace_add('write', update_values)
    modifier.trace_add('write', update_values)

    # Defining the FPS selection widget (dropdown menu)
    fps_dropdown_menu = OptionMenu(window, fps, *fps_options)
    fps_dropdown_menu.configure(font='Calibri 15', border=0, indicatoron=0, width=5, background='white', height=1)

    # Defining start/end frame labels
    start_frame_label = Label(window, font='Calibri 15', width=20, background='white', justify=LEFT)
    end_frame_label = Label(window, font='Calibri 15', width=20, background='white', justify=LEFT)

    # Defining modifier entry
    modifier_entry = Entry(window, width=10, font='Calibri 15', background='white', justify=CENTER, textvariable=modifier)

    # Defining headers for different sections
    start_frame_header_label = Label(window, text = 'START FRAME', font = 'Calibri 15 bold', width = 12, background = '#1e2b3a', foreground = 'white', relief=SUNKEN)
    end_frame_header_label = Label(window, text = 'END FRAME', font = 'Calibri 15 bold', width = 12, background = '#1e2b3a', foreground = 'white', relief=SUNKEN)
    fps_header_label = Label(window, text = 'FPS', font = 'Calibri 15 bold', width = 12, background = '#1e2b3a', foreground = 'white', relief=SUNKEN)
    modifier_header_label = Label(window, text = 'MODIFIER', font = 'Calibri 15 bold', width = 12, background = '#1e2b3a', foreground = 'white', relief=SUNKEN)
    total_time_header_label = Label(window, text='TOTAL TIME', background='#1e2b3a', font='Calibri 15 bold', foreground='white', relief=SUNKEN)
    total_time_label = Label(window, background='white', font='Calibri 30', foreground='black', borderwidth=10, text='0m 00s')
    slygolds_header_label = Label(window, text = 'SLYGOLDS', font = 'Calibri 15 bold', width = 12, background = '#955707', foreground = 'white', relief=SUNKEN)
    slygolds_time_label = Label(window, font = 'Calibri 15', width = 12, background = 'white', text='00:00.00')

    # Defining some extra frames to make the window look nice UwU
    empty_frame1 = Frame(window, height = 10, background = '#121a22')
    empty_frame2 = Frame(window, height = 10, background = '#121a22')
    empty_frame3 = Frame(window, height = 10, background = '#121a22')
    empty_frame4 = Frame(window, height = 10, background = '#121a22')
    empty_frame5 = Frame(window, height = 10, background = '#121a22')
    empty_frame6 = Frame(window, height = 10, background = '#121a22')

    # Buttons
    start_frame_button = Button(window, text = 'PASTE', font = 'Calibri 15 bold', background = '#085097', foreground = 'white', width = 8, command=paste_start_frame)
    end_frame_button = Button(window, text = 'PASTE', font = 'Calibri 15 bold', background = '#085097', foreground = 'white', width = 8, command=paste_end_frame)
    slygolds_button = Button(window, text = 'COPY', font = 'Calibri 15 bold', background = '#085097', foreground = 'white', width = 8, command=copy_slygold)
    clear_all_button = Button(window, text = 'CLEAR ALL', font = 'Calibri 15 bold', background = '#085097', foreground = 'white', width = 8, command=clear_all)

    ### PACKING WIDGETS INTO THE GRID ###

    empty_frame1.grid(row=1, column=1, sticky='ew')

    fps_header_label.grid(row=2, column=1, padx=7, pady=3, ipadx=5, ipady=5)
    fps_dropdown_menu.grid(row=2, column=2, padx=7, pady=3)
    modifier_header_label.grid(row=2, column=3, padx=7, pady=3, ipadx=5, ipady=5)
    modifier_entry.grid(row=2, column=4, padx=7, pady=7, ipady=5)

    empty_frame2.grid(row=3)

    start_frame_header_label.grid(row=4, column=1, padx=7, pady=3, ipadx=5, ipady=5)
    start_frame_label.grid(row=4, column=2, columnspan=2, padx=7, pady=3, ipadx=5, ipady=5)
    start_frame_button.grid(row=4, column=4, padx=7, pady=3, sticky='ew')
    end_frame_header_label.grid(row=5,column=1, padx=7, pady=3, ipadx=5, ipady=5)
    end_frame_label.grid(row=5, column=2, columnspan=2, padx=7, pady=3, ipadx=5, ipady=5)
    end_frame_button.grid(row=5, column=4, padx=7, pady=3, sticky='ew')

    empty_frame3.grid(row=6, column=1)

    total_time_header_label.grid(row=7, column=1, columnspan=4, sticky='ew', padx=7, pady=3)
    total_time_label.grid(row=8, column=1, columnspan=4, sticky='ew', padx=8, pady=3, ipadx=5, ipady=5)

    empty_frame4.grid(row=9, column=1)

    if True:
        # TODO
        # Add option in settings file to disable showing this section
        slygolds_header_label.grid(row=10,column=1, padx=7, pady=3, ipadx=5, ipady=5)
        slygolds_time_label.grid(row=10,column=2,columnspan=2, padx=7, pady=3, ipadx=5, ipady=5, sticky='ew')
        slygolds_button.grid(row=10,column=4, padx=7, pady=3, sticky='ew')
        empty_frame5.grid(row=11,column=1)

    clear_all_button.grid(row=12,column=1,columnspan=4, sticky='ew', padx=7, pady=3)

    empty_frame6.grid(row=13, column=1)

    update_values()

    ### MAINLOOP ###
    window.mainloop()

    return



if __name__ == '__main__':
    main()    