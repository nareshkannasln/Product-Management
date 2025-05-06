

# Inventory Management Web App

## Overview

This is an Inventory Management Web App built using Flask and MySQL. The app allows users to manage products, locations, and product movements within an organization. It supports full CRUD (Create, Read, Update, Delete) operations for managing the inventory data.

## Features

* **Product Management:** Add, update, view, and delete products.
* **Location Management:** Add, update, view, and delete product locations.
* **Product Movement:** Track and update movements of products between different locations.
* **Responsive Design:** The app uses custom CSS for layout and styling (no Bootstrap).

## Tech Stack

* **Backend:** Flask (Python web framework)
* **Database:** MySQL
* **Frontend:** HTML, CSS (custom styling)

## Prerequisites

Before running the app, make sure you have the following installed:

* Python 3.12
* MySQL Server
* pip (for installing Python packages)

### Install dependencies

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/nareshkannasln/Product-Management
cd <repository-directory>
pip install -r requirements.txt
```

### Set up MySQL Database

1. Create a MySQL database for the application:

```sql
CREATE DATABASE Product_Management;
```

2. Set up the required tables. The script will create the necessary schema on the first run of the app.

### Configuration

In the `config.py` file, provide your MySQL database credentials:



### Running the App

1. Run the Flask app:

```bash
flask run
```

2. Visit `http://127.0.0.1:8001/` in your browser to start using the app.

## Application Structure

* `app.py`: Main Flask application file.
* `templates/`: Directory containing HTML templates.

  * `index.html`: Home page of the app.
  * `products.html`: Page for managing products.
  * `locations.html`: Page for managing locations.
  * `movements.html`: Page for tracking product movements.
  * `report.htmk` : Page for shows the rport of product.
* `static/`: Directory containing static files like CSS 
* 

### Product Management

* **Add Product:** Add new products with name, description, and quantity.
* **Update Product:** Edit details of an existing product.
* **View Products:** List all products in the inventory.

### Location Management

* **Add Location:** Add new product locations.
* **Update Location:** Modify existing location details.
* **View Locations:** View all locations.

### Product Movement

* **Add Movement:** Track when products are moved between locations.
* **Update Movement:** Update movement details (e.g., quantity moved).
* **View Movements:** View all product movements.

## Future Improvements

* **JWT Authentication:** Implement JWT-based authentication for better security.
* **Role-based Access Control (RBAC):** Add different user roles (admin, staff) with varying permissions.
* **Reports and Analytics:** Add features to generate inventory reports and analytics.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
