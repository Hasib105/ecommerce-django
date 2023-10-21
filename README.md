# Ecommerce Django Project

This is a Django project for an ecommerce website.


## Project Structure

The project structure is as follows:

```
ecommerce/
├── ecommerce/
├── shop/
├── static/
├── tailwind/
├── db.sqlite3
├── manage.py
└── Pipfile
```

- `ecommerce/`: Contains the project settings and URL configurations.
- `shop/`: Contains the product catalog functionality.
- `static/`: Contains the static files (CSS, JS, images, etc.).
- `tailwind/`: Contains the configurations for TailwindCSS and custom themes.
- `db.sqlite3`: The SQLite database file.
- `manage.py`: The Django management script.
- `Pipfile`: The Python dependencies.

## Run Local Developement Server

To run the development server, follow these steps:

1. Clone the repository by running the following command:

   ```
   git clone https://github.com/Hasib105/ecommerce-django-.git
   ```

2. Navigate to the project directory:

   ```
   cd ecommerce-django-
   ```

3. Install pipenv if you haven't already:

   ```
   pip install pipenv
   ```

4. Create a virtual environment and install the dependencies:

   ```
   pipenv install
   ```

5. Activate the virtual environment:

   ```
   pipenv shell
   ```

6. Navigate to the `tailwind/` directory and run the following command to watch for Tailwind CSS changes:

   ```
   npm run tailwind-watch
   ```

7. In a new terminal window, navigate to the project directory and run the following command to start the Django development server:

   ```
   python manage.py runserver
   ```

8. Open your web browser and go to `http://localhost:8000` to view the website.

## Git Operations

### Cloning the Repository

To clone the repository, run the following command:

```
git clone https://github.com/Hasib105/ecommerce-django-.git
```

### Pulling Changes

To pull the latest changes from the repository, run the following command:

```
git pull
```

### Pushing Changes

To push your changes to the repository, run the following commands:

```
git add .
git commit -m "Your commit message"
git push
```

## Contributing

To contribute to the project, follow these steps:

1. Fork the repository.
2. Clone your forked repository.
3. Create a new branch for your changes.
4. Make your changes and commit them.
5. Push your changes to your forked repository.
6. Create a pull request to merge your changes into the main repository.