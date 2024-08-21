# store/models.py
from mongoengine import Document, fields

class Category(Document):
    name = fields.StringField(max_length=255, required=True)

    def __str__(self):
        return self.name

class Product(Document):
    category = fields.ReferenceField(Category, required=True)
    name = fields.StringField(max_length=255, required=True)
    description = fields.StringField()
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    image = fields.ImageField(upload_to='product_images/', null=True, blank=True)
    image_url = fields.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class CartItem(Document):
    product = fields.ReferenceField(Product, required=True)
    quantity = fields.IntField(min_value=1)

    def __str__(self):
        return f'{self.product.name} (x{self.quantity})'
