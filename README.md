# Geo Plant - Plant Catalog System 
Web application developed with Django, integrated with SQLite, to manage and register plants. The system allows users to register, manage, and monitor botanical information, location, life cycle, photos, and other relevant data about plants.

<p align="center">
  <img src="static/assets/geoplant.png" alt="GeoPlant Logo" />
</p>

## Features
- Plant registration and editing with detailed botanical data
- Geographic location recording via GPS coordinates
- Photo upload and management for plants
- Advanced search and filtering by species, location, and status
- Life cycle tracking and event monitoring (flowering, pruning, etc.)
- Support for multiple users with different permission levels
- Efficient CRUD aligned with all the system's operational logic

## Technologies and Dependencies
- Backend: Django 5.x
- Database: SQLite (native to the Django framework)
- Language: Python 3.12+
- Frontend: Django Templates
- ORM: Django ORM
- APIs: Django Rest Framework(in development)

## Installation

```bash
git clone https://github.com/YOURUSERHERE/geo-plant.git
cd geo-plant
```
Create and activate the virtual environment:
```bash
# On Linux/macOS
python -m venv venv
source venv/bin/activate  

# On Windows
python -m venv venv
venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
```
Run migrations:
```bash
python manage.py migrate
```
Start the development server:

```bash
python manage.py runserver
```
Access the system at: http://localhost:8000


## Contribute to this project
- Fork the repository
- Create a branch for your feature:
- Make clear and small commits
- Open a Pull Request describing your contribution
````bash
git checkout -b your-feature
````
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
