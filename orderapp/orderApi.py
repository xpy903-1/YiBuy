from rest_framework import serializers, viewsets

from orderapp.models import OrderModel


class OrderModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderModel
        fields = ('id', 'user_id', 'total', 'address_id', 'order_status')


# API视图类
class OrderAPIView(viewsets.ModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = OrderModelSerializer