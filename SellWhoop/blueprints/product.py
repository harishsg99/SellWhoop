from flask import Blueprint

products = Blueprints('products',__name__)
@products.route('/')
def index():
  return "all the the products"
@products.route('/<int:product_id>')
def details(product_id):
  return "product details" 
