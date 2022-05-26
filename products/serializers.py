from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
	"""docstring for ProductSerializer"""
	class Meta:
		model = Product
		fields = '__all__'

		