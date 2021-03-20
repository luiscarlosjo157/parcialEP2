from flaskext.mysql import MySQL
from src import app
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost' 
app.config['MYSQL_DATABASE_USER'] = 'root' 
app.config['MYSQL_DATABASE_PASSWORD'] = '12345678' 
mysql.init_app(app)
