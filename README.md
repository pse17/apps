# Приложения
Для установки наберитe  
git clone https://github.com/pse17/apps.git  
cd apps  
pip3 install -r requirements.txt  
uwsgi --http :80 --module apps.wsgi  

Для запуска тестов наберите  
python manage.py test

Для добавления новой записи о приложении наберите
curl -u admin:admin -d "name=App1" 127.0.0.1:/api/add  
где admin:admin имя пользователя и пароль,  
запрос вернет например {name: "Название приложения", apikey:12345}   
apikey - ключ чтобы для доступа к записи о приложении. Например так  
curl -u admin:admin 127.0.0.1:/api/12345  
Для редактирования названия приложения  
curl -u admin:admin -X PUT -H 'Content-Type: application/json' -d '{"name": "Новое название"}' 127.0.0.1:/api/12345  
Для удаления  
curl -u admin:admin -X DELETE 127.0.0.1:/api/12345  
Для вывода списка приложений  
curl -u admin:admin 127.0.0.1:/api/list

