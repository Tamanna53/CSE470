from django.test import TestCase,Client
class TestTemplates(TestCase):
    def setUp(self):
        self.c=Client()
    def test_home_template(self):
        response=self.c.post('/')
        self.assertTemplateUsed(response,'home.html')
    def test_home_context(self):
        response=self.c.post('/')
        self.assertEqual(response.context['products'].count(),0)
    def test_home_context_2(self):
        response=self.c.post('/')
        self.assertEqual(response.context['products'].count(),0)
    def test_store_template(self):
        response=self.c.post('/store/')
        self.assertTemplateUsed(response,'store/store.html')
    def test_register_template(self):
        response=self.c.post('/accounts/register/')
        self.assertTemplateUsed(response,'accounts/register.html')
   
   


