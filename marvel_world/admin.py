from django.contrib import admin

import marvel_world.models as models


@admin.register(models.Comic)
class ComicsAdmin(admin.ModelAdmin):
	fields = [
		'comic_name',
		'comic_number',
        'issue_number',
        'description'
	]

	list_display = [
		'comic_name',
		'comic_number',
        'issue_number',
        'description',
	]


# admin.site.register(models.CountryArea)


@admin.register(models.Power)
class PowersAdmin(admin.ModelAdmin):
	fields = ['power_name']
	list_display = ['power_name']
	ordering = ['power_name']

# admin.site.register(models.DevStatus)


@admin.register(models.Character)
class CharactersAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': (
				'character_name',
				'character_number',
				'alignment',
				'gender',
				'eye_color',
                'race',
                'hair_color',
                'publisher',
                'skin_color'
			)
		}),
		('Statistic', {
			'fields': [
				'height',
                'weight',
                'intelligence',
                'strengh',
                'speed',
                'durability',
                'power',
                'combat',
                'total'
			]
		})
	)

	list_display = (
		'character_name',
		'character_number',
		'alignment',
		'gender',
		'eye_color',
        'race',
        'hair_color',
        'publisher',
        'skin_color',
        'height',
        'weight',
        'intelligence',
        'strength',
        'speed',
        'durability',
        'power',
        'combat',
        'total',
        #'country_area_display',
		'comics_display',
        'super_power_display'
	)

	list_filter = (
		'alignment',
		'gender',
		'eye_color',
        'race',
        'hair_color',
        'publisher',
        'skin_color'
	)

# admin.site.register(models.HeritageSite)


@admin.register(models.Alignment)
class AlignmentsAdmin(admin.ModelAdmin):
	fields = ['alignment_name']
	list_display = ['alignment_name']
	ordering = ['alignment_name']

# admin.site.register(models.HeritageSiteCategory)


@admin.register(models.EyeColor)
class EyeColorsAdmin(admin.ModelAdmin):
	fields = ['eye_color_name']
	list_display = ['eye_color_name']
	ordering = ['eye_color_name']

@admin.register(models.SkinColor)
class SkinColorsAdmin(admin.ModelAdmin):
	fields = ['skin_color_name']
	list_display = ['skin_color_name']
	ordering = ['skin_color_name']
@admin.register(models.HairColor)
class HairColorsAdmin(admin.ModelAdmin):
	fields = ['hair_color_name']
	list_display = ['hair_color_name']
	ordering = ['hair_color_name']
@admin.register(models.Publisher)
class PublishersAdmin(admin.ModelAdmin):
	fields = ['publisher_name']
	list_display = ['publisher_name']
	ordering = ['publisher_name']
@admin.register(models.Race)
class RacesAdmin(admin.ModelAdmin):
	fields = ['race_name']
	list_display = ['race_name']
	ordering = ['race_name']
# admin.site.register(models.IntermediateRegion)
@admin.register(models.Gender)
class GendersAdmin(admin.ModelAdmin):
	fields = ['gender_name']
	list_display = ['gender_name']
	ordering = ['gender_name']


