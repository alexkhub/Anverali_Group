from django.db.models import Prefetch
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
from .models import *
from .serializers import *
from .utils import *


class User_RegistrationCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = User_RegistrationSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CustomerProfileRetrieveView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options', 'trace']

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        profile_serializer = self.serializer_class(obj)
        vacancy = Vacancy.objects.filter(user__slug=obj.slug).prefetch_related(
            Prefetch('skills', queryset=Skill.objects.all()))
        vacancy_serializer = VacancySerializer(vacancy, many=True)

        return Response({
            'profile': profile_serializer.data,
            'vacancy': vacancy_serializer.data

        }, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PerformerProfileRetrieveView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options', 'trace']

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        profile_serializer = self.serializer_class(obj)
        experience = Experience.objects.filter(user__slug=obj.slug).prefetch_related(
            Prefetch('skills', queryset=Skill.objects.all()))
        experience_serializer = VacancySerializer(experience, many=True)

        return Response({
            'profile': profile_serializer.data,
            'experience': experience_serializer.data

        }, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SearchVacancyListView(ListAPIView):
    queryset = Vacancy.objects.all().prefetch_related(
        Prefetch('skills', queryset=Skill.objects.all()))
    serializer_class = VacancySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = VacancyFilter
