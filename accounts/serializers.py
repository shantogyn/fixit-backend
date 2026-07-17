from rest_framework import serializers
from .models import User

#register serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "first_name",
            "username",
            "email",
            "phone_number",
            "password"
        ]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            phone_number=validated_data["phone_number"]
        )

        return user
    
#login serializer
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        username = attrs.get("username")

        if not email and not username:
            raise serializers.ValidationError(
                "Email or username is required."
            )

        return attrs
    


#logout serializer
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()