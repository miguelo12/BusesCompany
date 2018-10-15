from rest_framework.decorators import api_view
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
from rest_framework import viewsets
from django.http import HttpResponse

def public(request):
    return HttpResponse("You don't need to be authenticated to see this")


@api_view(['GET'])
def private(request):
    return HttpResponse("You should not see this message if not authenticated!")