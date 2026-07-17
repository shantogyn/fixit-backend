from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
#register serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "full_name",
            "email",
            "phone_number",
            "password"
        ]

    def create(self, validated_data):
        full_name = validated_data.get("full_name", "")
        user = User.objects.create_user(
            username=validated_data["email"],
            email=validated_data["email"],
            password=validated_data["password"],
            full_name=full_name,
            first_name=full_name,
            phone_number=validated_data["phone_number"]
        )

        return user
    
#login serializer
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    full_name = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        full_name = attrs.get("full_name")

        if not email and not full_name:
            raise serializers.ValidationError(
                "Email or full name is required."
            )

        return attrs
    


#logout serializer
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()





class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['full_name'] = user.full_name
        token['email'] = user.email

        return token