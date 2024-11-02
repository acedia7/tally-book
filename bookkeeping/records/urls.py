from django.urls import path
from .views import add_record, get_records, update_record, delete_record

urlpatterns = [
    path('', get_records, name='get_records'),  # 查询记录
    path('add/', add_record, name='add_record'),  # 增加记录
    path('update/<int:record_id>/', update_record, name='update_record'),  # 更新记录
    path('delete/<int:record_id>/', delete_record, name='delete_record'),  # 删除记录
]
