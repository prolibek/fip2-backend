import jwt
import requests
import json

from rest_framework.response import Response

from django.conf import settings 
from django.contrib.sites.shortcuts import get_current_site

class AuthorizationMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        access_token = request.COOKIES.get("access-token")
        refresh_token = request.COOKIES.get("refresh-token")

        if access_token is not None:
            key = settings.SECRET_KEY

        try:
            decoded_token = jwt.decode(refresh_token, key, algorithms=['HS256'])
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {decoded_token}'
        
            return self.get_response(request)
        except jwt.ExpiredSignatureError:
            url = f'http://{get_current_site(request)}/api/users/refresh-token/'
            data = {
                'refresh': refresh_token
            }

            refresh = requests.post(
                url, 
                json.dump(data),
                headers = { "Content-Type": "application/json" }            
            )

            refresh = refresh.json()
            new_access_token = refresh['access']

            response = Response()
            response.set_cookie(
                key = settings.SIMPLE_JWT['AUTH_COOKIE'],
                expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                value = new_access_token,
                secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite = settings.SIMPLE_JWT['HTTP_ONLY_SAMESITE']
            )
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {new_access_token}'

            return self.get_response(request)