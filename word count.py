import tkinter as tk
from tkinter import filedialog, messagebox
from collections import Counter
import string

# Optional: stopwords to ignore
STOPWORDS = {
    "the", "a", "an", "and", "or", "in", "on", "at", "to", "for", "of", "is", "are"
}

# Function to analyze text
def analyze_text(text):
    # Clean text
    text_clean = text.translate(str.maketrans("", "", string.punctuation))
    words = text_clean.lower().split()
    words_filtered = [w for w in words if w not in STOPWORDS]
    
    total_chars = len(text)
    total_words = len(words)
    total_sentences = text.count('.') + text.count('!') + text.count('?')
    total_paragraphs = text.count('\n') + 1
    
    word_freq = Counter(words_filtered).most_common(10)
    
    result = (
        f"Characters: {total_chars}\n"
        f"Words: {total_words}\n"
        f"Sentences: {total_sentences}\n"
        f"Paragraphs: {total_paragraphs}\n\n"
        f"Top 10 Words:\n"
    )
    for word, count in word_freq:
        result += f"{word}: {count}\n"
    
    return result

# GUI setup
def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as f:
            text_input.delete("1.0", tk.END)
            text_input.insert(tk.END, f.read())

def count_words():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter or open some text first!")
        return
    result = analyze_text(text)
    result_display.config(state=tk.NORMAL)
    result_display.delete("1.0", tk.END)
    result_display.insert(tk.END, result)
    result_display.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Advanced Word Counter")
root.geometry("600x600")

# Text input area
text_input = tk.Text(root, height=15)
text_input.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)
open_btn = tk.Button(btn_frame, text="Open File", command=open_file)
open_btn.pack(side=tk.LEFT, padx=5)
count_btn = tk.Button(btn_frame, text="Analyze Text", command=count_words)
count_btn.pack(side=tk.LEFT, padx=5)

# Result display
result_display = tk.Text(root, height=15, state=tk.DISABLED)
result_display.pack(pady=10)

root.mainloop()
