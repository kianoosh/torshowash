from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """test models."""
    
    def test_create_user_with_email_successful(self):
        """test if creating a user with email is successful"""
        name = None
        email = "test@example.com"
        password = "testpassword1234"
        user = get_user_model().objects.create_user(
            username=email,
            name=name,
            email=email,
            password=password,
        )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
