from rest_framework import serializers

from .models import *


class User_RegistrationSerializer(serializers.ModelSerializer):
    repeat_password = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'repeat_password', 'last_name', 'email', 'phone',
                  'role')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        password, repeat_password = attrs.get('password', None), attrs.pop('repeat_password', None)

        if password is None or repeat_password is None:
            raise serializers.ValidationError("Вы забыли заполнить пароль")
        if password != repeat_password:
            raise serializers.ValidationError("Пароль не совпадает")

        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'description', 'resume_file', 'role')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('title',)


class ExperienceSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(read_only=True, many=True)

    class Meta:
        model = Experience
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):
    skills = SkillSerializer(read_only=True, many=True)

    class Meta:
        model = Vacancy
        fields = '__all__'
