from django.shortcuts import render
from .models import Pant_list , Store_list
from .api_file.serializer import PantSerializer , StoreSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class pant_view (APIView):
    def get (self ,request):
        pant = Pant_list.objects.all ()
        serializer = PantSerializer (pant , many = True)
        return Response (serializer.data)
    
    def post (self , request) :
        serializer = PantSerializer(data=request.data)
        if serializer.is_valid ():
            serializer.save ()
            return Response (serializer.data)
        else : 
            return Response (serializer.errors)
        
class pant_detail_view (APIView):
    def get (self , request , pk):
        try :
            pant = Pant_list.objects.get (pk = pk)
        except :
            return Response ({'Error' : 'Pant not found'})
        serializer = PantSerializer (pant)
        return Response (serializer.data)
    
    def post (self , request , pk):
        serializer = PantSerializer (data= request.data)
        if serializer.is_valid ():
            serializer.save ()
            return Response (serializer.data)
        else :
            return Response (serializer.errors)
        
class store_view (APIView) :
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get (self , request):
        store = Store_list.objects.all ()
        serializer = StoreSerializer (store , many = True , context = {'request' : request})
        return Response (serializer.data)
    
    
    def post (self , request , pk) :
        serializer = StoreSerializer (data= request.data)
        if serializer.is_valid ():
            serializer.save ()
            return Response (serializer.data)
        else :
            return Response (serializer.errors)
        
    def delete (self , request , pk):
        store = Store_list.objects.get (pk = pk)
        store.delete ()
        return Response (status=status.HTTP_204_NO_CONTENT)
        
class store_detail_view (APIView):
    def get (self , request , pk):
        try :
            store = Store_list.objects.get (pk = pk)
        except :
            return Response ({'Error' , 'Store Not Found'})
        serializer = StoreSerializer (store)
        return Response (serializer.data)
    
    def post (self , request , pk):
        store = Store_list.objects.get (pk = pk)
        serializer = PantSerializer (store , data=request.data)
        if serializer.is_valid ():
            serializer.save ()
            return Response (serializer.data)
        else : 
            return Response (serializer.errors)