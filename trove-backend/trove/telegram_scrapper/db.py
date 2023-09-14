from entities import Product


class Database:
    def __init__(self):
        self.products = {}

    def save(self, product: Product):
        if product.id in self.products:
            product.images.extend(self.products[product.id].images)
                
        self.products[product.id] = product
    
    def to_json(self):
        return {
            'products': [product.to_json() for product in self.products.values()]
        }
    
    def __str__(self) -> str:
        return str(self.products)


            