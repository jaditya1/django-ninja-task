from django.db import models
from django.contrib.auth.models import User



class Tag(models.Model):
	tag_type = models.CharField(max_length=100,verbose_name='Tag Type')
	tag_value = models.CharField(max_length=100,verbose_name='Tag Value')
	deleted = models.BooleanField(default=False,verbose_name="Is Deleted")
	created_by = models.ForeignKey(User , on_delete=models.CASCADE)

	updated_by = models.ForeignKey(User , on_delete=models.CASCADE,
											related_name ='user_updated_by',
											null=True,blank=True)
	short_name = models.CharField(max_length=100,verbose_name='Short Name',null=True,blank=True)
	

	class Meta:
		unique_together = ('tag_type','tag_value')

		verbose_name='Tag'
		verbose_name_plural=' Tags'



	def __str__(self):
	   return str(self.tag_type)



class Seed(models.Model):
	row = models.IntegerField(verbose_name='Row')
	column = models.IntegerField(verbose_name='Column')
	status = models.CharField(max_length=50, choices=[
						('OK','OK'), 
						('INVALID','Invalid'),
						],verbose_name='Status')
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE,
						verbose_name='Tag', limit_choices_to={'deleted':False})
	

	class Meta:
		unique_together = ('row','column')
		verbose_name='Seed'
		verbose_name_plural='Seeds'

	def __str__(self):
	   return str(self.row)