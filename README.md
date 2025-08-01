## DATA INTEGRATION PROJECT

## Topic:
Compiling data on past and ongoing armed conflicts with commodity prices.

## Project Goal:
The goal of the project is to present two heterogeneous datasets—concerning armed conflicts and commodity prices—and to find relationships in seemingly unrelated data. The project analyzes how commodity prices may be linked to the intensity of armed conflicts based on historical data
	
## Project Description
The project is based on two datasets:
**Armed conflicts: https://www.prio.org/data/4**
  Contains information about past and ongoing conflicts, their locations, durations, intensities, and involved parties.
**Commodity prices: https://www.worldbank.org/en/research/commodity-markets**
  Selected dataset with prices of individual commodities for each year in the range 1960–2025.
  
## Features
The project integrates data on armed conflicts and commodity prices, offering advanced analytical and visualization tools. Key system features include:

- **1. Main dashboard**

	- Presents a summary of the number of years with commodity and conflict data, the latest available years, and the historical data range.
	- Aggregates statistics from both datasets and enables a quick overview of the database status.


  	<img width="1915" height="264" alt="image" src="https://github.com/user-attachments/assets/981e4924-11c3-45b5-b9d4-99e9986105b2" />


- **2. Commodity dashboard**


	- List of available commodities (e.g., oil, gas, metals, agricultural products) and visualization of their prices over time.
	- Dynamic data fetching for the selected commodity for charts and analyses.


  	<img width="1920" height="865" alt="image" src="https://github.com/user-attachments/assets/ffbbb786-251a-4fd0-b294-6333f315dfbc" />

- **3. Conflict dashboard**
	- Statistics on armed conflicts by year, type, and intensity level.
	- Graphical data representation.
   
	<img width="1920" height="502" alt="image" src="https://github.com/user-attachments/assets/49d1d6ec-fd80-43e4-bb1a-048e9f43f5c6" />
 
	<img width="1920" height="897" alt="image" src="https://github.com/user-attachments/assets/5d5560db-cd29-4ead-ab63-fbe7095ecaa0" />

   
- **4. REST API for dashboards**
	- API for retrieving commodity and conflict data, used by the frontend for dynamic visualizations
   
	<img width="1047" height="544" alt="image" src="https://github.com/user-attachments/assets/d6c5f8d0-1c56-469c-8a4c-7f8403189e38" />

 
- **5. Tables and reports**
	- Browse tables with commodity data, conflict data, or their joined reports (e.g., by year).
	- Select displayed columns.
	- Search by name.
   
	<img width="1186" height="677" alt="image" src="https://github.com/user-attachments/assets/fd4b5c2c-c9b7-40c1-99fc-d57542d3fbd9" />

		
- **6. Data export**
	- Select data range for export.
	- Export to JSON or XML format—the user chooses the output format.
	- Export includes both raw table data and joined data (e.g., by year).

 
- **6. Correlations and visualizations**
	- Dynamically generate charts of commodity prices against the number of conflicts over the years.
	- Automatically generate a heatmap of correlations between the number and intensity of conflicts and the prices of selected commodities

   <img width="1186" height="677" alt="image" src="https://github.com/user-attachments/assets/d8bea517-a9c6-4fa3-b8f2-b19cb2851e67" />
   
   <img width="1435" height="567" alt="image" src="https://github.com/user-attachments/assets/54fef23f-b702-4c9a-89dd-b95ca5db1a05" />


   
- **7. User management**
	- User registration, login, and logout.
	- Access to key features requires authorization (login-protected views).
	- Admin panel available at http://127.0.0.1:8000/admin/
		
- **8. Transactions with isolation level control**
	- Transaction mechanisms with the ability to set isolation level, read-only mode, and query timeout.
	
	
### **Technologies**
- **Backend:** Django (Python)
- **Frontend:** JavaScript (szablony Django)
- **Database:** PostgreSQL
- **API:** Django REST Framework (REST API)
- **Authentication:** Django Auth, Django Admin Panel
- **ORM:** Django ORM
- **Dependency management:** pip, requirements.txt
	
### **How to run the project**


> **Looking for a containerized setup?**  
> See the [`docker` branch](https://github.com/jagfoljersolen/data-integration-project/tree/docker) for Docker and Docker Compose deployment instructions.

**1. Clone the project from GitHub https://github.com/jagfoljersolen/data-integration-project** 
	
	git clone https://github.com/jagfoljersolen/data-integration-project.git	
 	cd data-integration-project
		
**2. Create and activate a virtual environment**
		
	python -m venv venv
	source venv/bin/activate 	# Linux/macOS
	venv\Scripts\activate 		# Windows
		
**3. Install dependencies**
		
	pip install -r requirements.txt
		
**4. Configure the database:**	

    *Log in to PostgreSQL (e.g., via terminal command):*

    psql -U postgres

*Create the database:*

    CREATE DATABASE integration_db;

*Create a user with a password:*

    CREATE USER db_user WITH PASSWORD 'integration';

*Grant privileges to the user:*

    GRANT ALL PRIVILEGES ON DATABASE integration_db TO db_user;

*Exit psql:*

    \q

*Ensure your settings.py file has the following configuration:*

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'integration_db',
            'USER': 'db_user',
            'PASSWORD': 'integration',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

   		
**5. Run migrations:**
   		
   	python manage.py migrate
   		
**6. Initialize the database**
   	
   	python manage.py import_commodity_with_units data/commodity_with_units.csv
	python manage.py import_conflicts data/conflicts.csv --batch-size 1000
		
**7. (Optional) Create an admin account**
		
	python manage.py createsuperuser
		
**8. Start the server**
		
	python manage.py runserver
		
**9. Open the application in your browser**
	
	http://127.0.0.1:8000/
		
	
   		
		
	

	
	
		
		
