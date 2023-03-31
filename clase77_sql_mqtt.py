import paho.mqtt.client as mqtt
import struct
import mysql.connector as mysql

def conectado(cliente,userdata,flags,rc):
    if rc == 0:
        print("Conectado OK")
        cliente.subscribe("demo")
    else:
        print("No conectado")
        
def receptor(cliente,userdata,mensaje):
    datos =  struct.unpack("ff",mensaje.payload)
    valores = [round (datos[0],2),round(datos[1],2)]
    cursor.execute(query,valores)
    db.commit()
    print(datos)

cliente = mqtt.Client()
cliente.connect("192.168.0.35",1883)

db = mysql.connect(host="192.168.0.35",user="eugenio",passwd="1234",database="pruebas")
cursor = db.cursor()
query = "INSERT INTO prueba3 (v1,v2) VALUE (%s,%s)"

cliente.on_connect = conectado
cliente.on_message =  receptor

cliente.loop_forever()