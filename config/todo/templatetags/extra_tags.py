from email import message
from django import template
import datetime

register = template.Library() # Djangoテンプレートタグライブラリ



@register.simple_tag
def time_stamping():
        now = datetime.datetime.now()
        d = now.strftime('%H:%M:%S')
        return d


@register.simple_tag
def time_judge(updatetime):
#    upd = updatetime   ←これだと「'>=' not supported between instances of 'str' and 'datetime.datetime'」というエラーが出る
    upd = datetime.datetime.strptime(updatetime, '%y/%m/%d %H:%M:%S')
    now = datetime.datetime.now()
    time_over = now + datetime.timedelta(seconds=-3)
    if upd >= time_over:
        return "★"
    else:
        return ""


@register.simple_tag
def add_message(updatetime):
    upd = datetime.datetime.strptime(updatetime, '%y/%m/%d %H:%M:%S')
    now = datetime.datetime.now()
    time_over = now + datetime.timedelta(seconds=-3)
    if upd >= time_over:
        return "1件のタスクが新たに追加されました"
    else:
        return ""

@register.simple_tag
def update_message(updatetime):
    upd = datetime.datetime.strptime(updatetime, '%y/%m/%d %H:%M:%S')
    now = datetime.datetime.now()
    time_over = now + datetime.timedelta(seconds=-3)
    if upd >= time_over:
        return "1件のタスクが更新されました"
    else:
        return ""


"""
@register.simple_tag
def add_message(updatetimes):
    msg = ""
    for updatetime in updatetimes:
        upd = datetime.datetime.strptime(updatetime, '%y/%m/%d %H:%M:%S')
        now = datetime.datetime.now()
        time_over = now + datetime.timedelta(seconds=-3)
        if upd >= time_over:
            msg = "タスクが新たに追加されました"
            break  
    return msg
"""



"""
@register.simple_tag
def update_mark(updatestatus):
        upd = str(updatestatus)
        if upd == "対応中":
                return "★"
        else:
                return " "
"""


"""
@register.filter(name="time_stamping")
def time_stamping():
        now = datetime.datetime.now()
        d = now.strftime('%H:%M')
        return d
"""
