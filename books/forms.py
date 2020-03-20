from django import forms
from .models import Book
class BookForm(forms.ModelForm):
	class Meta:
		model = Book

		fields=[
		'book_title',
		'book_author',
		'book_description',
		'book_image'
		]
