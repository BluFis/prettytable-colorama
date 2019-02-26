# -*- coding: utf-8 -*-
import prettytable as pt
import colorama as ca
from getWeather import GetWeather
import random
ca.init(autoreset=False)
print(ca.Fore.LIGHTYELLOW_EX+ca.Back.BLUE+'                          python cmd天气预报工具v1.0                  '+ ca.Style.RESET_ALL)
def setTextColor(s,forecolor='',backcolor=''):
    temp=[]
    for val in s:
        if "雨" in val:
            temp.append(ca.Fore.WHITE + ca.Back.RED + val + ca.Style.RESET_ALL)
        else:
            temp.append(forecolor+backcolor+val+ca.Style.RESET_ALL)
    return(temp)

gw = GetWeather()
wdata = gw.getWeather()
tb = pt.PrettyTable()
title_array=["日期","星期","温度","天气","风向","风力"]
title_array=setTextColor(title_array,ca.Fore.LIGHTWHITE_EX)
tb.field_names = title_array
color_array=[ca.Fore.LIGHTBLACK_EX,ca.Fore.LIGHTBLUE_EX,ca.Fore.LIGHTGREEN_EX,ca.Fore.LIGHTYELLOW_EX]
for res in wdata:
    color = random.choice(color_array)
    temp = setTextColor([res['days'], res['week'], res['temperature'], res['weather'], res['wind'], res['winp']],color)
    tb.add_row(temp)
tb.set_style(pt.MSWORD_FRIENDLY)
tb.hrules=pt.FRAME
tb.vrules=pt.NONE
tb.horizontal_char = '='
print(tb)
input("输入回车键退出")