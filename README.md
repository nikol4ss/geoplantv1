## Geo Plant - Plant Catalog System v1

A Django web application for registering and managing plants, with detailed botanical data, photos, and location tracking.

### About

This project is a web application developed with Django and SQLite to manage plant information. Users can register plants, edit botanical details, track life cycles, record GPS locations, and upload photos. The system provides efficient CRUD operations aligned with operational logic, supports advanced search and filtering by species, location, or status, and allows multiple users with different permission levels. Built with Django 5.x, Python 3.12+, Django ORM, and Django templates, the project is structured to expand with APIs via Django Rest Framework.

### Installation

1. Clone the repository
```bash
git clone https://github.com/user/geoplantv1.git
cd geoplantv1
```

2. Create and activate the virtual environment:
```bash
python -m venv venv
source venv/bin/activate  

pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the development server:

```bash
python manage.py runserver
```

5. Access the system at: http://localhost:8000

<br>
<p align="center" style="opacity:0.6;">
MIT License – see the <a href="LICENSE">LICENSE</a> file for details.
</p>
