from django.views import View
from rest_framework.decorators import api_view


@api_view(['GET'])
def test():
    print("this is test file")