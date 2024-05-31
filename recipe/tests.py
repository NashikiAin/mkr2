from django.test import TestCase
from .models import Category, Recipe
from datetime import datetime

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Test Category')

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_category_str_method(self):
        category = Category.objects.get(id=1)
        self.assertEqual(str(category), category.name)

class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Test Category')
        category = Category.objects.get(id=1)
        Recipe.objects.create(
            title='Test Recipe',
            description='Test Description',
            instructions='Test Instructions',
            ingredients='Test Ingredients',
            category=category
        )

    def test_title_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_created_at_auto_now_add(self):
        recipe = Recipe.objects.get(id=1)
        self.assertTrue(isinstance(recipe.created_at, datetime))

    def test_updated_at_auto_now(self):
        recipe = Recipe.objects.get(id=1)
        self.assertTrue(isinstance(recipe.updated_at, datetime))

    def test_recipe_str_method(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(str(recipe), recipe.title)
