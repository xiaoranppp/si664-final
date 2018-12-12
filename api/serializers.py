from marvel_world.models import Comic,Character,Power,CharacterPower,CharacterComic,Alignment,Gender,Race,Publisher,SkinColor,EyeColor,HairColor
from rest_framework import response, serializers, status





class AlignmentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Alignment
		fields = ('alignment_id', 'alignment_name')
class GenderSerializer(serializers.ModelSerializer):

	class Meta:
		model = Gender
		fields = ('gender_id', 'gender_name')
class RaceSerializer(serializers.ModelSerializer):

	class Meta:
		model = Race
		fields = ('race_id', 'race_name')
class PublisherSerializer(serializers.ModelSerializer):

	class Meta:
		model = Publisher
		fields = ('publisher_id', 'publisher_name')
class SkinColorSerializer(serializers.ModelSerializer):

	class Meta:
		model = SkinColor
		fields = ('skin_color_id', 'skin_color_name')
class HairColorSerializer(serializers.ModelSerializer):

	class Meta:
		model = HairColor
		fields = ('hair_color_id', 'hair_color_name')
class EyeColorSerializer(serializers.ModelSerializer):

	class Meta:
		model = EyeColor
		fields = ('eye_color_id', 'eye_color_name')
class ComicSerializer(serializers.ModelSerializer):

	class Meta:
		model = Comic
		fields = (
			'comic_id',
			'comic_name',
			'comic_number',
			'description',
            'issue_number'
			)
class PowerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Power
		fields = (
			'power_id',
			'power_name',
			)





class CharacterComicSerializer(serializers.ModelSerializer):
	character_id = serializers.ReadOnlyField(source='character.character_id')
	comic_id = serializers.ReadOnlyField(source='comic.comic_id')

	class Meta:
		model = CharacterComic
		fields = ('character_id', 'comic_id')
class CharacterPowerSerializer(serializers.ModelSerializer):
	character_id = serializers.ReadOnlyField(source='character.character_id')
	power_id = serializers.ReadOnlyField(source='power.power_id')

	class Meta:
		model = CharacterPower
		fields = ('character_id', 'power_id')


class CharacterSerializer(serializers.ModelSerializer):
	character_name = serializers.CharField(
		allow_blank=False,
		max_length=20
	)
	character_number = serializers.CharField(
		allow_blank=False,
        max_length=8
	)
	height = serializers.IntegerField(
		allow_null=False
	)
	weight = serializers.IntegerField(
		allow_null=False
	)
	intelligence = serializers.IntegerField(
		allow_null=True
	)
	speed = serializers.IntegerField(
		allow_null=True
	)
	strength = serializers.IntegerField(
		allow_null=True
	)
	combat = serializers.IntegerField(
		allow_null=True
	)
	power = serializers.IntegerField(
		allow_null=True
	)
	durability = serializers.IntegerField(
		allow_null=True
	)
	total = serializers.IntegerField(
		allow_null=True
	)
	alignment = AlignmentSerializer(
		many=False,
		read_only=True
		
	)
	gender = GenderSerializer(
		many=False,
		read_only=True
	)
	race = RaceSerializer(
		many=False,
		read_only=True
	)
	publisher = PublisherSerializer(
		many=False,
		read_only=True
	)
	skin_color = SkinColorSerializer(
		many=False,
		read_only=True
	)
	hair_color = HairColorSerializer(
		many=False,
		read_only=True
	)
	eye_color = EyeColorSerializer(
		many=False,
		read_only=True
	)
	alignment_id = serializers.PrimaryKeyRelatedField(
		allow_null=True,
		many=False,
		write_only=True,
		queryset=Alignment.objects.all(),
		source='alignment'
	)
	gender_id = serializers.PrimaryKeyRelatedField(
		allow_null=True,
		many=False,
		write_only=True,
		queryset=Gender.objects.all(),
		source='gender'
	)
	race_id = serializers.PrimaryKeyRelatedField(
		allow_null=True,
		many=False,
		write_only=True,
		queryset=Race.objects.all(),
		source='race'
	)
	publisher_id = serializers.PrimaryKeyRelatedField(
		allow_null=True,
		many=False,
		write_only=True,
		queryset=Publisher.objects.all(),
		source='publisher'
	)
	skin_color_id = serializers.PrimaryKeyRelatedField(
		allow_null=True,
		many=False,
		write_only=True,
		queryset=SkinColor.objects.all(),
		source='skin_color'
	)
	eye_color_id = serializers.PrimaryKeyRelatedField(
		allow_null=True,
		many=False,
		write_only=True,
		queryset=EyeColor.objects.all(),
		source='eye_color'
	)
	hair_color_id = serializers.PrimaryKeyRelatedField(
		allow_null=True,
		many=False,
		write_only=True,
		queryset=HairColor.objects.all(),
		source='hair_color'
	)
	character_power = CharacterPowerSerializer(
		source='character_power_set', # Note use of _set
		many=True,
		read_only=True
	)
	character_power_ids = serializers.PrimaryKeyRelatedField(
		many=True,
		write_only=True,
		queryset=Power.objects.all(),
		source='character_power'
	)
	character_comic = CharacterComicSerializer(
		source='character_comic_set', # Note use of _set
		many=True,
		read_only=True
	)
	character_comic_ids = serializers.PrimaryKeyRelatedField(
		many=True,
		write_only=True,
		queryset=Comic.objects.all(),
		source='character_comic'
	)

	class Meta:
		model = Character
		fields = (
			'character_id',
			'character_name',
			'character_number',
            'height',
            'weight',
            'intelligence',
            'speed',
            'power',
            'durability',
            'strength',
            'combat',
            'total',
			'alignment',
			'alignment_id',
            'gender',
            'gender_id',
            'race',
            'race_id',
            'publisher',
            'publisher_id',
            'skin_color',
            'skin_color_id',
            'eye_color',
            'eye_color_id',
            'hair_color',
            'hair_color_id',
			'character_power',
			'character_power_ids',
            'character_comic',
            'character_comic_ids'
		)

	def create(self, validated_data):
		"""
		This method persists a new HeritageSite instance as well as adds all related
		countries/areas to the heritage_site_jurisdiction table.  It does so by first
		removing (validated_data.pop('heritage_site_jurisdiction')) from the validated
		data before the new HeritageSite instance is saved to the database. It then loops
		over the heritage_site_jurisdiction array in order to extract each country_area_id
		element and add entries to junction/associative heritage_site_jurisdiction table.
		:param validated_data:
		:return: site
		"""

		# print(validated_data)

		powers = validated_data.pop('character_power')
		comics = validated_data.pop('character_comic')
		character = Character.objects.create(**validated_data)

		if powers is not None:
			for power in powers:
				CharacterPower.objects.create(
					character_id=character.character_id,
					power_id=power.power_id
				)

		if comics is not None:
			for comic in comics:
				CharacterComic.objects.create(
					character_id=character.character_id,
					comic_id=comic.comic_id
				)
		return character

	def update(self, instance, validated_data):
		# site_id = validated_data.pop('heritage_site_id')
		character_id = instance.character_id
		new_powers = validated_data.pop('character_power')
		new_comics = validated_data.pop('character_comic')
		instance.character_name = validated_data.get(
			'character_name',
			instance.character_name
		)
		instance.character_number = validated_data.get(
			'character_number',
			instance.character_number
		)
		instance.weight = validated_data.get(
			'weight',
			instance.weight
		)
		instance.height = validated_data.get(
			'height',
			instance.height
		)
		instance.intelligence = validated_data.get(
			'intelligence',
			instance.intelligence
		)
		instance.power= validated_data.get(
			'power',
			instance.power
		)
		instance.combat = validated_data.get(
			'combat',
			instance.combat
		)
		instance.speed = validated_data.get(
			'speed',
			instance.speed
		)
		instance.strength= validated_data.get(
			'strength',
			instance.strength
		)
		instance.durability = validated_data.get(
			'durability',
			instance.durability
		)
		instance.total = validated_data.get(
			'total',
			instance.total
		)
		instance.alignment_id = validated_data.get(
			'alignment_id',
			instance.alignment_id
		)
		instance.gender_id = validated_data.get(
			'gender_id',
			instance.gender_id
		)
		instance.race_id = validated_data.get(
			'race_id',
			instance.race_id
		)
		instance.publisher_id = validated_data.get(
			'publisher_id',
			instance.publisher_id
		)
		instance.skin_color_id = validated_data.get(
			'skin_color_id',
			instance.skin_color_id
		)
		instance.eye_color_id = validated_data.get(
			'eye_color_id',
			instance.eye_color_id
		)
		instance.hair_color_id = validated_data.get(
			'hair_color_id',
			instance.hair_color_id
		)
		
		instance.save()
		new_ids1 = []
		old_ids1 = CharacterComic.objects \
			.values_list('comic_id', flat=True) \
			.filter(character_id__exact=character_id)

		# TODO Insert may not be required (Just return instance)

		# Insert new unmatched country entries
		for comic in new_comics:
			new_id1 = comic.comic_id
			new_ids1.append(new_id1)
			if len(new_comics)==0:
				break
			if new_id1 in old_ids1:
				continue
			else:
				CharacterComic.objects \
					.create(character_id=character_id, comic_id=new_id1)

		# Delete old unmatched country entries
		for old_id1 in old_ids1:
			if old_id1 in new_ids1:
				continue
			else:
				CharacterComic.objects \
					.filter(character_id=character_id, comic_id=old_id1) \
					.delete()

		# If any existing country/areas are not in updated list, delete them
		new_ids = []
		old_ids = CharacterPower.objects \
			.values_list('power_id', flat=True) \
			.filter(character_id__exact=character_id)

		# TODO Insert may not be required (Just return instance)

		# Insert new unmatched country entries
		for power in new_powers:
			if len(new_powers)==0:
				break
			new_id = power.power_id
			new_ids.append(new_id)
			if new_id in old_ids:
				continue
			else:
				CharacterPower.objects \
					.create(character_id=character_id, power_id=new_id)

		# Delete old unmatched country entries
		for old_id in old_ids:
			if old_id in new_ids:
				continue
			else:
				CharacterPower.objects \
					.filter(character_id=character_id, power_id=old_id) \
					.delete()
		

		return instance