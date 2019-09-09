from django.contrib import admin
from .models import UserModel, UserCommentModel, ViceCommentModel
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'pwd', 'sex', 'number', 'img1',
                    'money', 'level', 'is_life', 'is_rm')


class UserCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'goods_id', 'detail', 'time')


class ViceCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_id', 'comment')


admin.site.register(UserModel, UserAdmin)
admin.site.register(UserCommentModel, UserCommentAdmin)
admin.site.register(ViceCommentModel, ViceCommentAdmin)