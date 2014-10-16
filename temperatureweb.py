from flask import Flask, render_template
from flask.ext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'temperature'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)

@app.route('/')
def main():
    cursor = mysql.connect().cursor()
    cursor.execute("Select * from temps order by time desc")
    data = [dict(time=row[0], degc=row[1], degf=row[2]) for row in cursor.fetchall()]
    return render_template('temps.html', data=data)

if __name__ == "__main__":
    app.debug = True
    app.run()

