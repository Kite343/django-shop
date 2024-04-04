from django.core.management.base import BaseCommand
# from goods.temp.goods_list import goods
from goods.management.commands.goods_list import goods
from goods.models import Products

class Command(BaseCommand):
    help = "Create goods"
    def handle(self, *args, **kwargs):
        # for good in goods:
        #     new_good = Products(name=good['name'], image=good['image'], description=good['description'], price=good['price'])
        #     new_good.save()
        good = goods[-1]
        new_good = Products(name=good['name'], image=good['image'], description=good['description'], price=good['price'])
        new_good.save()