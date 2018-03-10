# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers, filters
# import django_filters
from rest_framework import pagination

from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import csv
from models import *
from empinfo import *
from empinfo.serializer import *
from empinfo.permissions import IsOwnerOrReadOnly
from empinfo.pagination import PageLimitOffsetPagination, PagePagination


import json

# Create your views here.


class EmpList(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PagePagination

    def get(self, request, formate=None):
        queryset = Employee.objects.all()
        context = {
            'request': request, }
        serializer = EmployeeSerializer(queryset, many=True, context=context)
        return Response(serializer.data)

    def post(self, request, formate=None):
        context = {
            'request': request, }
        serializer = EmployeeSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # # def perform_create(self, serializer):
    #     context = {
    #         'request': request, }
    #     serializer.save(owner=self.request.user)


class EmpDetails(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    pagination_class = PagePagination

    def get_object(self, pk):
        # import pdb
        # pdb.set_trace()
        try:
            return Employee.objects.filter(pk=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, formate=None):
        queryset = self.get_object(pk)
        context = {
            'request': request, }
        serializer = EmployeeSerializer(queryset, many=True, context=context)
        return Response(serializer.data)

    def put(self, request, pk, formate=None):
        queryset = self.get_object(pk)
        context = {
            'request': request, }
        serializer = EmployeeSerializer(queryset, data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, formate=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeDetails(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
    pagination_class = PagePagination


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PagePagination


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PagePagination


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'employees': reverse('employee-list', request=request, format=format)
    })


class EmployeeHighlight(generics.GenericAPIView):
    queryset = Employee.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        queryset = self.get_object()
        return Response(queryset.highlighted)


class EmpListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('first_name', 'last_name', 'grades')
    pagination_class = PagePagination

    def get_queryset(self, *args, **kwargs):
        # import pdb
        # pdb.set_trace()
        queryset_list = Employee.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(grades__icontains=query)
            ).distinct()
        return queryset_list


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email')
