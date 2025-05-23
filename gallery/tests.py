from django.test import TestCase
from django.urls import reverse
from .models import Category, Image

class GalleryViewTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Nature')
        self.image = Image.objects.create(
            category=self.category,
            title='Sunset',
            image='test.jpg',  # adjust field names as needed
        )

    def test_gallery_view_status_code(self):
        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)

    def test_gallery_view_context(self):
        response = self.client.get(reverse('gallery'))
        self.assertIn('categories', response.context)
        self.assertIn(self.category, response.context['categories'])

    def test_image_detail_view_status_code(self):
        response = self.client.get(reverse('image_detail', args=[self.image.pk]))
        self.assertEqual(response.status_code, 200)

    def test_image_detail_view_context(self):
        response = self.client.get(reverse('image_detail', args=[self.image.pk]))
        self.assertIn('image', response.context)
        self.assertEqual(response.context['image'], self.image)

    def test_image_detail_view_404(self):
        response = self.client.get(reverse('image_detail', args=[999]))
        self.assertEqual(response.status_code, 404)
