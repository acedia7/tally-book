from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import save_record
from .utils import read_records, write_all_records
import matplotlib.pyplot as plt
import os
from collections import defaultdict
from django.conf import settings

@api_view(['POST'])
def add_record(request):
    data = request.data
    year = data.get('year')
    month = data.get('month')
    day = data.get('day')
    amount = data.get('amount')
    category = data.get('category')
    remark = data.get('remark', '')

    # 检查用户是否提供了所有必填字段
    if not all([year, month, day, amount, category]):
        return Response({"error": "Missing required fields"}, status=400)

    # 保存记录
    save_record(year, month, day, amount, category, remark)
    return Response({"message": "Record added successfully"})


@api_view(['GET'])
def get_records(request):
    records = read_records()
    print("读取的记录:", records)

    # 获取查询参数
    year = request.query_params.get('year')
    month = request.query_params.get('month')
    category = request.query_params.get('category')

    # 根据查询条件过滤记录
    if year is not None:
        records = [record for record in records if record['year'] == int(year)]
    if month is not None:
        records = [record for record in records if record['month'] == int(month)]
    if category is not None:
        records = [record for record in records if record['category'] == category]

    return Response(records)


@api_view(['PUT'])
def update_record(request, record_id):
    records = read_records()
    if record_id >= len(records):
        return Response({"error": "Record not found"}, status=404)

    data = request.data
    updated_data = {
        "year": data.get("year", records[record_id]["year"]),
        "month": data.get("month", records[record_id]["month"]),
        "day": data.get("day", records[record_id]["day"]),
        "amount": data.get("amount", records[record_id]["amount"]),
        "category": data.get("category", records[record_id]["category"]),
        "remark": data.get("remark", records[record_id]["remark"]),
    }

    records[record_id].update(updated_data)
    write_all_records(records)
    return Response({"message": "Record updated successfully"})


@api_view(['DELETE'])
def delete_record(request, record_id):
    records = read_records()
    if record_id >= len(records):
        return Response({"error": "Record not found"}, status=404)

    records.pop(record_id)
    write_all_records(records)
    return Response({"message": "Record deleted successfully"})

@api_view(['POST'])
def get_records_image(request):
    records = read_records()

    # 获取查询参数
    year = request.data.get('year')
    month = request.data.get('month')
    category = request.data.get('category')

    # 根据查询条件过滤记录
    if year is not None:
        records = [record for record in records if record['year'] == int(year)]
    if month is not None:
        records = [record for record in records if record['month'] == int(month)]
    if category is not None:
        records = [record for record in records if record['category'] == category]

    # 如果没有记录，返回错误信息
    if not records:
        return Response({"error": "No records found"}, status=404)

    # 准备数据用于聚合
    daily_totals = defaultdict(int)

    for record in records:
        day = record['day']
        amount = record['amount']
        daily_totals[day] += amount

    # 将聚合后的数据分开为天和对应的总金额
    days = sorted(daily_totals.keys())
    amounts = [daily_totals[day] for day in days]

    # 绘制折线图
    plt.figure(figsize=(10, 5))
    plt.plot(days, amounts, marker='o')
    plt.title(f'Records for {year}-{month}')
    plt.xlabel('Days')
    plt.ylabel('Total Amount')
    plt.grid()

    # 保存图像到本地
    image_path = os.path.join(settings.MEDIA_ROOT, 'charts', f'records_{year}_{month}_{category}.png')
    plt.savefig(image_path)
    plt.close()

    # 返回图像的 URL
    image_url = f"{request.build_absolute_uri(settings.MEDIA_URL)}charts/records_{year}_{month}_{category}.png"
    return Response({"image_url": image_url})

