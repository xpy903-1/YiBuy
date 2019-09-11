from rest_framework import serializers, viewsets
from goodsapp.models import GoodsModel
from shopcartapp.models import ShopCarModel, PictureModel


class GoodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GoodsModel
        fields = ('uid', 'name', 'goods_price', 'is_selected', 'goods_img')

class ShopCartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShopCarModel
        fields = ('id', 'count', 'is_selected')

class PictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PictureModel
        fields = ('id', 'picture_name', 'picture_path', 'picture_width', 'picture_height')

class GoodsAPIView(viewsets.ModelViewSet):
    queryset = GoodsModel.objects.all()
    serializer_class = GoodsSerializer

