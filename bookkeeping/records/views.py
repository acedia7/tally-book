from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import save_record
from .utils import read_records, write_all_records

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

