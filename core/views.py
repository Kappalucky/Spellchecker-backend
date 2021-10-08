"""Core Views: Details on what data to show"""

# Python imports
# Django imports
# 3rd party apps
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Local app imports
from .common import get_word


class Spellcheck(APIView):
    """HTTP request to evaluate passed query"""

    def get(self, request):
        """Returns spellcheck result via GET request"""
        try:
            word = request.query_params["word"]

            if not word and isinstance(word, str):
                return Response(
                    data="No word entered", status=status.HTTP_406_NOT_ACCEPTABLE
                )
        except:
            return Response(
                data="Must include word in query",
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )

        try:
            function_response = get_word(word)
            return Response(function_response, status=status.HTTP_200_OK)
        except Exception:
            return Response(data="Word not found", status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        """Returns spellcheck result via POST request"""
        try:
            word = request.data["word"]

            if not word and isinstance(word, str):
                return Response(
                    data="No word entered", status=status.HTTP_406_NOT_ACCEPTABLE
                )
        except:
            return Response(
                data="Must include word in query",
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )

        try:
            function_response = get_word(word)
            return Response(function_response, status=status.HTTP_200_OK)
        except Exception:
            return Response(data="Word not found", status=status.HTTP_404_NOT_FOUND)
