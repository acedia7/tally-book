# 1.记录ID有效性检查：增加了对record_id的下界检查，确保其不为负值。
# 2. 动态更新数据：使用循环遍历字段列表，简化了更新数据的逻辑，避免了重复代码。
# 这些优化使得代码更加健壮和可维护。
@api_view(['PUT'])
def update_record(request, record_id):
    # 读取所有记录
    records = read_records()
    
    # 检查记录ID是否有效
    if record_id < 0 or record_id >= len(records):
        return Response({"error": "Record not found"}, status=404)

    # 获取请求数据
    data = request.data
    
    # 更新数据，使用请求中的数据或保留原有数据
    updated_data = {}
    fields = ["year", "month", "day", "amount", "category", "remark"]
    for field in fields:
        if field in data:
            updated_data[field] = data[field]
        else:
            updated_data[field] = records[record_id][field]

    # 更新指定记录
    records[record_id].update(updated_data)
    
    # 写入所有记录
    write_all_records(records)
    
    # 返回成功消息
    return Response({"message": "Record updated successfully"})