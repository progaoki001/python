import tkinter as tk


class AppMain:
    def __init__(self):

        # main window
        self.root = tk.Tk()
        self.root.title('testToDo')
        self.root.geometry('300x500')
        # file menu
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="save", command=self.file_save)
        self.file_menu.add_command(label="road", command=self.file_road)
        self.menu_bar.add_cascade(label="file", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)

        # task input area
        self.frame1 = InputArea(self.root, 'Task', 20)
        # dead line input area
        self.frame2 = InputArea(self.root, 'Dead Line', 4)
        self.frame2.entry.insert(tk.END, "ex)200325")
        # priority & add Button
        self.frame3 = PriorityArea(self.root)
        # inner title TO DO LIST
        self.frame4 = tk.Label(self.root, text='TO DO LIST')
        self.frame4.pack()
        # To Do List Area
        self.frame5 = ToDoArea(self.root)
        self.frame5.pack()
        # sort & delete button
        self.frame6 = SortDelete(self.root)
        self.frame6.pack()
        self.frame6.click_sort_btn = self.click_sort_btn  # handle
        self.frame6.click_delete_btn = self.click_delete_btn  # handle
        # for handle
        self.frame3.click_add_btn = self.click_add_btn
        # for get text
        self.task_text = None
        self.dead_line_date = None
        # for get priority
        self.priority = None
        # for push To DO List
        self.to_do_list = []
        self.priority_char = None
        self.to_do_list_display = []
        # for check button
        self.check = []  # bool box
        self.check_button = []
        # for initialize check button
        self.check_button_init = 0
        self.check_button_list = []

    # for Add Button
    def click_add_btn(self):

        # initialize check button
        if self.check_button_init != 0:
            for i in range(len(self.check_button_list)):
                self.check_button_list[i].pack_forget()

        # get Input Area Text
        self.task_text = self.frame1.entry.get()
        self.frame1.entry.delete(0, 'end')
        self.dead_line_date = self.frame2.entry.get()
        self.frame2.entry.delete(0, 'end')
        self.priority = self.frame3.val.get()
        self.to_do_list.append([self.priority, self.dead_line_date, self.task_text])
        self.check_button_init += len(self.to_do_list)
        self.display()

    # 画面表示 ToDoList
    def display(self):
        #  表示画面の初期化
        if self.check_button_init != 0:
            for i in range(len(self.check_button_list)):
                self.check_button_list[i].pack_forget()

        if self.priority == 0:
            self.priority_char = 'C'
        elif self.priority == 1:
            self.priority_char = 'B'
        elif self.priority == 2:
            self.priority_char = 'A'
        else:
            self.priority_char = None

        # 全部記入しているか？未完成
        if self.task_text is None or self.dead_line_date is None:
            print('miss')  # for debug
        else:
            self.to_do_list_display.append([self.priority_char + '_' + self.dead_line_date + '_' + self.task_text])
            # 初期化
            self.priority_char = None
            self.task_text = None
            self.dead_line_date = None

        # set display check button
        self.check.append([]*len(self.to_do_list))
        self.check_button_list.append([]*len(self.to_do_list))
        for i in range(len(self.to_do_list)):
            self.check[i] = tk.BooleanVar()
            self.check_button = tk.Checkbutton(self.frame5, variable=self.check[i], text=self.to_do_list_display[i])
            self.check_button_list[i] = self.check_button
            self.check_button_list[i].pack()

    def click_sort_btn(self):
        self.to_do_list.sort(reverse=True)
        print(self.to_do_list)
        self.display()  # ソート後のto_do_listが反映されない

    def click_delete_btn(self):
        self.to_do_list = []
        self.display()

    def file_save(self):
        print("save")

    def file_road(self):
        print("road")

    def mainloop(self):
        self.root.mainloop()


class InputArea(tk.Frame):

    def __init__(self, master=None, text='', padx=None):
        super(InputArea, self).__init__(master)

        self.frame = tk.Frame(master)
        self.frame.pack()
        self.label = tk.Label(self.frame, text=text)
        self.label.grid(row=0, column=0, padx=padx)
        self.entry = tk.Entry(self.frame)
        self.entry.grid(row=0, column=1)


class PriorityArea(tk.Frame):

    def __init__(self, master=None):
        super(PriorityArea, self).__init__(master)

        self.frame = tk.Frame(master)
        self.frame.pack()
        self.label = tk.Label(self.frame, text='Priority')
        self.label.place(x=6, y=5)
        # radio button
        self.item = ['A', 'B', 'C']
        self.val = tk.IntVar()
        self.click_add_btn = None  # for handle

        for i in range(len(self.item)):
            if i == 0:
                tk.Radiobutton(self.frame, value=2, variable=self.val, text=self.item[i])\
                    .grid(row=1, column=i, padx=8, pady=30)
            if i == 1:
                tk.Radiobutton(self.frame, value=1, variable=self.val, text=self.item[i])\
                    .grid(row=1, column=i, padx=8, pady=30)
            if i == 2:
                tk.Radiobutton(self.frame, value=0, variable=self.val, text=self.item[i])\
                    .grid(row=1, column=i, padx=8, pady=30)

        # set AddButton
        self.button = tk.Button(self.frame, text='Add', command=self._click_add_btn)
        self.button.grid(row=1, column=3, padx=10)

    # for handle
    def _click_add_btn(self):
        if self.click_add_btn:
            self.click_add_btn()  # Why used 'child function'?


class ToDoArea(tk.Frame):

    def __init__(self, master=None):
        super(ToDoArea, self).__init__(master)
        self.frame = tk.Frame(master)
        self.frame.pack()


class SortDelete(tk.Frame):

    def __init__(self, master=None):
        super(SortDelete, self).__init__(master)

        self.frame = tk.Frame(master)
        self.frame.pack()
        self.button = tk.Button(self.frame, text='Sort', command=self._click_sort_btn)
        self.button.grid(row=0, column=0, padx=10, pady=10)
        self.button2 = tk.Button(self.frame, text='Del', command=self._click_delete_btn)
        self.button2.grid(row=0, column=1, padx=10, pady=10)
        self.click_sort_btn = None  # for handle
        self.click_delete_btn = None  # for handle

    # for handle
    def _click_sort_btn(self):
        if self.click_sort_btn:
            self.click_sort_btn()

    # for handle
    def _click_delete_btn(self):
        if self.click_delete_btn:
            self.click_delete_btn()


app = AppMain()
app.mainloop()
