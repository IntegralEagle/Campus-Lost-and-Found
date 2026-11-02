import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
from db_connection import get_connection
# ==================== MAIN WINDOW ====================
root = tk.Tk()
root.title("Campus Lost & Found Management System")
root.geometry("1100x750")
root.minsize(900, 650)
root.configure(bg="#eef3f8")
# ==================== TITLE ====================
title = tk.Label(
    root,
    text="Campus Lost & Found Management System",
    font=("Arial", 22, "bold"),
    bg="#eef3f8",
    fg="#183153"
)
title.pack(pady=15)
# ==================== INPUT FORM ====================
form = tk.LabelFrame(
    root,
    text="Report an Item",
    font=("Arial", 12, "bold"),
    bg="white",
    padx=15,
    pady=10
)
form.pack(fill="x", padx=20, pady=5)
tk.Label(form, text="Item Name:", bg="white").grid(
    row=0, column=0, sticky="w", padx=8, pady=6
)
name_entry = tk.Entry(form, width=30)
name_entry.grid(row=0, column=1, padx=8, pady=6)
tk.Label(form, text="Category:", bg="white").grid(
    row=0, column=2, sticky="w", padx=8, pady=6
)
category_box = ttk.Combobox(
    form,
    values=[
        "Electronics", "ID Card", "Bag", "Wallet",
        "Books", "Clothing", "Other"
    ],
    state="readonly",
    width=25
)
category_box.grid(row=0, column=3, padx=8, pady=6)
category_box.set("Electronics")

tk.Label(form, text="Report Type:", bg="white").grid(
    row=1, column=0, sticky="w", padx=8, pady=6
)
type_box = ttk.Combobox(
    form,
    values=["Lost", "Found"],
    state="readonly",
    width=27
)
type_box.grid(row=1, column=1, padx=8, pady=6)
type_box.set("Lost")

tk.Label(form, text="Location:", bg="white").grid(
    row=1, column=2, sticky="w", padx=8, pady=6
)
location_entry = tk.Entry(form, width=30)
location_entry.grid(row=1, column=3, padx=8, pady=6)

tk.Label(form, text="Description:", bg="white").grid(
    row=2, column=0, sticky="nw", padx=8, pady=6
)
description_entry = tk.Text(
    form, width=70, height=3, wrap="word"
)
description_entry.grid(
    row=2, column=1, columnspan=3,
    sticky="w", padx=8, pady=6
)

# ==================== SEARCH BAR ====================
search_frame = tk.LabelFrame(
    root,
    text="Search and Filter Reports",
    font=("Arial", 11, "bold"),
    bg="white",
    padx=10,
    pady=8
)
search_frame.pack(fill="x", padx=20, pady=5)

tk.Label(search_frame, text="Search:", bg="white").pack(
    side="left", padx=5
)
search_entry = tk.Entry(search_frame, width=30)
search_entry.pack(side="left", padx=5)

tk.Label(search_frame, text="Report Type:", bg="white").pack(
    side="left", padx=5
)
filter_type = ttk.Combobox(
    search_frame,
    values=["All", "Lost", "Found"],
    state="readonly",
    width=12
)
filter_type.set("All")
filter_type.pack(side="left", padx=5)

# ==================== REPORT TABLE ====================
table_frame = tk.LabelFrame(
    root,
    text="Saved Item Reports",
    font=("Arial", 12, "bold"),
    bg="white",
    padx=10,
    pady=10
)
table_frame.pack(fill="both", expand=True, padx=20, pady=10)

columns = (
    "report_id", "item_name", "report_type", "category",
    "location", "incident_date", "status"
)

report_table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=10,
    selectmode="browse"
)
headings = {
    "report_id": "ID",
    "item_name": "Item Name",
    "report_type": "Type",
    "category": "Category",
    "location": "Location",
    "incident_date": "Incident Date",
    "status": "Status"
}
widths = {
    "report_id": 55,
    "item_name": 180,
    "report_type": 90,
    "category": 120,
    "location": 180,
    "incident_date": 120,
    "status": 90
}
for column in columns:
    report_table.heading(column, text=headings[column])
    report_table.column(
        column, width=widths[column], anchor="center"
    )
scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=report_table.yview
)
report_table.configure(yscrollcommand=scrollbar.set)
report_table.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# ==================== CLEAR FORM ====================
def clear_form():
    name_entry.delete(0, tk.END)
    category_box.set("Electronics")
    type_box.set("Lost")
    location_entry.delete(0, tk.END)
    description_entry.delete("1.0", tk.END)
    name_entry.focus_set()

# ==================== VALIDATE FORM ====================
def validate_form():
    name = name_entry.get().strip()
    category = category_box.get().strip()
    report_type = type_box.get().strip()
    location = location_entry.get().strip()
    description = description_entry.get("1.0", tk.END).strip()
    if not name:
        messagebox.showwarning(
            "Validation Error", "Please enter the item name.",
            parent=root
        )
        name_entry.focus_set()
        return None

    if len(name) < 2 or len(name) > 100:
        messagebox.showwarning(
            "Validation Error",
            "Item name must contain 2 to 100 characters.",
            parent=root
        )
        name_entry.focus_set()
        return None

    valid_categories = [
        "Electronics", "ID Card", "Bag", "Wallet",
        "Books", "Clothing", "Other"
    ]
    if category not in valid_categories:
        messagebox.showwarning(
            "Validation Error", "Please select a valid category.",
            parent=root
        )
        category_box.focus_set()
        return None

    if report_type not in ("Lost", "Found"):
        messagebox.showwarning(
            "Validation Error", "Please select Lost or Found.",
            parent=root
        )
        type_box.focus_set()
        return None
    if len(location) < 2 or len(location) > 150:
        messagebox.showwarning(
            "Validation Error",
            "Location must contain 2 to 150 characters.",
            parent=root
        )
        location_entry.focus_set()
        return None

    if len(description) > 500:
        messagebox.showwarning(
            "Validation Error",
            "Description cannot exceed 500 characters.",
            parent=root
        )
        description_entry.focus_set()
        return None
    return (
        name, category, report_type.lower(),
        location, description
    )

# ==================== DISPLAY TABLE ROWS ====================
def display_records(records):
    for row in report_table.get_children():
        report_table.delete(row)
    for record in records:
        report_table.insert("", tk.END, values=record)

# ==================== VIEW / REFRESH REPORTS ====================
def view_reports(show_error=True):
    connection = None
    cursor = None
    try:
        connection = get_connection()
        if connection is None or not connection.is_connected():
            if show_error:
                messagebox.showerror(
                    "Database Error", "Could not connect to MySQL.",
                    parent=root
                )
            return
        cursor = connection.cursor()
        cursor.execute("""
            SELECT report_id, item_name, report_type,
                   category, location, incident_date, status
            FROM item_reports
            ORDER BY report_id DESC
        """)
        records = cursor.fetchall()
        display_records(records)
    except Exception as error:
        if show_error:
            messagebox.showerror(
                "Database Error",
                f"Could not load reports.\n\n{error}",
                parent=root
            )
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

# ==================== SEARCH REPORTS ====================
def search_reports(event=None):
    keyword = search_entry.get().strip()
    selected_type = filter_type.get()
    connection = None
    cursor = None
    try:
        connection = get_connection()
        if connection is None or not connection.is_connected():
            messagebox.showerror(
                "Database Error", "Could not connect to MySQL.",
                parent=root
            )
            return
        cursor = connection.cursor()
        query = """
            SELECT report_id, item_name, report_type,
                   category, location, incident_date, status
            FROM item_reports
            WHERE (
                item_name LIKE %s
                OR location LIKE %s
                OR category LIKE %s
            )
        """
        pattern = f"%{keyword}%"
        values = [pattern, pattern, pattern]

        if selected_type in ("Lost", "Found"):
            query += " AND report_type = %s"
            values.append(selected_type.lower())

        query += " ORDER BY report_id DESC"

        cursor.execute(query, tuple(values))
        records = cursor.fetchall()
        display_records(records)
        if not records:
            messagebox.showinfo(
                "Search Results", "No matching reports found.",
                parent=root
            )

    except Exception as error:
        messagebox.showerror(
            "Search Error",
            f"Could not search reports.\n\n{error}",
            parent=root
        )

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
def reset_search():
    search_entry.delete(0, tk.END)
    filter_type.set("All")
    view_reports()

# Search buttons are created AFTER their functions are defined
tk.Button(
    search_frame,
    text="Search",
    command=search_reports,
    bg="#2463a6",
    fg="white",
    cursor="hand2"
).pack(side="left", padx=5)

tk.Button(
    search_frame,
    text="Reset",
    command=reset_search,
    cursor="hand2"
).pack(side="left", padx=5)

search_entry.bind("<Return>", search_reports)

# ==================== ADD ITEM ====================
def add_item():
    validated = validate_form()
    if validated is None:
        return
    name, category, report_type, location, description = validated
    connection = None
    cursor = None
    saved = False
    try:
        connection = get_connection()
        if connection is None or not connection.is_connected():
            messagebox.showerror(
                "Database Error", "Could not connect to MySQL.",
                parent=root
            )
            return

        cursor = connection.cursor()
        query = """
            INSERT INTO item_reports
            (
                user_id, report_type, item_name, category,
                description, location, incident_date, status
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            1, report_type, name, category, description,
            location, date.today(), "open"
        )

        cursor.execute(query, values)
        connection.commit()
        saved = True

    except Exception as error:
        if connection is not None and connection.is_connected():
            connection.rollback()
        messagebox.showerror(
            "Database Error",
            f"Could not save the report.\n\n{error}",
            parent=root
        )

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

    if saved:
        clear_form()
        search_entry.delete(0, tk.END)
        filter_type.set("All")
        view_reports(show_error=False)
        messagebox.showinfo(
            "Success", "Item report saved successfully!",
            parent=root
        )

# ==================== DELETE SELECTED REPORT ====================
def delete_report():
    selected = report_table.selection()
    if not selected:
        messagebox.showwarning(
            "No Selection",
            "Please select a report from the table first.",
            parent=root
        )
        return
    values = report_table.item(selected[0], "values")
    report_id, item_name = values[0], values[1]

    if not messagebox.askyesno(
        "Confirm Delete",
        f"Delete '{item_name}' (ID: {report_id})?",
        parent=root
    ):
        return

    connection = None
    cursor = None
    deleted = False

    try:
        connection = get_connection()
        if connection is None or not connection.is_connected():
            messagebox.showerror(
                "Database Error", "Could not connect to MySQL.",
                parent=root
            )
            return

        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM item_reports WHERE report_id = %s",
            (report_id,)
        )
        connection.commit()
        deleted = cursor.rowcount > 0

    except Exception as error:
        if connection is not None and connection.is_connected():
            connection.rollback()
        messagebox.showerror(
            "Database Error",
            f"Could not delete the report.\n\n{error}",
            parent=root
        )

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

    if deleted:
        view_reports(show_error=False)
        messagebox.showinfo(
            "Success", "Report deleted successfully.", parent=root
        )
    else:
        view_reports(show_error=False)
        messagebox.showwarning(
            "Not Found",
            "The report no longer exists.",
            parent=root
        )

# ==================== ACTION BUTTONS ====================
buttons = tk.Frame(root, bg="#eef3f8")
buttons.pack(pady=10)
tk.Button(
    buttons,
    text="Submit Report",
    command=add_item,
    bg="#2463a6",
    fg="white",
    width=16,
    cursor="hand2"
).pack(side="left", padx=6)

tk.Button(
    buttons,
    text="Clear Form",
    command=clear_form,
    width=14,
    cursor="hand2"
).pack(side="left", padx=6)

tk.Button(
    buttons,
    text="View / Refresh Reports",
    command=view_reports,
    bg="#27834a",
    fg="white",
    width=20,
    cursor="hand2"
).pack(side="left", padx=6)

tk.Button(
    buttons,
    text="Delete Selected",
    command=delete_report,
    bg="#bd3838",
    fg="white",
    width=17,
    cursor="hand2"
).pack(side="left", padx=6)

# ==================== KEYBOARD EVENTS ====================
name_entry.bind(
    "<Return>",
    lambda event: (add_item(), "break")[1]
)
location_entry.bind(
    "<Return>",
    lambda event: (add_item(), "break")[1]
)
description_entry.bind(
    "<Control-Return>",
    lambda event: (add_item(), "break")[1]
)


# ==================== SAFE WINDOW CLOSING ====================

def close_application():
    confirm = messagebox.askyesno(
        "Exit Application",
        "Are you sure you want to close the application?",
        parent=root
    )
    if confirm:
        root.destroy()


root.protocol("WM_DELETE_WINDOW", close_application)

# ==================== START APPLICATION ====================
view_reports()
name_entry.focus_set()
root.mainloop()
