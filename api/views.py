from django.conf import Settings, UserSettingsHolder
from django.shortcuts import render
from re import U
from rest_framework import status, viewsets, generics, permissions
from rest_framework.response import Response
from api.serializers import UpcomingSerializer, OrdersSerializer, RatingsSerializer, CommentsSerializer, UpcomingSerializer, MyTokenObtainPairSerializer, RegisterSerializer
# UserSerializer,
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.authentication import TokenAuthentication

from .models import Upcoming, Orders, Ratings, Comments
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.decorators import login_required



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/',
        '/api/prediction/',
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get('text')
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)



class UpcomingViewSet(viewsets.ModelViewSet):
    queryset = Upcoming.objects.all()
    serializer_class = UpcomingSerializer
    # filter_fields=('user',)
    # permission_classes = [IsAuthenticated,]
    # authentication_classes = ([permissions.JWTAuthentication])
    # def get_queryset(self, user_id):
    #     queryset = queryset.filter(user = user_id)
    #     # serializer_class = UpcomingSerializer
    #     return queryset

    # def get_queryset(self):
    #     user = self.request.user.id
    #     # serializer_class = UpcomingSerializer
    #     return Upcoming.objects.filter(user=user)

    # def get(self, request):
    #     user = request.user
    #     # serializer_class = UpcomingSerializer
    #     upcomings = user.upcoming_set.all()
    #     # return Upcoming.objects.filter(user=user)
    #     serializers = UpcomingSerializer(upcomings, many=True)

    #     return Response(serializers.data)

        

    @action(detail=False, methods=['POST','GET'])
    def orders(self, request, pk):
        upcoming = Upcoming.objects.get(pk=pk)
        if request.method == 'GET':
            self.serializer_class = OrdersSerializer
            queryset = Orders.objects.filter(upcoming=upcoming)
            serializer = OrdersSerializer(queryset,many=True, context={'request':request})
            return Response(serializer.data)
        else:
            self.serializer_class = OrdersSerializer
            queryset = Orders.objects.filter(upcoming=upcoming)
            serializer = OrdersSerializer(data=request.data, context={'request':request})
            serializer.is_valid(raise_exception=True)
            serializer.save(upcoming=upcoming)
            return Response(serializer.data)
    
    @action(detail=False, methods=['DELETE'])
    def remove_order(self, request, pk, order):
        order = Orders.objects.get(pk=order)
        if order.delete():
            return Response({'message':'order deleted'})
        else:
            return Response({'message':'unable to delete order'})
    
    
    @action(detail=False, methods=['POST','GET'])
    def ratings(self, request, pk):
        upcoming = Upcoming.objects.get(pk=pk)
        if request.method == 'GET':
            self.serializer_class = RatingsSerializer
            queryset = Ratings.objects.filter(upcoming=upcoming)
            serializer = RatingsSerializer(queryset, many=True, context={'request':request})
            return Response(serializer.data)
        else:
            self.serializer_class = RatingsSerializer
            queryset = Ratings.objects.filter(upcoming=upcoming)
            serializer = RatingsSerializer(data=request.data, context={'request':request})
            serializer.is_valid(raise_exception=True)
            serializer.save(upcoming=upcoming)
            return Response(serializer.data)

    @action(detail=False, methods=['DELETE'])
    def remove_rating(self, request, pk, rating):
        rating = Ratings.objects.get(pk=rating)
        if rating.delete():
            return Response({'message':'rating deleted'})
        else:
            return Response({'message':'unable to delete rating'})

    @action(detail=False, methods=['POST','GET'])
    def comments(self, request, pk):
        upcoming = Upcoming.objects.get(pk=pk)
        if request.method == 'GET':
            self.serializer_class = CommentsSerializer
            queryset = Comments.objects.filter(upcoming=upcoming)
            serializer = CommentsSerializer(queryset, many=True, context={'request':request})
            return Response(serializer.data)
        else:
            self.serializer_class = CommentsSerializer
            queryset = Comments.objects.filter(upcoming=upcoming)
            serializer = CommentsSerializer(data=request.data, context={'request':request})
            serializer.is_valid(raise_exception=True)
            serializer.save(upcoming=upcoming)
            return Response(serializer.data)
    
    @action(detail=False, methods=['DELETE'])
    def remove_comment(self, request, pk, comment):
        comment = Comments.objects.get(pk=comment)
        if comment.delete():
            return Response({'message':'comment deleted'})
        else:
            return Response({'message':'unable to delete comment'})
