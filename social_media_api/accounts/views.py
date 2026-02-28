from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


CustomUser = get_user_model()


# REGISTER VIEW

class RegisterView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = None  # if using serializer separately

    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        token = Token.objects.create(user=user)

        return Response({
            "message": "User registered successfully",
            "token": token.key
        }, status=status.HTTP_201_CREATED)



class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser.objects.all(), id=user_id)

        if request.user == user_to_follow:
            return Response({"error": "You cannot follow yourself."}, status=400)

        request.user.following.add(user_to_follow)

        return Response({"message": "User followed successfully"})



class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser.objects.all(), id=user_id)

        request.user.following.remove(user_to_unfollow)

        return Response({"message": "User unfollowed successfully"})