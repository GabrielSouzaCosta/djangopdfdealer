# djangopdfdealer

This project is an example of how to transform html to pdf files and how to store it on a S3 Bucket, and also returns the url of the file to be acessed.

## Setup

1. Install requirements using: </br>
pip install -r requirements.txt

2. Migrate the database:</br>
python manage.py migrate

3. Setup your AWS Configurations to store the files, for details of how to do it, access the library documentation: </br> https://django-storages.readthedocs.io/en/latest/index.html </br>

4. Run the server: </br>
python manage.py runserver

5. Put your name and test it. 😉
