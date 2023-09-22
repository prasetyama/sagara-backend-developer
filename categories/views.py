from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import CategoriesSerializer

from rest_framework.permissions import IsAuthenticated

from .models import Categories

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_category(request,):

	if request.method == 'POST':
		se = CategoriesSerializer(data=request.data)
		
		if request.user.role == "author":
			if se.is_valid():
				
				category = Categories(
					display_name = se.validated_data.get("display_name"),
					created_by = request.user
				)
				category.save()

				payload = {
					'status': 'success',
					'data': se.data
				}

				return Response(payload, status=status.HTTP_201_CREATED)
		else :
			payload = {
				'status' : 'user not allowed'
			}
			return Response(payload, status=status.HTTP_400_BAD_REQUEST)
		
		return Response(se.errors, status=status.HTTP_400_BAD_REQUEST)
