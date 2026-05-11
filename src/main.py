import json
from bottle import post, run, request


@post('/salvar')
def salvar():
	R = False
	if request.json:
		R = 'Temp' in request.json and 'Luz' in request.json 
		R =  R and 'Equipo' in request.json
        try:
		    conn = mariadb.connect(
                user="db_user",
                password="db_password",
                host="127.0.0.1",
                port=3306,
                database="your_database"
            )
            cur = conn.cursor()
            cur.execute("insert into iot_data values (null,now(),?)",[json.dumps(request.json)])
            R = True
        except mariadb.Error as e:
            print(f"Error connecting: {e}")

	return {"Exito":R}

if __name__ == '__main__':
    run(app=app, 
        host='0.0.0.0', 
        port=443, 
        server='gunicorn', 
        keyfile='server.key', 
        certfile='server.crt')
