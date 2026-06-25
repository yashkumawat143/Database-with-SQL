# Flipkart Login System 🛒

## About Project
A simple Python project with:
- User Registration
- User Login
- MySQL Database

## Project Files
| File | Work |
|------|------|
| `app.py` | Database connection, save user, search user |
| `main.py` | Menu, Register, Login |

## Requirements
- Python 3.x
- MySQL
- mysql-connector-python

## Installation
pip install mysql-connector-python

## Database Setup
Step 1 - Create Database:
CREATE DATABASE hit-db-demo;

Step 2 - Create Table:
CREATE TABLE users (
  id       INT AUTO_INCREMENT PRIMARY KEY,
  name     VARCHAR(100),
  email    VARCHAR(100),
  password VARCHAR(100)
);

## How To Run
python main.py

## How It Works
1. Run the program
2. Choose Register or Login
3. Enter your details
4. Done!
