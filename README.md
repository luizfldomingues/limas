# Lima's Order Manager

A simple and efficient order and sales management system designed for dine-in establishments like restaurants, cafés, and ice cream shops.

## 🚀 Purpose

Lima's aims to simplify daily operations for establishment owners by providing a centralized platform for handling orders, tracking sales, and managing users and products. The goal is to offer an intuitive interface that requires minimal training.

## ✨ Features

* **Order Management:** Create, view, update, and complete active orders for different tables.
* **Sales History:** Access a complete history of completed orders within a specified date range and reopen them if needed.
* **Product Catalog:** (Admin) Add, edit, or remove products and categorize them by type.
* **User Management:** (Admin) Manage user accounts and their roles within the system.
* **Reporting:** (Admin) Generate sales reports for specific periods to gain insights into business performance.

## 🛠️ Getting Started

Follow these instructions to get a local copy up and running.

### **Prerequisites**

* Python 3.x
* pip

### **Installation & Setup**

1.  **Download the Project:**
    Download or clone the project files to your local machine.

2.  **Create and Activate a Virtual Environment:**
    It's highly recommended to use a Python virtual environment. In the project's root directory, run:

    ```bash
    # Create the virtual environment
    python -m venv .venv

    # Activate it (Linux/macOS)
    source .venv/bin/activate
    ```

3.  **Install Dependencies:**
    With the virtual environment active, install all required packages from the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application:**
    Execute the following command to start the Flask development server:

    ```bash
    flask run
    ```
    By default, the application will be available at **`http://127.0.0.1:5000`**.

    > **Note:** To make the application accessible to other devices on your local network, use the following command:
    > `flask run --host=0.0.0.0`

---

## 📖 How to Use

The application is designed to be as intuitive as possible. **Please note that the user interface is currently in Portuguese.**

### **Initial Setup**

* When you first access the application, you will be redirected to a registration page.
* **The first user account created is automatically granted administrator privileges.**

### **General Workflow**

* **Dashboard:** The main page displays all currently active orders.
* **Creating an Order:** Click on "Novo Pedido" in the header. You will be prompted to enter the table number, customer name, and select products.
* **Managing Orders:** From the main page, you can add items to an order, edit it, mark it as complete, or view more details (including deletion).
* **Order History:** The "Histórico" section allows you to view past orders and reopen them if necessary.

### **Admin-Specific Functions**

If you are logged in as an administrator, you will have access to additional pages:
* **Products (`Produtos`):** Manage the product catalog.
* **Reports (`Relatórios`):** Generate sales reports.
* **Users (`Usuários`):** Manage system users.

### **Configuration**

To prevent new user registrations, you can change a setting in the code:
1.  Open the file `preferences.py`.
2.  Change the value of the `allow_new_users` variable to `False`.

## 🎬 Showcase

[![Limas - A simple order and sales manager for dine-in establishments](https://img.youtube.com/vi/0umzbZ7kjq8/0.jpg)](https://www.youtube.com/watch?v=0umzbZ7kjq8)
