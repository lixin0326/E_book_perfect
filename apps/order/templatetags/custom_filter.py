
'''
过滤器
1.语法格式
2.内置过滤器
3.自定义过滤器

1>在app文件下新建一个

3>实例化过滤器
4>声明过滤器
5>注册过滤器 @register.filter

'''

from django import template
register = template.Library()

# value|multipy:params
@register.filter
def multiply(value, params):
    return value*params