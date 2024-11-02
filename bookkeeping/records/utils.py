import csv
import os
CSV_FILE_PATH = './records.csv'

# 初始化 CSV 文件
def initialize_csv_file():
    if not os.path.exists(CSV_FILE_PATH):
        with open(CSV_FILE_PATH, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Year', 'Month', 'Day', 'Amount', 'Category', 'Remark'])  # 添加 ID 列


# 读取所有记录
def read_records():
    initialize_csv_file()  # 确保文件存在
    records = []
    with open(CSV_FILE_PATH, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # 跳过表头
        for row in reader:
            records.append({
                "id": int(row[0]),  # 解析 ID
                "year": int(row[1]),
                "month": int(row[2]),
                "day": int(row[3]),
                "amount": float(row[4]),
                "category": row[5],
                "remark": row[6]
            })
    return records


# 保存新记录
def save_record(year, month, day, amount, category, remark):
    initialize_csv_file()  # 确保文件存在
    records = read_records()  # 读取现有记录以获取最新的 ID
    record_id = len(records)  # 新记录的 ID 为现有记录的数量

    with open(CSV_FILE_PATH, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([record_id, year, month, day, amount, category, remark])  # 写入 ID 和记录



# 写入所有记录（用于更新）
def write_all_records(records):
    with open(CSV_FILE_PATH, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Year', 'Month', 'Day', 'Amount', 'Category', 'Remark'])  # 更新表头以包含 ID
        for record in records:
            writer.writerow([record['id'], record['year'], record['month'], record['day'], record['amount'], record['category'], record['remark']])  # 写入 ID
