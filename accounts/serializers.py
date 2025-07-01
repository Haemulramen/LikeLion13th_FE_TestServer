from rest_framework import serializers
from accounts.models import User

class RegisterSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='username', write_only=True)
    pw = serializers.CharField(source='password', write_only=True)
    name = serializers.CharField(source='first_name')
    age = serializers.IntegerField(source='last_name', write_only=True)

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
