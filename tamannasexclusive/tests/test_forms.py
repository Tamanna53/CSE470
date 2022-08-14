from django.test import SimpleTestCase
from accounts import forms
class TestForms(SimpleTestCase):
    def test_valid_form(self):
        form=forms.RegistrationForm(data={
            'first_name':'test',
            'last_name':'test2',
            'phone_number':123456789,
            'password':'test',
            'confirm_password':'test'

           
        }
        )
        self.assertFalse(form.is_valid())
    def test_invalid_form(self):
        form=forms.RegistrationForm(data={})
        self.assertFalse(form.is_valid())
    def test_empty_form(self):
        form=forms.RegistrationForm(data={})
        self.assertFalse(form.is_valid())

    
