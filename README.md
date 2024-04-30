# ProdTrack

A Django app using SQLite for management and updates of reagent container data

![Screenshot](https://github.com/levina-anna/levina-anna.github.io/raw/main/images/ProdTrack.png)

## DB

- This application interacts directly with a SQLite database for CRUD operations

## Features

- **Data Display**:  Loads and displays data from the SQLite database into an HTML table, allowing users to view details of reagent containers.
- **Interactive Table**: Clicking on a table row triggers a modal form populated with the container's data, enabling quick and intuitive editing.
- **Data Updates**: Changes made in the modal form can be submitted to update the container information in the database.

## Installation and Launch

```bash
git clone <repository-url>
cd <project-directory-name>
# Install dependencies
pip install -r requirements.txt
# Apply database migrations
python manage.py migrate
# Run the application
python manage.py runserver
```

## Initial Data Loading

This project includes an initial data dump in `initial_data.json` that can be used to populate the database with sample data. To load this data into your database, ensure that you have completed all migrations, and then run the following command:

```bash
python manage.py loaddata initial_data.json
```

## Technologies Used

- Django 4.2.5
- Jinja2 3.1.2
- Python 3.11
- JavaScript
- Bootstrap5
- SQLite
- HTML
- CSS