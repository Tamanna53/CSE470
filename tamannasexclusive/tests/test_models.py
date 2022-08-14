from itertools import product
from django.test import TestCase
from django.urls import reverse
from accounts.models import Account
from store.models import Product
from carts.models import Cart,CartItem
from category.models import Category

class TestModels(TestCase):
   #testing cart model
    def test_cart_model(self):
        cart=Cart.objects.create(cart_id='1234567890')
        self.assertEqual(cart.cart_id,'1234567890')
    
    #testing Category model
    def test_category_model(self):
        category=Category.objects.create(category_name='test')
        self.assertEqual(category.category_name,'test')
    def test_category_model_2(self):
        category=Category.objects.create(category_name='test')
        self.assertEqual(category.category_name,'test')
    def test_category_model_slug(self):
        category=Category.objects.create(slug='test')
        self.assertEqual(category.slug,'test')
    def test_category_model_desc(self):
        category=Category.objects.create(description='test description about the product')
        self.assertEqual(category.description,'test description about the product')
    def test_category_model_image(self):
        category=Category.objects.create(cat_image='test image')
        self.assertEqual(category.cat_image,'test image')

    #Testing Account model
    def test_account_model(self):
        account=Account.objects.create(username='test')
        self.assertEqual(account.username,'test')
    def test_account_first_name_model(self):
        account=Account.objects.create(first_name='Alpha')
        self.assertEqual(account.first_name,'Alpha')
    def test_account_last_name_model(self):
        account=Account.objects.create(last_name='Beta')
        self.assertEqual(account.last_name,'Beta')
    def test_account_phone_model(self):
        account=Account.objects.create(phone_number=1234567890)
        self.assertEqual(account.phone_number,1234567890)
    def test_account_email_model(self):
        account=Account.objects.create(email="bravo@gmail.com")
        self.assertEqual(account.email,"bravo@gmail.com")
    def test_account_address_model(self):
        account=Account.objects.create(is_admin=True)
        self.assertEqual(account.is_admin,True)
   


    