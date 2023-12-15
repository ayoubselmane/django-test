# Project Documentation

## Introduction
This document provides an overview of the steps to set up and run the project.

## Steps
1. **Clone the Repository:** 
    ```
    git clone <repository_URL>
    ```

2. **Create a Virtual Environment:** 
    ```
    conda create -n yourenvname
    ```

3. **Navigate to the Cloned Folder:** 
    ```
    cd <folder_name>
    ```

4. **Install Required Packages:** 
    ```
    pip install -r requirement.txt
    ```

5. **Set Up Environment Variables:**
    - Create a `.env` file in the `receipt_tracker` directory.
    - Add the following credentials for a PostgreSQL database (uncomment in `settings.py` under `DATABASES`):
        ```
        SECRET_KEY=django-insecure-728k0bs%91o$^sp%aa_ji@2fmtwpdk7r1na#*$%l2+%)7tnpo3 
        DB_NAME=database_name 
        DB_USER=database_user 
        DB_PASSWORD=database_password 
        DB_HOST=localhost 
        DB_PORT=5432
        ```

6. **Run the Development Server:** 
    ```
    python manage.py runserver
    ```

7. **To Run on Local Network:** 
    ```
    python manage.py runserver 0.0.0.0:8000
    ```

8. **Add Your Local IP to Allowed Hosts:** 
    - Modify `settings.py` and add your IP address (e.g., `192.168.1.10`) to the `ALLOWED_HOSTS` list to enable network access:
        ```python
        ALLOWED_HOSTS = [
            'localhost',
            '127.0.0.1',
            '192.168.1.10',  # Add your IP here
        ]
        ```

## Conclusion
Follow these steps to effectively set up and run the project on your local machine or network.
