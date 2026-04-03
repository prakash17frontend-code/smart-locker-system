from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    password2 = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ["id", "name", "username", "email", "password", "password2"]
        read_only_fields = ["id"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Passwords do not match."})

        if User.objects.filter(username=attrs["username"]).exists():
            raise serializers.ValidationError({"username": "Username already exists."})

        email = attrs.get("email")
        if email and User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Email already exists."})

        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")

        user = User.objects.create_user(
            name=validated_data["name"],
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"],
            role="USER",
        )
        return user