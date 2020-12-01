from flask import Blueprint
from SellWhoop.models import Product

products = Blueprints('products',__name__)
@products.route('/')
def index():
  all_products = product.query.all()
  return "all the the products"

@products.route('/<int:product_id>')
def details(product_id):
  product = product.query.get_or_404(product_id)
  return product.name

