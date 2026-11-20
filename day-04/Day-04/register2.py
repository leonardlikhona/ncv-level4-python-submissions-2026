import tkinter as tk
from tkinter import ttk, messagebox

# ==========================================
# ORIGINAL DATA & LOGIC FUNCTIONS
# ==========================================
def add_learner(learners, number, name):
    if number in learners:
        return False
    learners[number] = {"name": name, "marks": []}
    return True

def add_mark(learners, number, mark):
    if number not in learners:
        return False
    learners[number]["marks"].append(mark)
    return True

def rename_learner(learners, number, new_name):
    if number not in learners:
        return False
    learners[number]["name"] = new_name
    return True

def delete_learner(learners, number):
    if number not in learners:
        return False
    del learners[number]
    return True

def average_of(values):
    total = 0
    for v in values:
        total = total + v
    return total / len(values)

def learner_average(learners, number):
    marks = learners[number]["marks"]
    if len(marks) == 0:
        return None
    return average_of(marks)

def is_valid_number(text):
    return text.isdigit() and len(text) == 7

def is_valid_mark(text):
    return text.isdigit() and 0 <= int(text) <= 100

# ==========================================
# SORTING FUNCTIONS (BUBBLE SORT)
# ==========================================
def get_sorted_rows(learners, sort_by="average", search_text=""):
    rows = []
    for number in learners:
        name = learners[number]["name"]
        if search_text.lower() not in name.lower() and search_text not in number:
            continue
        avg = learner_average(learners, number)
        marks_str = ", ".join(str(m) for m in learners[number]["marks"])
        rows.append({
            "number": number,
            "name": name,
            "marks": marks_str if marks_str else "No marks",
            "avg": avg
        })

    n = len(rows)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            swap = False
            if sort_by == "average":
                # Learners without marks go to the bottom
                a = rows[j]["avg"] if rows[j]["avg"] is not None else -1
                b = rows[j + 1]["avg"] if rows[j + 1]["avg"] is not None else -1
                if a < b:
                    swap = True
            elif sort_by == "name":
                if rows[j]["name"].lower() > rows[j + 1]["name"].lower():
                    swap = True
            elif sort_by == "number":
                if rows[j]["number"] > rows[j + 1]["number"]:
                    swap = True

            if swap:
                rows[j], rows[j + 1] = rows[j + 1], rows[j]
    return rows


# ==========================================
# TKINTER GRAPHICAL INTERFACE
# ==========================================
class LearnerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NCV Level 4 | Learner Records & Ranking")
        self.root.geometry("760x520")
        self.root.configure(padx=15, pady=15)

        self.learners = {}
        self.current_sort = "average"

        # --- Top Input Frame ---
        input_frame = ttk.LabelFrame(root, text="Manage Learner", padding=10)
        input_frame.pack(fill="x", pady=(0, 10))

        ttk.Label(input_frame, text="Student No (7 digits):").grid(row=0, column=0, sticky="w", padx=5)
        self.entry_num = ttk.Entry(input_frame, width=15)
        self.entry_num.grid(row=0, column=1, padx=5)

        ttk.Label(input_frame, text="Name:").grid(row=0, column=2, sticky="w", padx=5)
        self.entry_name = ttk.Entry(input_frame, width=22)
        self.entry_name.grid(row=0, column=3, padx=5)

        ttk.Button(input_frame, text="Add Learner", command=self.ui_add_learner).grid(row=0, column=4, padx=5)
        ttk.Button(input_frame, text="Rename", command=self.ui_rename_learner).grid(row=0, column=5, padx=5)
        ttk.Button(input_frame, text="Delete", command=self.ui_delete_learner).grid(row=0, column=6, padx=5)

        # --- Marks Frame ---
        mark_frame = ttk.LabelFrame(root, text="Capture Mark", padding=10)
        mark_frame.pack(fill="x", pady=(0, 10))

        ttk.Label(mark_frame, text="Student No:").grid(row=0, column=0, sticky="w", padx=5)
        self.entry_mark_num = ttk.Entry(mark_frame, width=15)
        self.entry_mark_num.grid(row=0, column=1, padx=5)

        ttk.Label(mark_frame, text="Mark (0-100):").grid(row=0, column=2, sticky="w", padx=5)
        self.entry_mark = ttk.Entry(mark_frame, width=10)
        self.entry_mark.grid(row=0, column=3, padx=5)

        ttk.Button(mark_frame, text="Add Mark", command=self.ui_add_mark).grid(row=0, column=4, padx=10)

        # --- Filter & Sort Controls ---
        ctrl_frame = ttk.Frame(root)
        ctrl_frame.pack(fill="x", pady=(0, 8))

        ttk.Label(ctrl_frame, text="Search:").pack(side="left", padx=(0, 5))
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *args: self.refresh_table())
        ttk.Entry(ctrl_frame, textvariable=self.search_var, width=20).pack(side="left", padx=(0, 15))

        ttk.Label(ctrl_frame, text="Sort By:").pack(side="left", padx=(0, 5))
        ttk.Button(ctrl_frame, text="Average (High → Low)", command=lambda: self.set_sort("average")).pack(side="left", padx=3)
        ttk.Button(ctrl_frame, text="Name (A → Z)", command=lambda: self.set_sort("name")).pack(side="left", padx=3)
        ttk.Button(ctrl_frame, text="Student No (Asc)", command=lambda: self.set_sort("number")).pack(side="left", padx=3)

        # --- Records Table ---
        columns = ("rank", "number", "name", "marks", "average")
        self.tree = ttk.Treeview(root, columns=columns, show="headings", height=12)
        self.tree.heading("rank", text="#")
        self.tree.heading("number", text="Student No")
        self.tree.heading("name", text="Learner Name")
        self.tree.heading("marks", text="Captured Marks")
        self.tree.heading("average", text="Average (%)")

        self.tree.column("rank", width=45, anchor="center")
        self.tree.column("number", width=110, anchor="center")
        self.tree.column("name", width=180, anchor="w")
        self.tree.column("marks", width=250, anchor="w")
        self.tree.column("average", width=100, anchor="e")

        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.on_row_select)

    def set_sort(self, sort_mode):
        self.current_sort = sort_mode
        self.refresh_table()

    def on_row_select(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0], "values")
            self.entry_num.delete(0, tk.END)
            self.entry_num.insert(0, values[1])
            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(0, values[2])
            self.entry_mark_num.delete(0, tk.END)
            self.entry_mark_num.insert(0, values[1])

    def ui_add_learner(self):
        num = self.entry_num.get().strip()
        name = self.entry_name.get().strip()
        if not is_valid_number(num) or name == "":
            messagebox.showerror("Invalid Input", "Enter a 7-digit student number and a valid name.")
            return
        if add_learner(self.learners, num, name):
            self.entry_num.delete(0, tk.END)
            self.entry_name.delete(0, tk.END)
            self.refresh_table()
        else:
            messagebox.showwarning("Duplicate", "That student number already exists.")

    def ui_rename_learner(self):
        num = self.entry_num.get().strip()
        new_name = self.entry_name.get().strip()
        if new_name == "":
            messagebox.showerror("Invalid Input", "Enter a new name.")
            return
        if rename_learner(self.learners, num, new_name):
            self.refresh_table()
        else:
            messagebox.showerror("Not Found", "No learner with that student number.")

    def ui_delete_learner(self):
        num = self.entry_num.get().strip()
        if delete_learner(self.learners, num):
            self.entry_num.delete(0, tk.END)
            self.entry_name.delete(0, tk.END)
            self.refresh_table()
        else:
            messagebox.showerror("Not Found", "No learner with that student number.")

    def ui_add_mark(self):
        num = self.entry_mark_num.get().strip()
        mark_text = self.entry_mark.get().strip()
        if not is_valid_mark(mark_text):
            messagebox.showerror("Invalid Mark", "Enter a whole number between 0 and 100.")
            return
        if add_mark(self.learners, num, int(mark_text)):
            self.entry_mark.delete(0, tk.END)
            self.refresh_table()
        else:
            messagebox.showerror("Not Found", "No learner with that student number.")

    def refresh_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        rows = get_sorted_rows(self.learners, self.current_sort, self.search_var.get())
        for idx, r in enumerate(rows, start=1):
            avg_display = f"{r['avg']:.1f}" if r["avg"] is not None else "—"
            self.tree.insert("", "end", values=(idx, r["number"], r["name"], r["marks"], avg_display))


if __name__ == "__main__":
    root = tk.Tk()
    app = LearnerApp(root)
    root.mainloop()