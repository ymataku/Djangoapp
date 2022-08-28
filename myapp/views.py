from django.shortcuts import render
from .models import Test

# Create your views here.

def index(request):
     sample_list = Test.objects.all()
    # 出力
     context = {
        'sample_list':sample_list,
    }
     if request.method == 'POST':
        #フォームからカラム用の変数へ代入
         user_name = is_private = request.POST.get('name', False)
         user_id = is_private = request.POST.get('id', False)

        # 先ほどのカラムを指定して保存
         Test.objects.create(
             test_name=user_name,
             tesetr_id=user_id,
         )
     return render(request,'HTML/index.html',context=context)
    