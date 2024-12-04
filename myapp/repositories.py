from .models import Product

class ProductRepository:
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_product_by_id(product_id):
        return Product.objects.filter(id=product_id).first()

    @staticmethod
    def create_product(data):
        return Product.objects.create(**data)

    @staticmethod
    def update_product(product, data):
        for field, value in data.items():
            setattr(product, field, value)
        product.save()
        return product

    @staticmethod
    def delete_product(product):
        product.delete()