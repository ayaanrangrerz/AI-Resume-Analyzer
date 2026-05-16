import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

# Keywords for scoring
skills = [
    "python", "java", "c++", "machine learning",
    "data structures", "sql", "html", "css"
]

# Analyze Resume

def analyze_resume():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

    if not file_path:
        return

    text = ""

    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text.lower()

    score = 0
    found_skills = []

    for skill in skills:
        if skill in text:
            score += 10
            found_skills.append(skill)

    if not text:
        result_text.set("No text could be extracted from the selected PDF.")
        return

    result_text.set(
        f"Resume Score: {score}/100\n\n"
        f"Skills Found:\n{', '.join(found_skills) if found_skills else 'None'}"
    )

# GUI
root = tk.Tk()
root.title("AI Resume Analyzer")
root.geometry("500x400")

heading = tk.Label(root, text="AI Resume Analyzer", font=("Arial", 20, "bold"))
heading.pack(pady=20)

btn = tk.Button(root, text="Upload Resume", command=analyze_resume, font=("Arial", 14))
btn.pack(pady=20)

result_text = tk.StringVar()

result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12), justify="left")
result_label.pack(pady=20)

root.mainloop()