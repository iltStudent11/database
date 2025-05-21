# Customer Database FastAPI Service

This project is a Python FastAPI web service for managing customer orders and addresses, backed by a MySQL database.

## Features
- Get a customer by ID
- Get all customers
- Get all addresses for a customer
- Get all orders for a customer
- Add an address for a customer
- Add an order for a customer

## Tech Stack
- Python 3.10+
- FastAPI
- SQLAlchemy
- Pydantic
- MySQL

## Setup
1. Create a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Set up your MySQL database using `schema.sql` (to be provided).
4. Configure your database connection in `main.py` or a `.env` file.
5. Run the API:
   ```powershell
   uvicorn main:app --reload
   ```

## Endpoints
- `GET /customers/{customer_id}`: Get a customer by ID
- `GET /customers`: Get all customers
- `GET /customers/{customer_id}/addresses`: Get all addresses for a customer
- `GET /customers/{customer_id}/orders`: Get all orders for a customer
- `POST /customers/{customer_id}/addresses`: Add an address for a customer
- `POST /customers/{customer_id}/orders`: Add an order for a customer

## Notes
- Ensure MySQL is running and accessible.
- Update connection strings as needed.
