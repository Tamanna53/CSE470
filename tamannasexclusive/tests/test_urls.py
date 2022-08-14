from itertools import product
from django.test import  SimpleTestCase
from django.urls import reverse,resolve
from banglakart.views import home
from store.views import store,product_detail,search
from carts.views import cart,add_cart,remove_cart,remove_cart_item,checkout,success
from accounts.views import register,login,logout

class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url=reverse('home')
        self.assertEquals(resolve(url).func,home)
    def test_store_url_is_resolved(self):
        url=reverse('store')
        self.assertEquals(resolve(url).func,store)
    def test_search_url_is_resolved(self):
        url=reverse('search')
        self.assertEquals(resolve(url).func,search)
    def test_cart_url_is_resolved(self):
        url=reverse('cart')
        self.assertEquals(resolve(url).func,cart)
    def test_add_cart_url_is_resolved(self):
        url=reverse('add_cart',args=[1])
        self.assertEquals(resolve(url).func,add_cart)
    def test_remove_cart_url_is_resolved(self):
        url=reverse('remove_cart',args=[1])
        self.assertEquals(resolve(url).func,remove_cart)
    def test_remove_cart_item_url_is_resolved(self):
        url=reverse('remove_cart_item',args=[1])
        self.assertEquals(resolve(url).func,remove_cart_item)
    def test_checkout_url_is_resolved(self):
        url=reverse('checkout')
        self.assertEquals(resolve(url).func,checkout)
    def test_success_url_is_resolved(self):
        url=reverse('success')
        self.assertEquals(resolve(url).func,success)
    def test_register_url_is_resolved(self):
        url=reverse('register')
        self.assertEquals(resolve(url).func,register)
    def test_login_url_is_resolved(self):
        url=reverse('login')
        self.assertEquals(resolve(url).func,login)
    def test_logout_url_is_resolved(self):
        url=reverse('logout')
        self.assertEquals(resolve(url).func,logout)
   


    
 
    
   
    
