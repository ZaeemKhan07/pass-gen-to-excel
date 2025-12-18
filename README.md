# Py-Password-Excel-Saver

A simple but effective Python-based password generator that creates strong, random passwords based on user-defined criteria. Generated passwords and their corresponding parameters are automatically saved to an Excel spreadsheet (`passwords.xlsx`) for easy tracking and management.

This project is containerized using Docker for easy and consistent deployment across different environments.

## Features

-   **Customizable Passwords**: Specify the desired number of letters, symbols, and numbers.
-   **Strong & Random**: Generates securely randomized passwords by shuffling all character types.
-   **Automatic Logging**: Saves every generated password and its parameters (number of letters, symbols, numbers) to `passwords.xlsx`.
-   **Dockerized**: Includes a `Dockerfile` and `docker-compose.yml` for quick and easy setup.

## Getting Started

You can run this project in two ways: using Docker (recommended) or by setting up a local Python environment.

### Prerequisites

-   For the Docker method: [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/) must be installed.
-   For the local method: [Python 3.9+](https://www.python.org/downloads/) and `pip` must be installed.

### Option 1: Running with Docker (Recommended)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/py-password-excel-saver.git
    cd py-password-excel-saver
    ```

2.  **Build and run the container:**
    Use Docker Compose to build the image and start the service in one command:
    ```bash
    docker-compose up --build
    ```

3.  **Follow the prompts:**
    The application will start, and you can enter your desired password criteria directly in the terminal.

### Option 2: Running Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/py-password-excel-saver.git
    cd py-password-excel-saver
    ```

2.  **Install the dependencies:**
    This project requires `pandas` and `openpyxl`. Install them using pip:
    ```bash
    pip install pandas openpyxl
    ```

3.  **Run the script:**
    Execute the `main.py` script:
    ```bash
    python main.py
    ```

## How It Works

When you run the application, you will be prompted for the following:
1.  **Number of letters**
2.  **Number of symbols**
3.  **Number of numbers**

The script then generates a password, prints it to the console, and saves it to a file named `passwords.xlsx` in the project's root directory. If the file already exists, the new password will be appended to it.

### Project Structure
```
.
├── Dockerfile
├── docker-compose.yml
├── main.py
└── saving_password.py
```
- **`main.py`**: The main script that takes user input and generates the password.
- **`saving_password.py`**: Contains the logic for saving the generated password data to an Excel file.
- **`Dockerfile`**: Defines the container image for the application.
- **`docker-compose.yml`**: Configures the Docker service for easy execution.

## Contributing
Contributions are welcome! If you have suggestions for improvements, please feel free to open an issue or submit a pull request.
