# Ecommerce Django Project

This is a Django project for an ecommerce website.


## Project Structure

The project structure is as follows:

```
ecommerce/
├── ecommerce/
├── shop/
├── static/
├── db.sqlite3
├── manage.py
├── package.json
├── Pipfile
└── tailwind.config.js
```

- `ecommerce/`: Contains the project settings and URL configurations.
- `shop/`: Contains the product catalog functionality.
- `static/`: Contains the static files (CSS, JS, images, etc.).
- `db.sqlite3`: The SQLite database file.
- `manage.py`: The Django management script.
- `package.json`: NPM dependencies.
- `Pipfile`: Python dependencies.
- `tailwind.config.js`: Tailwind CSS configurations.

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

6. Install the NPM dependencies:

   ```
   npm install
   ```

6. Run the following command to watch for Tailwind CSS changes:

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

## Misc

- To auto reload development server on html change, [django-browser-reload](https://github.com/adamchainz/django-browser-reload) package works effectively.
- To format, highlight & autocomplete django templates in vscode, [junstyle.vscode-django-support](https://marketplace.visualstudio.com/items?itemName=junstyle.vscode-django-support) is a decent extension.