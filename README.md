# To run the application:

    `docker-compose up`

## Users, patients and doctor are automatically created in the database

## After the application is up and running, you can access the application at:

    `http://localhost:8000`

## Also you can access the admin panel at:

    `http://localhost:8000/admin`

## You can log in through only through the doctor account

### Aziz Doctor:

    `login: AA1112233` 

    `password: 1`


# API

#### List of patients: [http://127.0.0.1:8000/api/v1/patients/](http://127.0.0.1:8000/api/v1/patients/)

#### Get patient form: [http://127.0.0.1:8000/api/v1/doctors/{patient_id}/appointment-form/](http://127.0.0.1:8000/api/v1/doctors/2/appointment-form/)
#### form is selected depending on age

#### Create appointment: [http://127.0.0.1:8000/api/v1/patients/appointments/](http://127.0.0.1:8000/api/v1/patients/appointments/)

#### List of appointments for patient: http://127.0.0.1:8000/api/v1/patients/2/appointments/
