from django.test import TestCase
from django.urls import reverse
from .models import Category, Image
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime


class GalleryTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Nature')
        self.image_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x47\x49\x46\x38\x39\x61',
            content_type='image/jpeg'
        )
        self.image = Image.objects.create(
            title='Sunset',
            image=self.image_file,
            created_date=datetime.date.today(),
            age_limit=10
        )
        self.image.categories.add(self.category)

    def test_gallery_view_status_code(self):
        response = self.client.get(reverse('gallery:gallery'))
        self.assertEqual(response.status_code, 200)

    def test_gallery_view_context(self):
        response = self.client.get(reverse('gallery:gallery'))
        self.assertIn('categories', response.context)
        self.assertIn(self.category, response.context['categories'])

    def test_image_detail_view_status_code(self):
        response = self.client.get(reverse('gallery:image_detail', args=[self.image.pk]))
        self.assertEqual(response.status_code, 200)

    def test_image_detail_context(self):
        response = self.client.get(reverse('gallery:image_detail', args=[self.image.pk]))
        self.assertEqual(response.context['image'], self.image)

    def test_image_detail_not_found(self):
        response = self.client.get(reverse('gallery:image_detail', args=[999]))
        self.assertEqual(response.status_code, 404)
