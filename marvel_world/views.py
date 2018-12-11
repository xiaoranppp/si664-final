from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Character,Comic,Power
from django_filters.views import FilterView
from .filters import Marvel_worldFilter,Marvel_comicFilter

def index(request):
	return HttpResponse("Hello, world. You're at the marvel world super hero")


class AboutPageView(generic.TemplateView):
	template_name = 'marvel_world/about.html'


class HomePageView(generic.TemplateView):
	template_name = 'marvel_world/home.html'

@method_decorator(login_required, name='dispatch')
class CharacterListView(generic.ListView):
	model = Character
	context_object_name = 'characters'
	template_name = 'marvel_world/characters.html'
	paginate_by = 50

	def get_queryset(self):
		return Character.objects.all().select_related('alignment','eye_color','skin_color','hair_color','race','gender','publisher').order_by('character_name')
@method_decorator(login_required, name='dispatch')
class CharacterDetailView(generic.DetailView):
    model = Character
    context_object_name=  'character'
    template_name = 'marvel_world/character_information.html'
@method_decorator(login_required, name='dispatch')
class ComicListView(generic.ListView):
	model = Comic
	context_object_name = 'comics'
	template_name = 'marvel_world/comics.html'
	paginate_by = 50

	def get_queryset(self):
		return Comic.objects.all().order_by('comic_name')
@method_decorator(login_required, name='dispatch')
class ComicDetailView(generic.DetailView):
    model = Comic
    context_object_name=  'comic'
    template_name = 'marvel_world/comic_information.html'
@method_decorator(login_required, name='dispatch')
class PowerListView(generic.ListView):
	model = Power
	context_object_name = 'powers'
	template_name = 'marvel_world/super_power.html'
	paginate_by = 50

	def get_queryset(self):
		return Power.objects.all().order_by('power_name')
@method_decorator(login_required, name='dispatch')
class PowerDetailView(generic.DetailView):
    model = Power
    context_object_name=  'power'
    template_name = 'marvel_world/super_power_information.html'
@method_decorator(login_required, name='dispatch')
class CharacterFilterView(FilterView):
	filterset_class = Marvel_worldFilter
	template_name = 'marvel_world/character_filter.html'
@method_decorator(login_required, name='dispatch')
class ComicFilterView(FilterView):
	filterset_class = Marvel_comicFilter
	template_name = 'marvel_world/comic_filter.html'
#class CharacterDetailView(generic.DetailView):model = Characters context_object_name=  'character'template_name='marvel_world/character_information.html'

