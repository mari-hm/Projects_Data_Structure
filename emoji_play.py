import tkinter as tk
import random

word_to_emoji = {
    'دوست دارم': '❤️',
    'اتوبوس': '💋♴🅾️',
    'سیب زمینی': '🌎🍎',
    'تهران': '🍖🔚',
    'آفتاب گردان': ' 🔄☀️',
    'بالن': ' 🔛⚽',
    'شیر کاکائو': '🍫🍼',
}

score = 0
current_word = ''

def generate_puzzle():
    global current_word
    random_index = random.randint(0, len(word_to_emoji) - 1)
    current_word = list(word_to_emoji.keys())[random_index]
    return current_word, word_to_emoji[current_word]

def check_guess():
    guess = guess_entry.get()
    if guess.lower() == current_word.lower():
        result_label.config(text='آفرین!', fg='green')
        global score
        score += 1
    else:
        result_label.config(text=f'اوه اشتباهه، عبارت درست {current_word}.', fg='red')
    update_score()

def update_score():
    score_label.config(text=f'امتیاز: {score}')

def play_game():
    global current_word
    current_word, emoji = generate_puzzle()
    emoji_label.config(text=emoji)
    guess_entry.delete(0, tk.END)
    guess_entry.focus()

def quit_game():
    root.destroy()

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("Emoji Guessing Game")

# ایجاد ویجت‌ها
emoji_label = tk.Label(root, font=('Arial', 48), relief=tk.RAISED, width=8, height=4)
emoji_label.pack(pady=10)

guess_entry = tk.Entry(root, font=('Arial', 16))
guess_entry.pack(pady=5)
guess_entry.bind('<Return>', lambda event: check_guess())

check_button = tk.Button(root, text='بررسی', font=('Arial', 16), command=check_guess)
check_button.pack(pady=5)

result_label = tk.Label(root, font=('Arial', 16))
result_label.pack(pady=5)

score_label = tk.Label(root, font=('Arial', 16))
score_label.pack(pady=5)
update_score()

play_button = tk.Button(root, text='شروع بازی جدید', font=('Arial', 16), command=play_game)
play_button.pack(pady=5)

quit_button = tk.Button(root, text='خروج', font=('Arial', 16), command=quit_game)
quit_button.pack(pady=5)

play_game()

# شروع حلقه رویداد
root.mainloop()
