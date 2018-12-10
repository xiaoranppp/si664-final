from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Characters,Comics,Powers


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
class ComicListView(generic.ListView):
	model = Comics
	context_object_name = 'comics'
	template_name = 'marvel_world/comics.html'
	paginate_by = 50

	def get_queryset(self):
		return Comics.objects.all().order_by('comic_name')
class ComicDetailView(generic.DetailView):
    model = Comics
    context_object_name=  'comic'
    template_name = 'marvel_world/comic_information.html'
class PowerListView(generic.ListView):
	model = Powers
	context_object_name = 'powers'
	template_name = 'marvel_world/super_power.html'
	paginate_by = 50

	def get_queryset(self):
		return Powers.objects.all().order_by('power_name')
class PowerDetailView(generic.DetailView):
    model = Powers
    context_object_name=  'power'
    template_name = 'marvel_world/super_power_information.html'

#class CharacterDetailView(generic.DetailView):model = Characters context_object_name=  'character'template_name='marvel_world/character_information.html'

