from flask import Flask, request, render_template
from markupsafe import escape
from models import Products
from database import session

app = Flask(__name__)

@app.route("/")
def homepage():
    # add_product()
    get_Product()
    return render_template('homepage.html')

@app.route("/hello/")
@app.route("/hello/<name>")
def greet( name = None):
    return render_template('greet.html', name=name)

@app.route("/products/<id>/")
def products(id):
    products = get_Product()
    page = '<h1>Products Get</h1>'
    page+='<ul>'
    for product in products:
        page+=f'<li>{product.name}</li>'
    page+='</ul>'
    return page


# @app.route("/products/<id>/", methods=['GET', 'POST', 'PUT'])
# def products(id):
#     if request.method=='POST':
#         return "This is POST call"
    
#     elif request.method=='PUT':
#         return "This is PUT call"
    
#     else:
#         return render_template('products.html')

@app.route("/about-us/")
def aboutUs():
    return "<p> About Us </p>"

@app.route("/users/", methods=['GET', 'POST'])
def userDetail():
    if request.method=='POST':
        firstName=request.form['fname']
        lastName=request.form['lname']
        return f"<p> User : {firstName} {lastName}</p>"
    elif request.method=="GET":
        firstName=request.args.get['fname']
        lastName=request.args.get['lname']
        return f"<p> User : {firstName} {lastName}</p>"
    

# def add_product():
#     product = Products(name = "Product 1", price = 20, quantity= 10)
#     session.add(product)
#     session.commit()
    
def get_Product():
    return (session.query(Products).all())