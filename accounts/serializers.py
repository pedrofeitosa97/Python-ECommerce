from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Account

class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150, validators=[UniqueValidator(Account.objects.all(),'An user with that username already exists')])
    password = serializers.CharField(max_length=150, write_only=True)
    first_name = serializers.CharField(max_length=127)
    last_name = serializers.CharField(max_length=127)
    email = serializers.EmailField(max_length=127, validators=[UniqueValidator(Account.objects.all(),'An user with that email already exists')])

    def create(self, validated_data:dict) -> Account:
        return Account.objects.create_user(**validated_data)
    def update(self, instance: Account, validated_data: dict) -> Account:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
