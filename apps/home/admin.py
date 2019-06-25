from django.contrib.auth.models import User

import xadmin

from apps.car.models import UserProfile
from apps.comments.models import Book2, Book_classify2
from xadmin import views


# 本质是对表的操作--->操作模型

# 全局配置
# 修改主题 默认是不允许修改


class BaseStyleSetting(object):
    # 可以修改主题
    enable_themes = True
    use_bootswatch = True


# 注册
xadmin.site.register(views.BaseAdminView, BaseStyleSetting)


class GlobalSettings(object):
    site_title = 'e_book后台管理系统'
    site_footer = 'e_book文化股份有限公司'
    menu_style = 'accordion'  # 菜单折叠


class ClassifyAdmin(object):
    list_display = ['name']
    # 后台列表查询条件
    search_fields = ['name']
    list_per_page = 10


class BooksAdmin(object):
    # 后台列表显示列
    list_display = ['book_id', 'book_name', 'author', 'info', 'price']
    # 后台列表查询条件
    search_fields = ['book_id', 'book_name', 'author']
    # 后台列表通过时间查询
    list_per_page = 10


class UserProfileAdmin(object):
    list_display = ['phone', 'desc', 'uid', 'user']
    # 后台列表查询条件
    search_fields = ['phone', 'desc', 'uid', 'user']
    list_per_page = 10




xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Book_classify2, ClassifyAdmin)
xadmin.site.register(Book2, BooksAdmin)
xadmin.site.register(UserProfile, UserProfileAdmin)
