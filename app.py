from tkinter import *
from tkinter import ttk

LIST_OF_WORDS = ['avoid', 'fallacious', 'visit', 'command', 'curve', 'wrist', 'fabulous', 'grip', 'time', 'puny',
                 'discovery', 'valuable', 'permissible', 'effect', 'approval', 'cook', 'settle', 'dazzling',
                 'courageous', 'pray', 'program', 'unknown', 'stranger', 'numerous', 'ball', 'sweltering', 'live',
                 'well-made', 'wretched', 'understood', 'flower', 'baby', 'sheep', 'sharp', 'direful', 'abnormal',
                 'waves', 'lake', 'place', 'ragged', 'calm', 'tacit', 'hateful', 'head', 'buzz', 'blind', 'encouraging'
    , 'expand', 'likeable', 'stupendous', 'volleyball', 'vengeful', 'rough', 'summer', 'glistening'
    , 'boring',
                 'available',
                 'blushing', 'adjoining', 'wrathful', 'fancy', 'tree', 'shelf', 'badge', 'strap', 'stem', 'pet',
                 'hulking',
                 'jog', 'depend', 'scare', 'naughty', 'open', 'launch', 'writing', 'unable', 'thought', 'gray', 'blink',
                 'wakeful', 'exercise', 'pets', 'tooth', 'reproduce', 'egg', 'efficacious', 'mind', 'obnoxious',
                 'chilly', 'want', 'scream', 'question', 'acoustics', 'store', 'flowers', 'curl', 'jail', 'subsequent',
                 'dysfunctional', 'victorious']


class App():

    def __init__(self):
        # Creates the root window
        self.root = Tk()
        self.root.title("Typing Speed Processor")
        self.root.geometry("800x500")
        self.root.configure(bg="#F1EEE9", highlightthickness=0, pady=10, padx=70)

        # Creating a text widget and a scroll bar
        self.text = Text(self.root, width=70, height=10, pady=10, padx=20)
        self.text.insert('1.0', " ".join([item for item in LIST_OF_WORDS]))
        self.text['state'] = 'disabled'
        self.text.tag_add("format", "1.0", "end")
        self.text.tag_configure('format', font=('TkFixedFont', 20), relief='raised', spacing2=5, wrap="word")
        self.text.grid(column=0, row=0)

        ys = ttk.Scrollbar(self.root, orient='vertical', command=self.text.yview)
        self.text['yscrollcommand'] = ys.set
        ys.grid(column=1, row=0, sticky='ns')


        # Creates the entry text area
        self.entry_text_widget = Text(self.root, width=50, height=5, pady=10, padx=20, font=('TkFixedFont"', 15))
        self.entry_text_widget.grid(column=0, row=1, pady=30)
        self.entry_text_widget.tag_add("entry_format", "1.0", "end")
        self.entry_text_widget['state'] = 'disabled'

        # Creates the start Button
        start_button = ttk.Button(self.root, text="start!", command=self.start)
        start_button.grid(column=0, row=2)

        self.word_count_label = ttk.Label(self.root, text="")
        self.word_count_label.grid(column=0, row=3)
        self.running = False

        self.root.mainloop()

    def disable(self):
        """Stops the program and counts the number of words entered"""
        self.running = False
        self.entry_text_widget['state'] = 'disabled'
        typed_text = self.entry_text_widget.get('1.0', 'end')
        user_text_list = typed_text.split()

        number_of_words = 0
        text_widget_words = self.text.get('1.0', 'end')

        for word in user_text_list:
            if word in text_widget_words:
                number_of_words += 1

        self.word_count_label.config(text=f'Your typing speed is: {number_of_words} words per minute')


    def highlight(self):
        """ highlights the text as it being typed """

        if self.running:
            typed_text = self.entry_text_widget.get('1.0', 'end')
            self.text.tag_config("red_tag", foreground="red")

            for word in typed_text.split():
                offset = '+%dc' % len(word)  # +5c (5 chars)
                try:
                    pos_start = self.text.search(word, "1.0", END)
                    pos_end = pos_start + offset
                    self.text.tag_add('red_tag', pos_start, pos_end)

                    self.text.see('red_tag.last + 5 chars') # Moves the view to the end of the highlighted word
                except:
                    pass
            self.root.after(200, self.highlight)

    def start(self):
        """ starts the speed typing program"""
        if self.running:
            self.entry_text_widget.focus_set()
        else:
            self.running = True
            self.text.see("1.0")
            self.word_count_label.config(text="")
            self.text.tag_delete("red_tag")
            self.entry_text_widget['state'] = 'normal'
            self.entry_text_widget.delete('1.0', END)
            self.entry_text_widget.focus_set()
            self.highlight()
            self.root.after(6000, self.disable)



if __name__ == "__main__":
    app = App()
