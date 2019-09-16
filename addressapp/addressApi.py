from rest_framework import serializers, viewsets

from addressapp.models import AddressModel


class AddressModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddressModel
        fields = ('id', 'user_id', 'ads', 'name', 'phone')


# API视图类
class AddressAPIView(viewsets.ModelViewSet):
    queryset = AddressModel.objects.all()
    serializer_class = AddressModelSerializer
