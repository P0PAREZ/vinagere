import tkinter as tk
import pyperclip

def vigenere_cipher(text, keyword, mode):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    key = ''.join(keyword[i % len(keyword)] for i in range(len(text)))
    if mode == 'encrypt':
        result = ''.join(alphabet[(alphabet.index(text[i]) + alphabet.index(key[i])) % 33]
                         for i in range(len(text)))
    elif mode == 'decrypt':
        result = ''.join(alphabet[(alphabet.index(text[i]) - alphabet.index(key[i])) % 33]
                         for i in range(len(text)))
    return result

def paste_text(field):
    field.delete(0, tk.END)
    field.insert(0, app.clipboard_get())

def on_entry_click(event):
    if entry_text.get() == 'Введите текст здесь':
        entry_text.delete(0, tk.END)
    if entry_keyword.get() == 'Введите ключ здесь':
        entry_keyword.delete(0, tk.END)

def on_focus_out(event):
    if entry_text.get() == '':
        entry_text.insert(0, 'Введите текст здесь')
    if entry_keyword.get() == '':
        entry_keyword.insert(0, 'Введите ключ здесь')

def encrypt_text():
    text = entry_text.get()
    keyword = entry_keyword.get()
    encrypted_text = vigenere_cipher(text, keyword, 'encrypt')
    result_label.config(text=encrypted_text)
    copy_button.config(state="normal")

def decrypt_text():
    text = entry_text.get()
    keyword = entry_keyword.get()
    decrypted_text = vigenere_cipher(text, keyword, 'decrypt')
    result_label.config(text=decrypted_text)
    copy_button.config(state="normal")

def copy_result():
    text = result_label.cget("text")
    pyperclip.copy(text)
    result_label.config(text="Текст скопирован в буфер обмена")

app = tk.Tk()
app.title('Шифр Виженера')

input_frame = tk.Frame(app)
input_frame.pack(pady=10)

label_text = tk.Label(input_frame, text="Текст:")
label_text.grid(row=0, column=0, padx=10, pady=10)

entry_text = tk.Entry(input_frame, font=('Arial', 14))
entry_text.insert(0, 'Введите текст здесь')
entry_text.bind('<FocusIn>', on_entry_click)
entry_text.bind('<FocusOut>', on_focus_out)
entry_text.grid(row=0, column=1, padx=10, pady=10)

label_keyword = tk.Label(input_frame, text="Ключ:")
label_keyword.grid(row=1, column=0, padx=10, pady=10)

entry_keyword = tk.Entry(input_frame, font=('Arial', 14))
entry_keyword.insert(0, 'Введите ключ здесь')
entry_keyword.bind('<FocusIn>', on_entry_click)
entry_keyword.bind('<FocusOut>', on_focus_out)
entry_keyword.grid(row=1, column=1, padx=10, pady=10)

button_frame = tk.Frame(app)
button_frame.pack(pady=10)

encrypt_button = tk.Button(button_frame, text="Зашифровать", command=encrypt_text)
encrypt_button.grid(row=0, column=0, padx=10, pady=10)

decrypt_button = tk.Button(button_frame, text="Расшифровать", command=decrypt_text)
decrypt_button.grid(row=0, column=1, padx=10, pady=10)

result_label = tk.Label(app, text="", font=('Arial', 18))
result_label.pack(pady=10)

copy_button = tk.Button(app, text="Копировать", command=copy_result, state="disabled")
copy_button.pack(pady=10)

app.mainloop()                    
