from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

# Create your views here.

class Index(TemplateView):
	model = Cliente
	template_name = 'Reservas/index.html'

	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		context['clientes'] = Cliente.objects.all()
		return context


		