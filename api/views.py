from marvel_world.models import Character, CharacterPower,CharacterComic,Comic,Power
from api.serializers import CharacterSerializer,ComicSerializer
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response


class CharacterViewSet(viewsets.ModelViewSet):
	"""
	This ViewSet provides both 'list' and 'detail' views.
	"""
	queryset = Character.objects.select_related('alignment','gender','race','publisher','skin_color','eye_color','hair_color').order_by('character_name')
	serializer_class = CharacterSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def delete(self, request, pk, format=None):
		site = self.get_object(pk)
		self.perform_destroy(self, site)

		return Response(status=status.HTTP_204_NO_CONTENT)

	def perform_destroy(self, instance):
		instance.delete()
class ComicViewSet(viewsets.ModelViewSet):
	"""
	This ViewSet provides both 'list' and 'detail' views.
	"""
	queryset = Comic.objects.order_by('comic_name')
	serializer_class = ComicSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def delete(self, request, pk, format=None):
		site = self.get_object(pk)
		self.perform_destroy(self, site)

		return Response(status=status.HTTP_204_NO_CONTENT)

	def perform_destroy(self, instance):
		instance.delete()
