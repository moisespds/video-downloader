@echo off
echo Iniciando servidor...

call venv\Scripts\activate
python manage.py runserver

pause