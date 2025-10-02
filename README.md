# CSV Analyzer with Flask API

A powerful web tool designed for businesses to easily upload their sales data in CSV format and instantly gain key insights into their performance. This application processes sales files to reveal total revenue, best-selling products, and top customers through a user-friendly interface and a robust API.

## Project Objective

The goal of this project is to provide a simple, self-hosted solution for small to medium-sized businesses to perform essential sales analysis without needing complex software. By simply providing a sales report in CSV format, a user can quickly understand:

- **Overall Financial Performance:** What is the total revenue?
- **Product Popularity:** Which product is the best-seller?
- **Customer Value:** Who are the most valuable customers by spending?
- **Sales Volume:** What is the total number of transactions?

This tool empowers users to make data-driven decisions by making sales analysis accessible and instantaneous.

## Features

- **File Upload:** A dedicated endpoint to securely receive and store `.csv` files, assigning a unique ID to each one.
- **Dynamic Analysis:** The user specifies in the frontend which columns from their file correspond to "product," "price," "quantity," and "customer."
- **RESTful API:** The architecture is split into two main endpoints, following best practices: one for uploading and one for analysis.
- **JSON Results:** The API returns a structured JSON object with the analysis results, including:
  - Total Revenue
  - Best-Selling Product
  - Top-Spending Customer
  - Total Transactions
- **Simple Interface:** A frontend built with HTML, CSS, and JavaScript that consumes the API, allowing for easy and intuitive interaction without external tools.

## Technologies Used

- **Backend:** Python, Flask, Pandas
- **Frontend:** HTML, CSS, JavaScript (with `fetch` API)
- **Server (for deployment):** Gunicorn (recommended)

## How to Run the Project Locally

Follow the steps below to run the application on your machine.

**1. Clone the Repository**
```bash
git clone [https://github.com/eubrunoo/CSV-Analyzer-with-Flask-API.git](https://github.com/eubrunoo/CSV-Analyzer-with-Flask-API.git)
cd CSV-Analyzer-with-Flask-API
```

**2. Create and Activate a Virtual Environment**
```bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```
**3. Install Dependencies**

The `requirements.txt` file contains all the necessary Python libraries.
```bash
pip install -r requirements.txt
```
**4. Create Necessary Folders**

Ensure that the `uploads`, `templates`, and `static` folders exist in the project root.

**5. Run the Application**

Use the Flask command to start the development server.
```bash
flask run
```
**6. Access in Your Browser**

Open your browser and navigate to the following URL:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## API Usage

The API consists of two main endpoints:

**1. File Upload**

- URL: `/files`

- Method: `POST`

- Body (form-data):

  - `file`: The `.csv` file to be uploaded.

- Success Response (201 Created):
  ```bash
  {
  "message": "File uploaded successfully!",
  "file_id": "a1b2c3d4-e5f6-7890-a1b2-c3d4e5f67890"
  }
  ```
  
**2. File Analysis**

- URL: `/files/<file_id>/analysis`

- Method: `POST`

- URL Parameter:

  - `file_id`: The ID returned by the upload endpoint.

- Body (form-data):

  - `coluna_produto`: Name of the product column.

  - `coluna_preco`: Name of the price column.

  - `coluna_quantidade`: Name of the quantity column.

  - `coluna_cliente`: Name of the customer column.

**Success Response (200 OK):**

```bash
{
  "total_revenue": 15300.0,
  "best_selling_product": "Mouse",
  "top_spending_customer": 501,
  "total_transactions": 9
}
```
  


