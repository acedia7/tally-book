@api_view(['DELETE'])
def delete_record(request, record_id):
    records = read_records()  # 读取所有记录，返回一个记录列表

    # 检查记录 ID 是否有效
    if not (0 <= record_id < len(records)):  # 确保 record_id 在有效范围内
        return Response({"error": "Record not found"}, status=404)  # 如果无效，返回404错误，表示未找到记录

    # 记录删除前的状态
    original_record = records[record_id]  # 获取要删除的记录，方便后续返回
    print(f"Deleting record: {original_record}")  # 打印要删除的记录信息，便于调试和记录操作

    # 删除指定 ID 的记录
    updated_records = records[:record_id] + records[record_id + 1:]  # 创建更新后的记录列表，排除要删除的记录

    # 保存更新后的记录
    write_all_records(updated_records)  # 将更新后的记录列表写入存储，保存更改
    print(f"Record deleted successfully. Remaining records: {len(updated_records)}")  # 打印剩余记录数量，提供运行时信息

    # 返回响应，包含成功删除的消息和被删除的记录信息
    return Response({"message": "Record deleted successfully", "deleted_record": original_record})  # 返回成功删除的消息和被删除的记录