# Rule Validation API

This is a simple API for validating rules.

## Installation

### Locally

1.  Clone the repository:

    ```bash
    git clone https://github.com/chiefcookandbottlewasher/rule-validation-api.git
    ```
2.  Navigate to the project directory:

    ```bash
    cd rule-validation-api
    ```
3.  Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```
4.  Activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```
5.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```
6.  Run the application:

    ```bash
    python app.py
    ```

### Via Docker

1.  Clone the repository:

    ```bash
    git clone https://github.com/chiefcookandbottlewasher/rule-validation-api.git
    ```
2.  Navigate to the project directory:

    ```bash
    cd rule-validation-api
    ```
3.  Build the Docker image:

    ```bash
    docker build -t rule-validation-api .
    ```
4.  Run the Docker container:

    ```bash
    docker-compose up -d
    ```

## Usage

The API is available on port 5000.

### Endpoints

*   `/rules`: Returns a list of rules.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.