from sqlalchemy.orm import Session
from src.models import Product

# Insertar o actualizar productos
def upsert_product(db: Session, product_data):
    product = db.query(Product).filter_by(product_id=product_data["product_id"]).first()
    
    if product:
        product.title = product_data["title"]
        product.price = product_data["price"]
        product.store_id = product_data["store_id"]
    else:
        product = Product(**product_data)
        db.add(product)
    
    db.commit()
    return product

# Obtener todos los productos
def get_products(db: Session):
    return db.query(Product).all()
