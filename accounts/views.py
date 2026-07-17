from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer,LogoutSerializer
from rest_framework.permissions import IsAuthenticated

from .models import User

#register view
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            return Response(
                {
                    "message": "Registration Successful",
                    "user_id": user.id
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# #login view
# class LoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         email = request.data.get("email")
#         password = request.data.get("password")

#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             return Response(
#                 {"message": "Invalid email or password"},
#                 status=status.HTTP_401_UNAUTHORIZED
#             )

#         if not check_password(password, user.password):
#             return Response(
#                 {"message": "Invalid email or password"},
#                 status=status.HTTP_401_UNAUTHORIZED
#             )

#         refresh = RefreshToken.for_user(user)

#         return Response(
#             {
#                 "message": "Login Successful",
#                 "access": str(refresh.access_token),
#                 "refresh": str(refresh),
#                 "user": {
#                     "id": user.id,
#                     "name": user.first_name,
#                     "username": user.username,
#                     "email": user.email,
#                     "role": user.role,
#                 }
#             },
#             status=status.HTTP_200_OK
#         )

#login view with Serializer
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get("email")
        full_name = serializer.validated_data.get("full_name")
        password = serializer.validated_data["password"]

        user = None
        if email:
            user = User.objects.filter(email=email).first()
        elif full_name:
            user = User.objects.filter(full_name=full_name).first()

        if user is None or not user.check_password(password):
            return Response(
                {"message": "Invalid email/full name or password"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user": {
                    "id": user.id,
                    "full_name": user.full_name,
                    "email": user.email,
                    "role": user.role,
                },
            },
            status=status.HTTP_200_OK,
        )

#profile view
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response(
            {
                "id": user.id,
                "full_name": user.full_name,
                "email": user.email,
                "phone_number": user.phone_number,
                "role": user.role,
            },
            status=status.HTTP_200_OK,
        )
    


#logout view
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LogoutSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        refresh_token = serializer.validated_data["refresh"]

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"message": "Logout Successful"},
                status=status.HTTP_205_RESET_CONTENT
            )
        except Exception as e:
            return Response(
                {"message": "Invalid token"},
                status=status.HTTP_400_BAD_REQUEST
            )

#me view
class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        return Response(
            {
                "id": user.id,
                "full_name": user.full_name,
                "email": user.email,
                "phone_number": user.phone_number,
                "role": user.role,
                "status": user.status,
            },
            status=status.HTTP_200_OK
        )