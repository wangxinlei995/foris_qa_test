import datetime

def date_format_tomorrow(delta=0, format_str='%m-%d'):
    '''
    获取日期字符串
    :param delta: 期望获得的日期与当天的日期的时间间隔
    :param format_str: 日期格式
    :return:
    '''
    all_tomorrow = datetime.date.today() + datetime.timedelta(days=1).strftime("%Y年%m月%d日")
    tomorrow = all_tomorrow[6:]
    return tomorrow

def date_format_nine_day(delta=0, format_str='%m-%d'):
    '''
    获取日期字符串
    :param delta: 期望获得的日期与当天的日期的时间间隔
    :param format_str: 日期格式
    :return:
    '''
    all_nine_day = datetime.date.today() + datetime.timedelta(days=9).strftime("%Y年%m月%d日")
    nine_day = all_nine_day[6:]
    return nine_day

def date_format_today(delta=0, format_str='%m-%d'):
    '''
    获取日期字符串
    :param delta: 期望获得的日期与当天的日期的时间间隔
    :param format_str: 日期格式
    :return:
    '''
    all_today = datetime.date.today().strftime('%Y年%m月%d日')
    today = all_today[6:]
    return today

def exchange_date_format(date_str):
    '''
    转换日期字符串格式为 mm-dd
    :param date_str: 输入格式 1月2日
    :return:
    '''
    month = date_str[:date_str.find('月')]
    day= date_str[date_str.find('月') + 1:date_str.find('日')]
    if len(month)==1:
        month='0'+month
    if len(day)==1:
        day='0'+day
    return f'{month}-{day}'


