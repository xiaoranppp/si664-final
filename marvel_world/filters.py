import django_filters
from marvel_world.models import Comic,Character,Power,Alignment,SkinColor,HairColor,EyeColor,Race,Publisher,Gender


class Marvel_comicFilter(django_filters.FilterSet):
    comic_name = django_filters.CharFilter(
		field_name='comic_name',
		label='Comic Name',
		lookup_expr='icontains'
	)
    year = django_filters.CharFilter(
		field_name='comic_name',
		label='Year(please enter 4 number as year)',
		lookup_expr='icontains'
	)
    description = django_filters.CharFilter(
		field_name='description',
		label='Description',
		lookup_expr='icontains'
	)
    

    
    

	# Add description, heritage_site_category, region, sub_region and intermediate_region filters here

    Character= django_filters.ModelChoiceFilter(
		field_name='characters',
		label='Character in this Comic',
        queryset=Character.objects.all(),
		lookup_expr='exact'
	)
    class Meta:
	    model =Comic
	    fields = []
class Marvel_worldFilter(django_filters.FilterSet):
    character_name = django_filters.CharFilter(
		field_name='character_name',
		label='Character Name',
		lookup_expr='icontains'
	)
    

    
    

	# Add description, heritage_site_category, region, sub_region and intermediate_region filters here

    Power= django_filters.ModelChoiceFilter(
		field_name='super_power',
		label='super power',
		queryset=Power.objects.all(),
		lookup_expr='exact'
	)
    gender= django_filters.ModelChoiceFilter(
        field_name='gender',
        label='Gender',
        queryset=Gender.objects.all(), 
        lookup_expr='exact')
    alignment= django_filters.ModelChoiceFilter(
        field_name='alignment',
        label='Alignment',
        queryset=Alignment.objects.all(), 
        lookup_expr='exact')
    skin_color= django_filters.ModelChoiceFilter(
        field_name='skin_color',
        label='Skin Color',
        queryset=SkinColor.objects.all(), 
        lookup_expr='exact')
    eye_color= django_filters.ModelChoiceFilter(
        field_name='eye_color',
        label='Eye Color',
        queryset=EyeColor.objects.all(), 
        lookup_expr='exact')
    hair_color= django_filters.ModelChoiceFilter(
        field_name='hair_color',
        label='Hair Color',
        queryset=HairColor.objects.all(), 
        lookup_expr='exact')
    race= django_filters.ModelChoiceFilter(
        field_name='race',
        label='Race',
        queryset=Race.objects.all(), 
        lookup_expr='exact')
    Publisher= django_filters.ModelChoiceFilter(
        field_name='publisher',
        label='Publisher',
        queryset=Publisher.objects.all(), 
        lookup_expr='exact')
    weight = django_filters.NumberFilter(
		field_name='weight',
		label='Weight(kg)',
		lookup_expr='exact'
	)
    height = django_filters.NumberFilter(
		field_name='height',
		label='Height(cm)',
		lookup_expr='exact'
	)
    
    
	# Add date_inscribed filter here


    class Meta:
	    model =Character
	    # form = SearchForm
	    # fields [] is required, even if empty.
	    fields = []