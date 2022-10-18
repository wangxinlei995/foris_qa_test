from lib.util import date_format_tomorrow, date_format_today

#encoding=utf-8
class ElementsId():
     nine_day_forecast='00000000-0000-0072-ffff-ffff000001ac'       #九天预报页面
     local_forecast='00000000-0000-0074-ffff-ffff00000340'     #本港预报
     ext_forecast='00000000-0000-0074-ffff-ffff00000344'   #延伸预报

class ElementsAccessibilityId():
     more_btn='转到上一层级'    #左上角更多选项btn
     btn_list_nine_day_forecast='九天预报'  #往返tab按钮
     tab_list_nine_day_forecast='九天预报'
     tab_list_local_forecast='本港预报'
     tab_extension_clause_forecast='延伸预报'
     tab_tittle_forecast='天气预报'
     datetime_today= date_format_today()
     datetime_tomorrow= date_format_tomorrow()
     chatbot='聊天机械人'
