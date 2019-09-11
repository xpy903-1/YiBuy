from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class CheckGoodsMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        dontfilters = [
            'goods/detail/<uid>',
            'goods/queryimg/img/<uid>',
            'goods/type/list/<fuid>',
        ]
        if request.path not in dontfilters:
            data = {'code': 404, 'msg': 'not found'}

            return JsonResponse(data)