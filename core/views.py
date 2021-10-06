"""Core Views: Details on what data to show"""

# Python imports
# Django imports
from django.shortcuts import render

# 3rd party apps
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Local app imports
from .common import get_word

class Spellcheck(APIView):
	"""HTTP get request to evaluate passed query"""

	def post(self, request):
		"""Returns spellcheck result"""
		word = request.data['word']

		try:
			function_response = get_word(word)
			return Response(function_response, status=status.HTTP_200_OK)
		except Exception:
			return Response(data={"Word not found"}, status=status.HTTP_404_NOT_FOUND)