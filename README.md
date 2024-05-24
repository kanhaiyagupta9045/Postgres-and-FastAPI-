# Bank and Branch Management API

This is a FastAPI project to manage banks and their branches using PostgreSQL and SQLAlchemy.

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy (async)

## Requirements

- Python 3.7+
- PostgreSQL

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the PostgreSQL database and update the database URL in your environment variables:
    ```sh
    DATABASE_URL=postgresql+asyncpg://username:password@localhost/dbname
    ```

## Database Models

### Bank
- id: Integer, Primary Key
- name: String(49), Unique, Not Null
- branches: Relationship to `Branch`

### Branch
- ifsc: String(11), Primary Key
- bank_id: Integer, Foreign Key to `banks.id`
- branch: String(74), Not Null
- address: String(195), Not Null
- city: String(50), Not Null
- district: String(50), Not Null
- state: String(26), Not Null
- bank: Relationship to `Bank`

## Pydantic Schemas

### BranchBase
- ifsc: str
- bank_id: int
- branch: str
- address: str
- city: str
- district: str
- state: str

### BranchCreate (inherits BranchBase)
### Branch (inherits BranchBase)
  - orm_mode: True

### BankBase
- name: str

### BankCreate (inherits BankBase)
### Bank (inherits BankBase)
  - id: int
  - branches: List[Branch]
  - orm_mode: True

## API Endpoints

### Create Bank
- **URL:** `/create_bank/`
- **Method:** `POST`
- **Request Body:** `BankCreate`
- **Response:** `Bank`
- **Description:** Creates a new bank.

### Read Banks
- **URL:** `/read_banks/`
- **Method:** `GET`
- **Response:** `List[BankCreate]`
- **Description:** Reads all banks.

### Create Branch for Specific Bank
- **URL:** `/create_branch/`
- **Method:** `POST`
- **Request Body:** `BranchCreate`
- **Response:** `Branch`
- **Description:** Creates a branch for a specific bank.

### Read Branch by Bank ID
- **URL:** `/branch/{id}`
- **Method:** `GET`
- **Response:** `BranchSchema`
- **Description:** Reads branch details for a specific bank ID.

## Example Usage

### Create a Bank

```sh
curl -X POST "http://127.0.0.1:8000/create_bank/" -H "Content-Type: application/json" -d '{"name": "State Bank of India"}'
