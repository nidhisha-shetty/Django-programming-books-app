from django.db import models

# Create your models here.

class Book(models.Model):
	book_title = models.CharField(max_length=100)
	book_author = models.CharField(max_length=50)
	book_description=models.TextField()
	book_image = models.ImageField(default="images/coming_soon.jpg", upload_to='images/')

	def go_to_link_edit(self):
		return f"/edit/{self.id}/"

	def go_to_link_view(self):
		return f"/view/{self.id}"

	def go_to_link_delete(self):
		return f"/delete/{self.id}"