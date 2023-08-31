import pandas as pd
from datetime import datetime, timedelta

# 设置起始日期和结束日期
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# 创建一个空的DataFrame来保存工作日
workdays_df = pd.DataFrame(columns=['Date', 'Is_Workday'])

# 循环遍历日期范围
current_date = start_date
while current_date <= end_date:
    # 判断当前日期是否为工作日（周一到周五）
    if current_date.weekday() < 5:
        # 将工作日添加到DataFrame中，并将Is_Workday设置为1
        workdays_df = workdays_df._append({'Date': current_date, 'Is_Workday': 1}, ignore_index=True)
    else:
        # 将非工作日添加到DataFrame中，并将Is_Workday设置为0
        workdays_df = workdays_df._append({'Date': current_date, 'Is_Workday': 0}, ignore_index=True)
    # 增加一天
    current_date += timedelta(days=1)

# 将DataFrame保存到Excel文件中
workdays_df.to_excel('workdays_2023.xlsx', index=False)