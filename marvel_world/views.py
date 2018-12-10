from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Characters


def index(request):
	return HttpResponse("Hello, world. You're at the marvel world super hero")


class AboutPageView(generic.TemplateView):
	template_name = 'marvel_world/about.html'


class HomePageView(generic.TemplateView):
	template_name = 'marvel_world/home.html'


class CharacterListView(generic.ListView):
	model = Characters
	context_object_name = 'characters'
	template_name = 'marvel_world/characters.html'
	paginate_by = 50

	def get_queryset(self):
		return Characters.objects.all().select_related('alignment','eye_color','skin_color','hair_color','race','gender','publisher').order_by('character_name')
class CharacterDetailView(generic.DetailView):
    model = Characters
    context_object_name=  'character'
    template_name = 'marvel_world/character_information.html'

#class CharacterDetailView(generic.DetailView):model = Characters context_object_name=  'character'template_name='marvel_world/character_information.html'

