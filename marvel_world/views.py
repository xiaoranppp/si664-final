from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Character,Comic,Power,CharacterPower,CharacterComic
from django_filters.views import FilterView
from .filters import Marvel_worldFilter,Marvel_comicFilter
from .forms import CharacterForm,PowerForm,ComicForm
from django.urls import reverse,reverse_lazy
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
	paginate_by = 600

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
@method_decorator(login_required, name='dispatch')
class CharacterCreateView(generic.View):
	model = Character
	form_class = CharacterForm
	success_message = "Character created successfully"
	template_name = 'marvel_world/character_new.html'
	# fields = '__all__' <-- superseded by form_class
	# success_url = reverse_lazy('heritagesites/site_list')

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def post(self, request):
		form = CharacterForm(request.POST)
		if form.is_valid():
			character = form.save(commit=False)
			character.save()
			for power in form.cleaned_data['super_power']:
				CharacterPower.objects.create(character=character, power=power)
			for comic in form.cleaned_data['comics']:
				CharacterComic.objects.create(character=character, comic=comic)
			return redirect(character) # shortcut to object's get_absolute_url()
			# return HttpResponseRedirect(site.get_absolute_url())
		return render(request, 'marvel_world/character_new.html', {'form': form})

	def get(self, request):
		form = CharacterForm()
		return render(request, 'marvel_world/character_new.html', {'form': form})
@method_decorator(login_required, name='dispatch')
class PowerCreateView(generic.View):
	model = Power
	form_class = PowerForm
	success_message = "Super power created successfully"
	template_name = 'marvel_world/power_new.html'
	# fields = '__all__' <-- superseded by form_class
	# success_url = reverse_lazy('heritagesites/site_list')

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def post(self, request):
		form = PowerForm(request.POST)
		if form.is_valid():
			power = form.save(commit=False)
			power.save()
			for character in form.cleaned_data['character']:
				CharacterPower.objects.create(character=character, power=power)
			return redirect(power) # shortcut to object's get_absolute_url()
			# return HttpResponseRedirect(site.get_absolute_url())
		return render(request, 'marvel_world/power_new.html', {'form': form})

	def get(self, request):
		form = PowerForm()
		return render(request, 'marvel_world/power_new.html', {'form': form})
@method_decorator(login_required, name='dispatch')
class ComicCreateView(generic.View):
	model = Comic
	form_class = ComicForm
	success_message = "Comic created successfully"
	template_name = 'marvel_world/comic_new.html'
	# fields = '__all__' <-- superseded by form_class
	# success_url = reverse_lazy('heritagesites/site_list')

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def post(self, request):
		form = ComicForm(request.POST)
		if form.is_valid():
			comic = form.save(commit=False)
			comic.save()
			for character in form.cleaned_data['character']:
				CharacterComic.objects.create(character=character, comic=comic)
			return redirect(comic) # shortcut to object's get_absolute_url()
			# return HttpResponseRedirect(site.get_absolute_url())
		return render(request, 'marvel_world/comic_new.html', {'form': form})

	def get(self, request):
		form = ComicForm()
		return render(request, 'marvel_world/comic_new.html', {'form': form})
#class CharacterDetailView(generic.DetailView):model = Characters context_object_name=  'character'template_name='marvel_world/character_information.html'

@method_decorator(login_required, name='dispatch')
class CharacterUpdateView(generic.UpdateView):
	model = Character
	form_class = CharacterForm
	# fields = '__all__' <-- superseded by form_class
	context_object_name = 'character'
	# pk_url_kwarg = 'site_pk'
	success_message = "Character updated successfully"
	template_name = 'marvel_world/character_update.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def form_valid(self, form):
		character = form.save(commit=False)
		# site.updated_by = self.request.user
		# site.date_updated = timezone.now()
		character.save()

		# Current country_area_id values linked to site
		old_ids = CharacterPower.objects\
			.values_list('power_id', flat=True)\
			.filter(character_id=character.character_id)

		# New countries list
		new_powers = form.cleaned_data['super_power']

		# TODO can these loops be refactored?

		# New ids
		new_ids = []

		# Insert new unmatched country entries
		for power in new_powers:
			new_id = power.power_id
			new_ids.append(new_id)
			if new_id in old_ids:
				continue
			else:
				CharacterPower.objects \
					.create(character=character, power=power)

		# Delete old unmatched country entries
		for old_id in old_ids:
			if old_id in new_ids:
				continue
			else:
				CharacterPower.objects \
					.filter(character_id=character.character_id, power_id=old_id) \
					.delete()


		old_ids1 = CharacterComic.objects\
			.values_list('comic_id', flat=True)\
			.filter(character_id=character.character_id)

		# New countries list
		new_comics = form.cleaned_data['comics']

		# TODO can these loops be refactored?

		# New ids
		new_ids1 = []

		# Insert new unmatched country entries
		for comic in new_comics:
			new_id1 = comic.comic_id
			new_ids1.append(new_id1)
			if new_id1 in old_ids1:
				continue
			else:
				CharacterComic.objects \
					.create(character=character, comic=comic)

		# Delete old unmatched country entries
		for old_id1 in old_ids1:
			if old_id1 in new_ids1:
				continue
			else:
				CharacterComic.objects \
					.filter(character_id=character.character_id, comic_id=old_id1) \
					.delete()

		return HttpResponseRedirect(character.get_absolute_url())
@method_decorator(login_required, name='dispatch')
class PowerUpdateView(generic.UpdateView):
	model = Power
	form_class = PowerForm
	# fields = '__all__' <-- superseded by form_class
	context_object_name = 'power'
	# pk_url_kwarg = 'site_pk'
	success_message = "Super power updated successfully"
	template_name = 'marvel_world/power_update.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def form_valid(self, form):
		power = form.save(commit=False)
		# site.updated_by = self.request.user
		# site.date_updated = timezone.now()
		power.save()

		# Current country_area_id values linked to site
		old_ids = CharacterPower.objects\
			.values_list('character_id', flat=True)\
			.filter(power_id=power.power_id)

		# New countries list
		new_chs = form.cleaned_data['character']

		# TODO can these loops be refactored?

		# New ids
		new_ids = []

		# Insert new unmatched country entries
		for character in new_chs:
			new_id = character.character_id
			new_ids.append(new_id)
			if new_id in old_ids:
				continue
			else:
				CharacterPower.objects \
					.create(character=character, power=power)

		# Delete old unmatched country entries
		for old_id in old_ids:
			if old_id in new_ids:
				continue
			else:
				CharacterPower.objects \
					.filter(character_id=old_id, power_id=power.power_id) \
					.delete()


		

		return HttpResponseRedirect(power.get_absolute_url())
		# return redirect('heritagesites/site_detail', pk=site.pk)
@method_decorator(login_required, name='dispatch')
class ComicUpdateView(generic.UpdateView):
	model = Comic
	form_class = ComicForm
	# fields = '__all__' <-- superseded by form_class
	context_object_name = 'comic'
	# pk_url_kwarg = 'site_pk'
	success_message = "Comic updated successfully"
	template_name = 'marvel_world/comic_update.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def form_valid(self, form):
		comic = form.save(commit=False)
		# site.updated_by = self.request.user
		# site.date_updated = timezone.now()
		comic.save()

		# Current country_area_id values linked to site
		old_ids = CharacterComic.objects\
			.values_list('character_id', flat=True)\
			.filter(comic_id=comic.comic_id)

		# New countries list
		new_chs = form.cleaned_data['character']

		# TODO can these loops be refactored?

		# New ids
		new_ids = []

		# Insert new unmatched country entries
		for character in new_chs:
			new_id = character.character_id
			new_ids.append(new_id)
			if new_id in old_ids:
				continue
			else:
				CharacterComic.objects \
					.create(character=character, comic=comic)

		# Delete old unmatched country entries
		for old_id in old_ids:
			if old_id in new_ids:
				continue
			else:
				CharacterComic.objects \
					.filter(character_id=old_id, comic_id=comic.comic_id) \
					.delete()


		

		return HttpResponseRedirect(comic.get_absolute_url())
@method_decorator(login_required, name='dispatch')
class CharacterDeleteView(generic.DeleteView):
	model =Character
	success_message = "Character deleted successfully"
	success_url = reverse_lazy('characters')
	context_object_name = 'character'
	template_name = 'marvel_world/character_delete.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()

		# Delete HeritageSiteJurisdiction entries
		CharacterPower.objects \
			.filter(character_id=self.object.character_id) \
			.delete()
		CharacterComic.objects \
			.filter(character_id=self.object.character_id) \
			.delete()

		self.object.delete()

		return HttpResponseRedirect(self.get_success_url())
@method_decorator(login_required, name='dispatch')
class PowerDeleteView(generic.DeleteView):
	model =Power
	success_message = "Super power deleted successfully"
	success_url = reverse_lazy('super_power')
	context_object_name = 'power'
	template_name = 'marvel_world/power_delete.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()

		# Delete HeritageSiteJurisdiction entries
		CharacterPower.objects \
			.filter(power_id=self.object.power_id) \
			.delete()

		self.object.delete()

		return HttpResponseRedirect(self.get_success_url())
@method_decorator(login_required, name='dispatch')
class ComicDeleteView(generic.DeleteView):
	model =Comic
	success_message = "Comic deleted successfully"
	success_url = reverse_lazy('comics')
	context_object_name = 'comic'
	template_name = 'marvel_world/comic_delete.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()

		# Delete HeritageSiteJurisdiction entries
		CharacterComic.objects \
			.filter(comic_id=self.object.comic_id) \
			.delete()

		self.object.delete()

		return HttpResponseRedirect(self.get_success_url())