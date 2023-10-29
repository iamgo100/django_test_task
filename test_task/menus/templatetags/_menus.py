from django import template
from menus.models import MenuItem
from django.db import connection

register = template.Library()

def search_childs(parent_id, menu_items):
    curr_menu_items = []
    childs_list = list(filter(lambda el: el["parent_id"]==parent_id, menu_items))
    for child in childs_list:
        curr_menu_items.insert(child["position"]-1, {
            "name": child["name"],
            "url": child["url"],
            "childs": search_childs(child["id"], menu_items)
        })
    return curr_menu_items

@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    old_len_of_queries = len(connection.queries)
    menu_items = list(MenuItem.objects.all().values())
    curr_menu = []
    main_menu_item = list(filter(lambda el: el["code_name"]==menu_name, menu_items))[0]
    if main_menu_item:
        curr_menu = search_childs(main_menu_item["id"], menu_items)
    print(f'кол-во запросов для {menu_name}:', len(connection.queries)-old_len_of_queries)
    return {
        "menu": curr_menu,
        "request": context["request"]
    }


# Этот способ был изначально реализован и протестирован, но в нем содержится 34 запроса к БД,
# поэтому данный способ был отклонен, но оставлен, чтобы было понятно, с чего все началось.

# def search_childs(child_list, menu_items):
#     curr_menu_items = []
#     for child in child_list:
#         curr_item = menu_items.get(id=child.id)
#         print(len(connection.queries))
#         curr_menu_items.insert(curr_item.position-1, {
#             "name": curr_item.name,
#             "url": curr_item.url,
#             "childs": search_childs(curr_item.childs.all(), menu_items)
#         })
#     return curr_menu_items

# @register.inclusion_tag('menu.html', takes_context=True)
# def draw_menu(context, menu_name):
#     menu_items = MenuItem.objects.all()
#     print(len(connection.queries))
#     curr_menu = []
#     main_menu_item = menu_items.filter(code_name=menu_name)
#     print(len(connection.queries))
#     if main_menu_item:
#         curr_menu = search_childs(main_menu_item[0].childs.all(), menu_items)
#     print(len(connection.queries))
#     print(connection.queries)
#     return {
#         "menu": curr_menu,
#         "request": context["request"]
#     }