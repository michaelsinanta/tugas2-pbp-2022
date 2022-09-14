from django.test import TestCase
from katalog.models import CatalogItem;
# Create your tests here.

def katalogTest(TestCase):
    def SetKatalog(self):
        CatalogItem.object.create(
            item_name = "Blender Daging Mito",
            item_price = 665,
            item_stock = 10,
            description = "Mampu menggiling daging hingga halus dan bumbu--bumbu dapur",
            rating = 10,
            item_url = "https://shopee.co.id/Mito-CH-200-Chopper-2-Liter-Blender-Daging-Bumbu-Dapur-Serbaguna-Lowatt-i.162626293.6303392934"
        )
    def Katalog_should_same(self):
        # Unit Testing
        CatalogObject = CatalogItem.object.get(
            item_name = "Blender Daging Mito",
            item_price = 665,
            item_stock = 10,
            description = "Mampu menggiling daging hingga halus dan bumbu--bumbu dapur",
            rating = 10,
            item_url = "https://shopee.co.id/Mito-CH-200-Chopper-2-Liter-Blender-Daging-Bumbu-Dapur-Serbaguna-Lowatt-i.162626293.6303392934"
        )
        # Functional Testing
        self.assertEqual(CatalogObject.item_name, "Blender Daging Mito");
        self.assertEqual(CatalogObject.item_price, 665);
        self.assertEqual(CatalogObject.item_stock, 10);
        self.assertEqual(CatalogObject.description, "Mampu menggiling daging hingga halus dan bumbu--bumbu dapur");
        self.assertEqual(CatalogObject.rating, 10);
        self.assertEqual(CatalogObject.item_url, "https://shopee.co.id/Mito-CH-200-Chopper-2-Liter-Blender-Daging-Bumbu-Dapur-Serbaguna-Lowatt-i.162626293.6303392934");
