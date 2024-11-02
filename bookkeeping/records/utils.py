import csv
import os
CSV_FILE_PATH = './records.csv'

# 初始化 CSV 文件
def initialize_csv_file():
    if not os.path.exists(CSV_FILE_PATH):
        with open(CSV_FILE_PATH, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Year', 'Month', 'Day', 'Amount', 'Category', 'Remark'])

# 读取所有记录
def read_records():
    initialize_csv_file()  # 确保文件存在
    records = []
    with open(CSV_FILE_PATH, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # 跳过表头
        for idx, row in enumerate(reader):
            records.append({
                "id": idx,
                "year": int(row[0]),
                "month": int(row[1]),
                "day": int(row[2]),
                "amount": float(row[3]),
                "category": row[4],
                "remark": row[5]
            })
    return records

# 保存新记录
def save_record(year, month, day, amount, category, remark):
    initialize_csv_file()  # 确保文件存在
    with open(CSV_FILE_PATH, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([year, month, day, amount, category, remark])

# 写入所有记录（用于更新）
def write_all_records(records):
    with open(CSV_FILE_PATH, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Year', 'Month', 'Day', 'Amount', 'Category', 'Remark'])
        for record in records:
            writer.writerow([record['year'], record['month'], record['day'], record['amount'], record['category'], record['remark']])
