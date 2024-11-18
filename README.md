## Experiment 1 Developing a Simple Webserver

---
### Date : 18 / 11/ 2024 
### Day : Monday

---
## Aim 

---
To develop a simple webserver to serve html pages and display the configuration details of laptop.


## Design Steps 

---

### Step 1: Install Django
If you haven't installed Django yet, you can do so via pip:

```commandline
pip install django

```

### Step 2: Create a Django Project
Create a new Django project. Let's name the project exerciseProject:

```commandline
django-admin startproject exerciseProject 
cd windows_config_doc
```

### Step 3: Create a Django App
Create a new app inside the project to handle the documentation page. Let's name the app as windowsConfiguration

```commandline
python manage.py startapp windowsConfiguration

```
### Step 4: Add the App to Installed Apps
Open exerciseProject/settings.py and add windowsConfiguration to the INSTALLED_APPS list:

```commandline
INSTALLED_APPS = [
    ...
    'windowsConfiguration',
]
```
### Step 5: Create the Template Directory
Inside the windowsConfig app, create a templates folder and then a windowsConfiguration folder inside it to store out HTML file.

Directory structure should look like this:
```commandline
exerciseProject/
    windowsConfiguration/
        templates/
            windowsConfiguration/
                window.html
    exerciseProject/
        settings.py
        urls.py
    manage.py

```

---
### Step 6: Add the HTML File

Place your Windows configuration HTML content into the window.html file within 

``windowsConfiguration/templates/windowsConfiguration/.``

---

### Step 7: Create a View to Render the HTML File

Now, you need to create a view in windowsConfiguration/views.py to render the HTML file. This view will render the window.html when accessed:

```commandline
from django.shortcuts import render

def show_documentation(request):
    return render(request, 'windowsConfiguration/window.html')

```

---

## Step 8: Define a URL for the Configuration View
Next, create a urls.py file inside the windowsConfiguration  app (if it doesn’t already exist) and define a URL pattern for the view you created.

```commandline
from django.urls import path
from . import views

urlpatterns = [
    path('', views.windowConfig, name='system_info'),
]

```

---

## Step 9: Include the App’s URLs in the Main URL Configuration
Now, open the main urls.py file in the project directory (exerciseProject/urls.py) and include the windowsConfiguration app's URLs:

```commandline
from django.contrib import admin
from django.urls import path , include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('system-info/', include('windowsConfiguration.urls')),
]

```

## Step 10: Run the Development Server
Now that everything is set up, run the Django development server:

```commandline
python manage.py runserver

```

Once the server is running, open a browser and go to:

```commandline
http://127.0.0.1:8000/system_info/

```

This should render the HTML page containing our Windows configuration.

---
# Output 
![image](https://github.com/user-attachments/assets/54a2ca98-8f04-4e6c-859f-d6ea082e4753)

---

# Result
The program for implementing simple webserver is executed successfully.

