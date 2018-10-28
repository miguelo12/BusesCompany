# BusesCompany

# Es necesario tener instalado virtualenv
>pip install virtualenv

# 1° Instalar los requerimientos
```
cd backend

virtualenv venv (En caso de no tener la carpeta venv ejecutar este script).

venv\Scripts\activate

pip install -r requirements.txt
```
# 2° Correr el servidor(Backend).
```
python manage.py runserver
```

# 3° Correr el frontend.
```
cd frontend

npm install (instalar con npm para la primera vez).

npm run dev
```
#Supuestos
```
    - Se puede iniciar creando trayectos - choferes - pasajeros.
    - Al ingresar trayectos se habilitaran 3 botones. (editar-eliminar-bus)
    - Al ingresar en el boton del bus se puede agregar un nuevo bus y los pasajeros.
    - Es necesario ingresar una matricula con un chofer para poder agregar pasajeros al bus.
```

#Lo que no hace o funciona a medias
```
    - No filtra.
    - Promedio del chart esta a medias.
```
#Lo que se utilizo
```
    Frontend:
    - Vuetify 
        - Vuejs (cli3)
        - Apexchart
        - axios
        - vue2-datepicker
        - vue-router
    
    Backend:
    - Django
        - Django-rest-framework
        - DRFM
        - MongoEngine
        - django-cors-headers
        - markdown

    Base de datos:
    - MongoDB
```

# Vue.js
>Leer README.md en frontend.