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
# Build and run the application using Docker
docker-compose up --build
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