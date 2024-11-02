# 1. 增加记录删除前的状态：在删除记录之前，获取并打印要删除的记录信息，以便于调试和记录操作。
# 2. 打印剩余记录数量：在删除操作后，打印剩余记录的数量，提供更多的运行时信息。
# 3. 返回被删除的记录：在响应中返回被删除的记录信息，增加了接口的返回数据量，便于前端或调用者了解具体删除了什么内容。
@api_view(['DELETE'])
def delete_record(request, record_id):
    records = read_records()  # 读取所有记录

    # 检查记录 ID 是否有效
    if not (0 <= record_id < len(records)):
        return Response({"error": "Record not found"}, status=404)  # 返回404错误

    # 记录删除前的状态
    original_record = records[record_id]  # 获取要删除的记录
    print(f"Deleting record: {original_record}")  # 打印要删除的记录信息

    # 删除指定 ID 的记录
    updated_records = records[:record_id] + records[record_id + 1:]  # 创建更新后的记录列表

    # 保存更新后的记录
    write_all_records(updated_records)  # 保存更新后的记录
    print(f"Record deleted successfully. Remaining records: {len(updated_records)}")  # 打印剩余记录数量

    return Response({"message": "Record deleted successfully", "deleted_record": original_record})  # 返回成功删除的消息和被删除的记录