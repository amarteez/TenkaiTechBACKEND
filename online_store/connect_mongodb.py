from mongoengine import Document, StringField, DecimalField, ReferenceField, ImageField, URLField, connect

# Conectar a MongoDB (asegúrate de usar la misma URI de conexión que en settings.py)
connect(
    db='tenkaitechDB',
    host='mongodb+srv://anelmartez18:NPsCQPVYRHhhOczM@tenkaitechdb.o8qlj.mongodb.net/?retryWrites=true&w=majority&appName=tenkaitechDB',
    alias='default'
)

# Definir los modelos (deberías haber definido estos modelos en otro archivo o importarlos)
class Category(Document):
    name = StringField(max_length=255)

class Product(Document):
    category = ReferenceField(Category)
    name = StringField(max_length=255)
    description = StringField()
    price = DecimalField()
    image = ImageField(null=True, blank=True)
    image_url = URLField(null=True, blank=True)

class CartItem(Document):
    product = ReferenceField(Product)
    quantity = DecimalField()

def test_mongodb_operations():
    try:
        # Crear un nuevo documento
        category = Category(name="Electronics")
        category.save()

        product = Product(
            category=category,
            name="Smartphone",
            description="A high-end smartphone",
            price=699.99,
        )
        product.save()

        # Consultar documentos
        products = Product.objects(category=category)
        print("Products in category:", products)

        # Verifica que los documentos estén correctamente guardados
        print("Saved Category:", Category.objects(name="Electronics").first())
        print("Saved Product:", Product.objects(name="Smartphone").first())
        
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    test_mongodb_operations()
