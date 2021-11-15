from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/inventarios_jp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

class Item(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50), nullable=False)
    codigo_identificacion=db.Column(db.Integer, nullable=False)
    precio=db.Column(db.Integer, nullable=False)
    categoria=db.Column(db.String(50), nullable=True)
    foto=db.Column(db.String(255), nullable=True)
    descripcion=db.Column(db.String(255), nullable=True)
    anotacion_gerente=db.Column(db.String(255), nullable=True)

    def repr(self) :
        return "[Item %s]" % str(self.id)
db.create_all()

class Empleado(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50), nullable=False)
    codigo_identificacion=db.Column(db.Integer, nullable=False)
    puesto=db.Column(db.String(50), nullable=False)
    rol=db.Column(db.String(50), nullable=False)
    foto=db.Column(db.String(255), nullable=True)
    descripcion=db.Column(db.String(255), nullable=True)
    anotacion_gerente=db.Column(db.String(255), nullable=True)

    def repr(self) :
        return "[Empleado %s]" % str(self.id)
db.create_all()


class IndexItem(Resource):
    def get(self):
        item = Item.query.all()
        response = []
        if item:
            for item in Item:
                response.append({
                "id": item.id,
                "nombre": item.nombre,
                "codigo de identificacion": item.codigo_identificacion,
                "precio": item.precio,
                "categoria": item.categoria,
                "foto": item.foto,
                "descripcion": item.descripcion,
                "anotacion gerente": item.anotacion_gerente
                })
        return {'Items obtenidos': response}, 201

    def post(self):
        itemporcrear = request.get_json()
        item = Item(nombre=itemporcrear['nombre'], codigo_identificacion=itemporcrear['codigo_identificacion'], precio=itemporcrear['precio'], categoria=itemporcrear['categoria'],foto=itemporcrear['foto'],descripcion=itemporcrear['descripcion'],anotacion_gerente=itemporcrear["anotacion_gerente"] )
        db.session.add(item)
        db.session.commit()
        if itemporcrear is None:
            return "Los campos estan vacios", 400
        if (item.nombre) == "":
            return 'Especificar nombre es obligatorio',400
        if str(item.codigo_identificacion) == "":
            return 'Especificar codigo de identificacion es obligatorio', 400 
        if str(item.precio) == "":
            return "Especificar el precio ya que es obligatorio",400
        else:
            return { "response": "Item registrado exitosamente :)!"}, 201

class ItemByID(Resource):
    def get(self,id):
        item = Item.query.filter_by(id=id).first()
        if item == None:
            return ({"Error": "No se encuentran items en la lista con ese id :" + str(id)}),406
        else:
            return{'item': {
                "id": item.id,
                "nombre": item.nombre,
                "codigo de identificacion": item.codigo_identificacion,
                "precio": item.precio,
                "categoria": item.categoria,
                "foto": item.foto,
                "descripcion": item.descripcion,
                "anotacion gerente": item.anotacion_gerente
            }},201
    def put(self,id):
        
        item = Item.query.filter_by(id=id).first()
        datos = request.get_json()
        if item == None:
            return ({"Error:" "No se encuentran items con el id:  " + str (id) + 'por actualizar'}),403
        else:
         item.nombre = datos['nombre']
         item.codigo_identificacion = datos['codigo_identificacion']
         item.precio = datos['precio']
         item.categoria = datos['categoria']
         item.foto = datos["foto"]
         item.descripcion = datos["descripcion"]
         db.session.commit()
         return {"response :" "Item actualizado correctamente"},201
    def delete (self,id):
        item = Item.query.filter_by(id=id).first()
        if item:
            db.session.delete(item)
            db.session.commit()
            return { "response": "Item con id: {item}. Borrado exitosamente. ".format(item=id)}, 203
        else:
            return ({"Error": "No se encuentran items para borrar en la lista con ese id :" + str(id)}),406
    

class IndexEmpleado(Resource):
    def get(self):
        empleado = Empleado.query.all()
        response = []
        if empleado:
            for empleado in Empleado:
                response.append({
                "id": empleado.id,
                "nombre": empleado.nombre,
                "codigo de identificacion": empleado.codigo_identificacion,
                "puesto": empleado.puesto,
                "rol": empleado.rol,
                "foto": empleado.foto,
                "descripcion": empleado.descripcion,
                "anotacion_gerente": empleado.anotacion_gerente
                })
        return {'Empleados obtenidos': response}, 201
   
    def post(self):
        empleadoporcrear = request.get_json()
        empleado = Empleado(nombre=empleadoporcrear['nombre'], codigo_identificacion=empleadoporcrear['codigo_identificacion'], puesto=empleadoporcrear['puesto'], rol=empleadoporcrear['rol'],foto=empleadoporcrear['foto'],descripcion=['descripcion'],anotacion_gerente=empleadoporcrear["anotacion_gerente"] )
        db.session.add(empleado)
        db.session.commit()
        if empleadoporcrear is None:
            return "Los campos estan vacios", 400
        if (empleado.nombre) == "":
            return 'Especificar nombre es obligatorio',400
        if str(empleado.codigo_identificacion) == "":
            return 'Especificar codigo de identificacion es obligatorio', 400 
        if str(empleado.puesto) == "":
            return "Especificar el puesto ya que es obligatorio",400
        if str(empleado.rol) == "":
            return "Especificar el rol ya que es obligatorio",400
        else:
            return { "response": "Empleado registrado exitosamente :)!"}, 201

class EmpleadoByID(Resource):
     def get(self,id):
        empleado = Empleado.query.filter_by(id=id).first()
        if empleado == None:
            return ({"Error": "No se encuentran empleados en la lista con ese id :" + str(id)}),406
        else:
            return{'Empleado': {
                "id": empleado.id,
                "nombre": empleado.nombre,
                "codigo de identificacion": empleado.codigo_identificacion,
                "puesto": empleado.puesto,
                "rol": empleado.rol,
                "foto": empleado.foto,
                "descripcion": empleado.descripcion,
                "anotacion gerente": empleado.anotacion_gerente
            }},201
     def put(self,id):
        
        empleado = Empleado.query.filter_by(id=id).first()
        datos = request.get_json()
        if empleado == None:
            return ({"Error:" "No se encuentran Empleado con el id:  " + str (id) + 'por actualizar'}),403
        else:
         empleado.nombre = datos['nombre']
         empleado.codigo_identificacion = datos['codigo_identificacion']
         empleado.puesto = datos['puesto']
         empleado.rol = datos['rol']
         empleado.foto = datos["foto"]
         empleado.descripcion = datos["descripcion"]
         db.session.commit()
         return {"response :" "Empleado actualizado correctamente"},201
     def delete (self,id):
        empleado = Empleado.query.filter_by(id=id).first()
        if empleado:
            db.session.delete(empleado)
            db.session.commit()
            return { "response": "Empleado con id: {item}. Borrado exitosamente. ".format(item=id)}, 203
        else:
            return ({"Error": "No se encuentran Empleados para borrar en la lista con ese id :" + str(id)}),406







class IndexRoute(Resource):
    def get(self):
        return {'response': 'Mi api de sistema de inventarios :)'},200

api.add_resource(IndexRoute,'/')
api.add_resource(IndexItem,'/item')
api.add_resource(ItemByID, '/item/<int:id>')
api.add_resource(IndexEmpleado, '/empleado')
api.add_resource(EmpleadoByID, '/empleado/<int:id>')