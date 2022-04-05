import os,qrcode
from django.views.generic import View
from django.shortcuts import render
from .models import Table1
from .serializers import PriceSerializer
from rest_framework import viewsets

default_qr_extension = '.png'

# Create your views here.
class PriceViewSet(viewsets.ModelViewSet):
    queryset = Table1.objects.all()
    # serializer_class에는 해당 모델에 대한 serializer를 넣어주어야한다.
    serializer_class = PriceSerializer

class IndexView(View):

    def check_qr_exist(self,product_id,product_object):
        if (str(product_id) + ".png") not in os.listdir(os.getcwd()+"/apis/static"):
            obj = list(product_object)[0]
            dict = {
                'id' : product_id,
                'product_name': obj.productname,
                'price': obj.price
            }
            img = qrcode.make(dict)
            img.save(os.getcwd() + "/apis/static/" + str(product_id) + default_qr_extension)

    def get(self,request):
        product_id = 1
        product_object = Table1.objects.filter(pk=product_id)
        self.check_qr_exist(product_id,product_object)
        context = {
            'id' : product_id,
            'image_url' : str(product_id) + default_qr_extension
        }
        return render(request, 'qrview/index.html', context)

    def post(self,request):
        product_id = request.POST['product_id']
        product_object = Table1.objects.filter(pk=product_id)
        self.check_qr_exist(product_id,product_object)
        context = {
            'id' : product_id,
            'image_url': str(product_id) + default_qr_extension
        }
        return render(request, 'qrview/index.html', context)