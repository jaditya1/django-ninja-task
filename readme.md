### Configuring app
1. `sudo docker-compose up`
2. For adding superuser:
  - `sudo docker-compose run api python manage.py createsuperuser`
3. For adding new django app:
  - `sudo docker-compose run api python manage.py startapp SeedMgmt`


### Running developmentweb server
1. `sudo docker-compose up`
2. Api doc swagger url: `http://localhost:8000/api/docs/`