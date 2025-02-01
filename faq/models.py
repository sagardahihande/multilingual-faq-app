from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True)  # Hindi
    question_bn = models.TextField(blank=True)  # Bengali

    def get_translated_question(self, lang_code):
        return getattr(self, f'question_{lang_code}', self.question)

    def save(self, *args, **kwargs):
        if not self.pk:  # Only translate on creation
            translator = Translator()
            try:
                self.question_hi = translator.translate(self.question, dest='hi').text
            except:
                pass
            try:
                self.question_bn = translator.translate(self.question, dest='bn').text
            except:
                pass
        super().save(*args, **kwargs)