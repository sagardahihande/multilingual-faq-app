from django.test import TestCase
from django.urls import reverse
from .models import FAQ

class FAQTests(TestCase):
    def test_translation_fallback(self):
        faq = FAQ.objects.create(
            question="Hello",
            answer="World"
        )
        self.assertEqual(faq.get_translated_question('fr'), "Hello")

    def test_api_response(self):
        FAQ.objects.create(question="Test", answer="Answer")
        response = self.client.get(reverse('faq-list') + '?lang=hi')
        self.assertEqual(response.status_code, 200)