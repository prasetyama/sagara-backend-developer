from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import PostSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.utils import timezone
from accounts.models import CustomUser


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
	if request.method == 'POST':
		se = PostSerializer(data=request.data)
		
		if request.user.role == "author":
			if se.is_valid():
				
				post = Post(
					title = se.validated_data.get("title"),
					content = se.validated_data.get("content"),
					category = se.validated_data.get("category"),
					created_by = request.user,
					author = request.user
				)
				post.save()

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
	

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_post(request, *args, **kwargs):

	post = get_object_or_404(
			Post,
			id=kwargs['id']
		)
	
	se = PostSerializer(data=request.data)
	
	if request.user.role == "author":
		if se.is_valid():
			
			post.title = se.validated_data.get("title"),
			post.content = se.validated_data.get("content"),
			post.category_id = se.validated_data.get("category")

			post.save()

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


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request, *args, **kwargs):

	if request.user.role == "author":

		post = get_object_or_404(
				Post,
				id=kwargs['id']
			)

		post.deleted_by = request.user
		post.deleted_at = timezone.now()

		post.save()

		payload = {
			'status': 'delete success',
		}

		return Response(payload, status=status.HTTP_200_OK)
	else :
		payload = {
			'status' : 'user not allowed'
		}
		return Response(payload, status=status.HTTP_400_BAD_REQUEST)


