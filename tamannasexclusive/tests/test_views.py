from django.test import TestCase,Client
class TestViews(TestCase):
 def setUp(self):
  self.c=Client()
 def test_home(self):
  response=self.c.post('/')
  self.assertEqual(response.status_code,200)
 def test_home_template(self):
    response=self.c.post('/')
    self.assertTemplateUsed(response,'home.html')
 def test_home_context(self):
    response=self.c.post('/')
    self.assertEqual(response.context['products'].count(),0)
 def test_home_context_2(self):
    response=self.c.post('/')
    self.assertEqual(response.context['products'].count(),0)
 def test_store(self):
  response=self.c.post('/store/')
  self.assertEqual(response.status_code,200)
 def test_category(self):
    response=self.c.post('/store/category/jackets')
    self.assertEqual(response.status_code,301)
 def test_cart(self):
    response=self.c.post('/cart')
    self.assertEqual(response.status_code,301)
 def test_checkout(self):
    response=self.c.post('/cart/checkout')
    self.assertEqual(response.status_code,301)
 def test_search(self):
    response=self.c.post('/search')
    self.assertEqual(response.status_code,404)
 def test_login(self):
    response=self.c.post('/accounts/login')
    self.assertEqual(response.status_code,301)
    
 def test_logout(self):
        response=self.c.post('/accounts/logout')
        self.assertEqual(response.status_code,301)
 def test_register(self):
     response=self.c.post('/accounts/register')
     self.assertEqual(response.status_code,301)
 def test_place_order(self):
        response=self.c.post('/checkout/success')
        self.assertEqual(response.status_code,404)
 

        
















 
  
        