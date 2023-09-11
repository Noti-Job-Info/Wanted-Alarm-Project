from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.permissions import AllowAny, IsAuthenticated

from accounts.serializers import UserSerializer


class UserDetailView(APIView):
    '''
    🔗 url: /accounts/
    ✅ get: 유저 정보 반환
    ✅ put: 유저 정보 수정
    '''
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            user_object = User.objects.get(email=user.email)
            serializer = UserSerializer(user_object)
            return Response(
                serializer.data, 
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            # common > response.py 사용하는 방법?
            return Response(
                {'message': 'User not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request):
        user = request.user
        user_object = User.objects.get(email=user.email)

        serializer = UserSerializer(
            user_object, 
            data=request.data, 
            partial=True
        )
        if serializer.is_valid():
            update_userinfo = serializer.save()
            return Response(
                UserSerializer(update_userinfo).data,
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )