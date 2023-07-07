from tkinter import *
from emoji_translate.emoji_translate import Translator

def translate_to_emoji():
    input_text = input_entry.get()
    emo = Translator(exact_match_only=False, randomize=True)
    translated_text = emo.emojify(input_text)
    output_label.config(text=translated_text)

# ایجاد پنجره اصلی
root = Tk()
root.title("Text to Emoji Translator")

# ایجاد ویجت‌ها
input_label = Label(root, text="Enter text:")
input_label.pack()
input_entry = Entry(root, width=50)
input_entry.pack()

translate_button = Button(root, text="Translate to Emoji", command=translate_to_emoji)
translate_button.pack()

output_label = Label(root, text="")
output_label.pack()

# شروع حلقه رویداد
root.mainloop()
