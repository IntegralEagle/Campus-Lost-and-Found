# 🎓 Campus Lost & Found Management System

A Python-based desktop application developed using **Tkinter** and **MySQL** to help students report, search, and manage lost and found items within a college campus.

The system provides a simple graphical interface where students can submit lost or found item reports, view existing reports, search for items, filter records, and delete selected reports.

---

## 📌 Project Overview

Losing personal belongings in a college campus is a common problem. Students may find it difficult to locate lost items or connect with the person who found them.

The **Campus Lost & Found Management System** aims to simplify this process by providing a centralized platform to record and manage lost and found item information.

The application uses Tkinter for its graphical user interface and MySQL for storing item reports.

## ✨ Features

- **Report an Item:** Submit details of lost or found items.
- **Item Categories:** Select the appropriate category for an item.
- **Report Type:** Choose between Lost and Found.
- **Location Details:** Specify where an item was lost or found.
- **Contact Information:** Provide a contact number to help students coordinate item recovery.
- **Search Items:** Search for reports using item names.
- **Filter Reports:** Filter records based on Lost, Found, or All.
- **View Reports:** Display saved item reports in a table.
- **Delete Reports:** Select and delete an existing report.
- **Clear Form:** Reset the input fields.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Tkinter | Graphical User Interface |
| MySQL | Database management |
| MySQL Connector/Python | Python–MySQL connectivity |
| python-dotenv | Managing database configuration |
| VS Code | Development environment |
| Git & GitHub | Version control and project hosting |

## 📂 Project Structure

```text
Lost_Found_Tkinter/
│
├── main.py
├── db_connection.py
├── test_db.py
├── requirements.txt
├── .env
├── .gitignore
│
└── __pycache__/
```

### File Description

| File | Description |
|---|---|
| `main.py` | Contains the Tkinter GUI, application layout, buttons, and event-handling functions. |
| `db_connection.py` | Establishes the connection between Python and the MySQL database. |
| `test_db.py` | Tests whether the application can successfully connect to MySQL. |
| `requirements.txt` | Contains the Python dependencies required by the project. |
| `.env` | Stores database configuration such as the MySQL password. |
| `.gitignore` | Prevents sensitive and unnecessary files from being uploaded to GitHub. |

## ⚙️ Installation and Setup

### 1. Prerequisites

Make sure you have installed:

- Python 3
- MySQL Server
- MySQL Workbench
- Visual Studio Code

### 2. Clone the Repository

```bash
git clone https://github.com/IntegralEagle/Campus-Lost-and-Found.git
```

Navigate to the project directory:

```bash
cd Campus-Lost-and-Found
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🗄️ Database Configuration

The application uses MySQL as its database.

**Database Name:** `campus_lost_found`

Open MySQL Workbench and make sure the database and the required `item_reports` table exist.

Example database creation command:

```sql
CREATE DATABASE IF NOT EXISTS campus_lost_found;
```

Select the database:

```sql
USE campus_lost_found;
```

The table should contain the columns required by the application, including item details, report type, location, contact number, and status. Its exact structure must match the SQL queries in `main.py`.

### Environment Variables

Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_mysql_password
```

Replace `your_mysql_password` with your own MySQL password.

**Important:** Never upload your `.env` file or expose your database password publicly.

## ▶️ Running the Application

Open the project folder in VS Code.

Activate your virtual environment and run:

```bash
python main.py
```

To test the database connection separately:

```bash
python test_db.py
```

The Tkinter application window should open after successful execution.

## 🖥️ Application Modules

### 1. Report an Item
Allows users to enter item information, select its report type, and submit the report.

### 2. Search and Filter
Allows users to search for items and filter reports according to their type.

### 3. Saved Item Reports
Displays the stored reports in a table with relevant details.

### 4. Delete Selected Report
Allows users to select an existing report and delete it after confirmation.

### 5. Clear Form
Resets the input fields to their default values.

## 🔄 Event Handling

The application uses Tkinter button commands to handle user interactions.

| Event | Functionality |
|---|---|
| Submit Report | Validates and saves item details to MySQL. |
| Search | Searches for matching item reports. |
| Reset | Resets the search and filter fields. |
| View / Refresh Reports | Retrieves and displays saved records. |
| Delete Selected | Deletes the selected report from MySQL. |
| Clear Form | Clears the item input fields. |

## 🧪 Testing

The following operations can be tested:

1. Submit a Lost Item report.
2. Submit a Found Item report.
3. Try submitting the form with empty fields.
4. Search for an existing item.
5. Filter reports by Lost and Found.
6. Refresh the saved reports table.
7. Select and delete a report.
8. Verify that deleted records are no longer displayed.
9. Test the application with MySQL disconnected.

## 📸 Screenshots

Add your application screenshots here after uploading them to a `screenshots` folder.

Example:

```text
screenshots/
├── main_window.png
├── submit_report.png
├── search_filter.png
└── saved_reports.png
```

Embed them in this README using:

```markdown
![Main Window](screenshots/main_window.png)

![Search and Filter](screenshots/search_filter.png)

![Saved Reports](screenshots/saved_reports.png)
```

## 🚀 Future Enhancements

- Student login and registration.
- Image upload for lost and found items.
- Improved item-matching functionality.
- Email or notification alerts.
- Report status updates when an item is returned.

## 👨‍💻 Author

**Lavya Sinha**

B.Tech – Computer Science and Engineering (Cybersecurity)

## 📄 License

This project was developed for educational and academic purposes.