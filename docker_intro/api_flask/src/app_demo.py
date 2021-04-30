from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


app = Flask(__name__)

#----------[ Conexión a la base de datos del contenedor mysql_demo: 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://apiuser:apiuser001@mysql_demo/agro_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#---------- Conexión a la base de datos del contenedor mysql_demo ]


#----------[ Modelo y Esquema  de las tablas a consultar con SQLAlchemy:
class Products(db.Model):
	__tablename__ = "products"
	id = db.Column(db.Integer, primary_key=True)
	date  = db.Column(db.String(10))
	commodity_name = db.Column(db.String(100))
	variety = db.Column(db.String(100))
	low_price = db.Column(db.Float)
	high_price = db.Column(db.Float)
	mid_price = db.Column(db.Float)

	def __repr__(self):
		return '<Output %d>' % self.id
    
class ProductsSchema(ModelSchema):
	class Meta(ModelSchema.Meta):
		model = Products
		sqla_session = db.session
	# id = fields.Number(dump_only=False)
	date  = fields.String(required=False)
	commodity_name = fields.String(required=False)
	variety = fields.String(required=False)
	low_price = fields.Number(required=False)
	high_price = fields.Number(required=False)
	mid_price = fields.Number(required=False)
#---------- Modelo y Esquema  de las tablas a consultar con SQLAlchemy ]


# product_schema = ProductsSchema()
products_schema = ProductsSchema(many=True)


#----------[ Metodo para probar funcionamiento de la API:
@app.route("/", methods=["GET"])
def ping():
    return jsonify({"response": "Prueba API REST / Demo"})
#---------- Metodo para probar funcionamiento de la API ]


#----------[ Metodo que ejecuta query a la base de datos y retorna la info. en formato JSON:
@app.route('/products', methods=['GET'])
def get_products():    
    get_products = Products.query.all()    
    products = products_schema.dump(get_products)
    return make_response(jsonify({"products": products}))
#---------- Metodo que ejecuta query a la base de datos y retorna la info. en formato JSON ]


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=4002, debug=True)    