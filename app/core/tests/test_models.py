from django.test import TestCase
from django.contrib.auth import get_user_model

from ..models import Tag

def sample_user(email='Test123@gmail.com', password="PasswordPass"):
    return get_user_model().objects.create_user(email, password)

class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """
        Test creating a new user with an email is successful
        """
        email = 'test@gmail.com'
        password = 'HappyPass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized"""
        email = 'test@gmail.com'
        password = 'HappyPass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_emaiil(self):
        """Test creating user with no email will raise error"""
        password = 'HappyPass123'
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None,
                password
            )

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        email = 'test@gmail.com'
        password = 'HappyPass123'
        user = get_user_model().objects.create_superuser(
            email,
            password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """ Test the tag string representation """
        tag = Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)