from unittest.mock import sentinel

from django.test import SimpleTestCase
from django.urls import resolve

from apps.accounts.serializers import UserSerializer
from apps.accounts.models import User
from apps.accounts.views import UserView


class UserSignupTests(SimpleTestCase):
    def test_user_model_requires_phone_and_address_for_superuser(self):
        self.assertEqual(User.REQUIRED_FIELDS, ["phone_number", "address"])
        self.assertTrue(User._meta.get_field("phone_number").unique)

    def test_signup_route_is_registered(self):
        match = resolve("/users/signup/")
        self.assertEqual(match.func.view_class, UserView)

    def test_serializer_uses_user_manager_for_creation(self):
        serializer = UserSerializer()
        validated_data = {
            "email": "user@example.com",
            "password": "StrongPass123",
            "phone_number": "998901234567",
            "address": "Tashkent",
            "first_name": "Test",
            "last_name": "User",
        }

        original_create_user = UserSerializer.Meta.model.objects.create_user
        calls = []

        def fake_create_user(*, password, **validated_data):
            calls.append((password, validated_data))
            return sentinel.user

        UserSerializer.Meta.model.objects.create_user = fake_create_user
        try:
            created_user = serializer.create(validated_data.copy())
        finally:
            UserSerializer.Meta.model.objects.create_user = original_create_user

        self.assertIs(created_user, sentinel.user)
        self.assertEqual(calls, [("StrongPass123", {
            "email": "user@example.com",
            "phone_number": "998901234567",
            "address": "Tashkent",
            "first_name": "Test",
            "last_name": "User",
        })])
