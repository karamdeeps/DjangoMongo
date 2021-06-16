from user.models import User
from user.serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'delete', 'update', 'put']

    def list(self, request, *args, **kwargs):
        queryset = User.objects.all()
        data_serializer = UserSerializer(queryset, many=True)
        return Response({
            'message': 'Data Fetched Successfully',
            'result': data_serializer.data
        },
            status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        profession = request.data.get('profession')
        salary = request.data.get('salary')
        position = request.data.get('position')
        user_id = User.objects.create(position=position,
                                      name= name,
                                      profession= profession,
                                      salary= salary
                                      )
        return Response({
            'message': 'Data Fetched Successfully',
            'result': {
                'user_id': user_id.id
            }
        },
            status=status.HTTP_200_OK)

    # def update(self, request, *args, **kwargs):
    #     name = request.data.get('name')
    #     profession = request.data.get('profession')
    #     salary = request.data.get('salary')
    #     position = request.data.get('position')

    # def destroy(self, request, *args, **kwargs):
    #     pass
