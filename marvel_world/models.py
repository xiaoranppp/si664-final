
from django.db import models





class CharacterComic(models.Model):
    character_comic_id = models.AutoField(primary_key=True)
    character = models.ForeignKey('Character', models.DO_NOTHING)
    comic = models.ForeignKey('Comic', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'character_comic'
        ordering = ['character', 'comic']
        verbose_name = 'character comic relationship'
        verbose_name_plural = 'character comic relationship'



class CharacterPower(models.Model):
    character_power_id = models.AutoField(primary_key=True)
    character = models.ForeignKey('Character', models.DO_NOTHING)
    power = models.ForeignKey('Power', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'character_power'
        ordering = ['character', 'power']
        verbose_name = 'character power relationship'
        verbose_name_plural = 'character power relationship'

class Comic(models.Model):
    comic_id = models.AutoField(primary_key=True)
    comic_number = models.CharField(unique=True, max_length=25)
    comic_name = models.CharField(unique=True, max_length=25)
    issue_number = models.CharField(max_length=5, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    #character=models.ManyToManyField(Characters,through='CharacterComic')

    class Meta:
        managed = False
        db_table = 'comic'
        ordering = ['comic_name']
        verbose_name = 'comic information'
        verbose_name_plural = 'comic information'

    def __str__(self):
        return self.comic_name
   

    #characters_display.short_description = 'characters'
class Power(models.Model):
    power_id = models.AutoField(primary_key=True)
    power_name = models.CharField(unique=True, max_length=25)
    #characters=models.ManyToManyField(Characters,through='CharacterPower')


    class Meta:
        managed = False
        db_table = 'power'
        ordering = ['power_name']
        verbose_name = 'super power information'
        verbose_name_plural = 'super power information'

    def __str__(self):
        return self.power_name
    
    #characters_display.short_description = 'characters'
class Character(models.Model):
    character_id = models.AutoField(primary_key=True)
    character_name = models.CharField(unique=True, max_length=20)
    alignment = models.ForeignKey('Alignment', models.DO_NOTHING, blank=True, null=True)
    gender = models.ForeignKey('Gender', models.DO_NOTHING, blank=True, null=True)
    eye_color = models.ForeignKey('EyeColor', models.DO_NOTHING, blank=True, null=True)
    race = models.ForeignKey('Race', models.DO_NOTHING, blank=True, null=True)
    hair_color = models.ForeignKey('HairColor', models.DO_NOTHING, blank=True, null=True)
    publisher = models.ForeignKey('Publisher', models.DO_NOTHING, blank=True, null=True)
    skin_color = models.ForeignKey('SkinColor', models.DO_NOTHING, blank=True, null=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    character_number = models.CharField(max_length=8)
    intelligence = models.IntegerField(blank=True, null=True)
    strength = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    durability = models.IntegerField(blank=True, null=True)
    power = models.IntegerField(blank=True, null=True)
    combat = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    super_power = models.ManyToManyField(Power, through='CharacterPower',related_name='characters')
    comics=models.ManyToManyField(Comic,through='CharacterComic',related_name='characters')

    class Meta:
        managed = False
        db_table = 'character_info'
        ordering = ['character_name']
        verbose_name = 'character information'
        verbose_name_plural = 'character information'

    def __str__(self):
        return self.character_name
    
    def comics_display(self):
        return ', '.join(
            comics.comic_name for comics in self.comics.all())

    comics_display.short_description = 'comics'
    def super_power_display(self):
        return ', '.join(
           super_power.power_name for super_power in self.super_power.all())

    super_power_display.short_description = 'super power set'





        

class Alignment(models.Model):
    alignment_id = models.AutoField(primary_key=True)
    alignment_name = models.CharField(unique=True, max_length=8)

    class Meta:
        managed = False
        db_table = 'alignment'
        ordering = ['alignment_name']
        verbose_name = 'marvel heros alignment'
        verbose_name_plural = 'marvel heros alignment'

    def __str__(self):
        return self.alignment_name

class EyeColor(models.Model):
    eye_color_id = models.AutoField(primary_key=True)
    eye_color_name = models.CharField(unique=True, max_length=25)

    class Meta:
        managed = False
        db_table = 'eye_color'
        ordering = ['eye_color_name']
        verbose_name = 'eye colors of marvel heros'
        verbose_name_plural = 'eye colors of marvel heros '

    def __str__(self):
        return self.eye_color_name


class Gender(models.Model):
    gender_id = models.AutoField(primary_key=True)
    gender_name = models.CharField(unique=True, max_length=8)

    class Meta:
        managed = False
        db_table = 'gender'
        ordering = ['gender_name']
        verbose_name = 'gender of marvel heros'
        verbose_name_plural = 'gender of marvel heros'

    def __str__(self):
        return self.gender_name


class HairColor(models.Model):
    hair_color_id = models.AutoField(primary_key=True)
    hair_color_name = models.CharField(unique=True, max_length=25)

    class Meta:
        managed = False
        db_table = 'hair_color'
        ordering = ['hair_color_name']
        verbose_name = 'hair colors of marvel heros'
        verbose_name_plural = 'hair colors of marvel heros '

    def __str__(self):
        return self.hair_color_name





class Publisher(models.Model):
    publisher_id = models.AutoField(primary_key=True)
    publisher_name = models.CharField(unique=True, max_length=25)

    class Meta:
        managed = False
        db_table = 'publisher'
        ordering = ['publisher_name']
        verbose_name = 'publishers of marvel heros'
        verbose_name_plural = 'publishers of marvel heros '

    def __str__(self):
        return self.publisher_name


class Race(models.Model):
    race_id = models.AutoField(primary_key=True)
    race_name = models.CharField(unique=True, max_length=25)

    class Meta:
        managed = False
        db_table = 'race'
        ordering = ['race_name']
        verbose_name = 'races of marvel heros'
        verbose_name_plural = 'races of marvel heros '

    def __str__(self):
        return self.race_name


class SkinColor(models.Model):
    skin_color_id = models.AutoField(primary_key=True)
    skin_color_name = models.CharField(unique=True, max_length=25)

    class Meta:
        managed = False
        db_table = 'skin_color'
        ordering = ['skin_color_name']
        verbose_name = 'skin colors of marvel heros'
        verbose_name_plural = 'skin colors of marvel heros '

    def __str__(self):
        return self.skin_color_name
