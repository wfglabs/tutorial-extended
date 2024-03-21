from django.contrib.auth.hashers import check_password
from django.core.mail import EmailMultiAlternatives
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import User
from .serializers import UserSerializer
from tutorialextended import settings

@api_view(['GET'])
def get_data(request):
    print(settings.EMAIL_HOST_USER)
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():

        serializer.save()

        sender_email = settings.EMAIL_HOST_USER
        receiver_email = serializer.data.get('email')

        with open('tutorialextended/templates/email.html', 'r') as file:
            html_content = file.read()

        msg = EmailMultiAlternatives("Welcome to Tutorial Extended !!", '', sender_email, [receiver_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def authenticate_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'authenticated': False, 'error': 'Wrong email provided, please try again'})

    if(check_password(password, user.password)):
        return Response({'authenticated': True})
    else:
        return Response({'authenticated': False, 'error': 'Wrong password entered, please try again'})