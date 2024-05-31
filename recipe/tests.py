from django.test import TestCase
from .models import Category, Recipe

class CategoryModelTest(TestCase):
    def setUpTestData(cls):
        Category.objects.create(name='Test Category')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_category_name(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.name, 'Test Category')

class RecipeModelTest(TestCase):
    def setUpTestData(cls):
        category = Category.objects.create(name='Test Category')
        Recipe.objects.create(title='Test Recipe', description='Test Description', instructions='Test Instructions', ingredients='Test Ingredients', category=category)

    def test_title_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_recipe_title(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.title, 'Test Recipe')

    def test_recipe_description(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.description, 'Test Description')

    def test_recipe_instructions(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.instructions, 'Test Instructions')

    def test_recipe_ingredients(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.ingredients, 'Test Ingredients')

    def test_recipe_category(self):
        recipe = Recipe.objects.get(id=1)
        category = Category.objects.get(id=1)
        self.assertEqual(recipe.category, category)
