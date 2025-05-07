# Django REST Framework Patient Record API with Data Masking

This project implements a simple Patient Record API using Django REST Framework. A key feature is the **masking of sensitive patient data** (specifically, the `name` and `diagnosis` fields) when creating new records via the API endpoint. The masking is performed using the **Faker** library, replacing the real data with fake, plausible-looking information before saving it to the database.

