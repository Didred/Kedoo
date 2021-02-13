import rest_framework
import re
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from kedoo.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


# class View(APIView):
    # permission_classes = (IsAuthenticated,)
@api_view(['GET'])
def status(request):
    if request.auth:
        if Token.objects.get(key=request.auth.key):
            return Response(status=rest_framework.status.HTTP_200_OK)
    return Response(status=rest_framework.status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def logout(request):
    if request.auth:
        Token.objects.get(key=request.auth.key).delete()
        return Response(status=rest_framework.status.HTTP_200_OK)
    return Response(status=rest_framework.status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def reg(request):
    serialized = UserSerializer(data=request.data)

    if serialized.is_valid():
        if not re.match(r'(?=.*[0-9])(?=.*[,.!@#$%^&*()\[\]{}/|//?<>=-])(?=.*[a-z])', serialized.data["password"]):
            return Response({"password": "Simple password"}, status=rest_framework.status.HTTP_400_BAD_REQUEST)
        User.objects.create_user(serialized.data["username"], "", serialized.data["password"])
        return Response(serialized.data, status=rest_framework.status.HTTP_201_CREATED)
    else:
        return Response(serialized.errors, status=rest_framework.status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    error = "Invalid username or password"
    try:
        user = User.objects.get(username=request.data["username"])

        if user.check_password(request.data["password"]):
            token, _ = Token.objects.get_or_create(user=user)

            return Response({"token": token.key}, status=rest_framework.status.HTTP_200_OK)
        else:
            return Response({"errors": error}, status=rest_framework.status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"errors": error}, status=rest_framework.status.HTTP_200_OK)


@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response(status=rest_framework.status.HTTP_200_OK)
