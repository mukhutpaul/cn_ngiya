@echo off
cd \
cd system
cd fardrc

if not exist mediafiles mkdir mediafiles
cd mediafiles
if not exist documents mkdir documents
if not exist face mkdir face
if not exist finger mkdir finger
if not exist photos mkdir photos
if not exist qrcode mkdir qrcode
cd qrcode
if not exist Unite mkdir Unite


 
python manage.py find_justification    
python manage.py runserver 0.0.0.0:80