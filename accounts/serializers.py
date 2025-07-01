from rest_framework import serializers
from accounts.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='username', write_only=True)
    pw = serializers.CharField(source='password', write_only=True)
    name = serializers.CharField(source='first_name')
    age = serializers.IntegerField()

    class Meta:
        model = User

        fields = ['id', 'pw', 'name', 'age']
    
    def validate_id(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user

class AuthSerializer(serializers.Serializer):
    id = serializers.CharField(source='username')
    pw = serializers.CharField(source='password', write_only=True)

    def validate(self, data):
        user = User.get_user_by_username(data['username'])
        if user is None:
            raise serializers.ValidationError("User does not exist.")
        else:
            if not user.check_password(data['password']):
                raise serializers.ValidationError("Incorrect password.")
            
        token = RefreshToken.for_user(user)
        refresh_token = str(token)
        access_token = str(token.access_token)

        data = {
            "user" : user,
            "refresh_token" : refresh_token,
            "access_token" : access_token
        }
        
        return data
