from django.shortcuts import render, redirect
from .models import Movie, Images
from .serializers import MovieSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.forms import UserCreationForm


# welcome page#
def welcome_view(request):
    return render(request,'welcome.html')

# choose either you are user or admin #
def choose_view(request):
    return render(request,'choose.html')

# User --> show all movies
def show_user_view(request):
    obj = Movie.objects.all()
    return render(request,'showmovies.html', {'obj':obj})

# Registration form
def user_register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    return render(request,'register.html',{'form':form})

#-------------------------------------------------------------------------------#
# By Class Based View
class IndexView(APIView):
    allowed_methods = ['GET']
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        queryset = Movie.objects.all()
        # We can filter our movies by name
        name = request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

            ### OR ###
     #### BY FUNCTION BASED VIEW ####
@api_view(['GET','POST'])
def movie_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def movie_detail_view(request,pk):
    try:
        obj = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=MovieSerializer(obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer=MovieSerializer(obj, data=request.data)
        if serializer.is_valid():
            serialixer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
NOTE:-
    You can search via name by passing it as query_param
    for example:- http://127.0.0.1:8000/api/movies/?name=ironman
"""


def poster_view(request):
    obj = Images.objects.all()
    return render(request,'showposter.html', {'obj':obj})
