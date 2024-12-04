from .repositories import ProductRepository

class ProductService:
    @staticmethod
    def list_products():
        return ProductRepository.get_all_products()

    @staticmethod
    def retrieve_product(product_id):
        return ProductRepository.get_product_by_id(product_id)

    @staticmethod
    def create_new_product(data):
        return ProductRepository.create_product(data)

    @staticmethod
    def modify_product(product_id, data):
        product = ProductRepository.get_product_by_id(product_id)
        if product is not None:
            return ProductRepository.update_product(product, data)
        return None

    @staticmethod
    def remove_product(product_id):
        product = ProductRepository.get_product_by_id(product_id)
        if product is not None:
            ProductRepository.delete_product(product)
            return True
        return False