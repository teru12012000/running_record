import tkinter as tk
import datetime


#基本設定
app=tk.Tk()
app.geometry("600x400")
app.title("ランニングの記録")

#日付取得
dt_time=datetime.datetime.now()
text_dt=f'{dt_time.year}/{dt_time.month}/{dt_time.day}'
paint_date=tk.Label(app,text=text_dt)
paint_date.place(
  x=500,
  y=0,
)


menu_label=[]
menu_entry=[]
for i in range(3):
  a=i+1
  y_label_position=50*i+30
  y_text_position=50*i+60
  menu_label.append(tk.Label(app,text=f'{a}つ目のメニュー:'))
  menu_entry.append(tk.Entry(app))
  menu_label[i].place(
    x=200,
    y=y_label_position,
    
  )
  menu_entry[i].place(
    x=200,
    y=y_text_position,
    width=200,
  )


#距離の入力
thought_menu_label=tk.Label(app,text='合計走行距離(km)※数字のみ')
thought_menu_entry=tk.Entry(app)


#感想の入力
thought_menu_label=tk.Label(app,text='感想')
thought_menu_entry=tk.Entry(app)
thought_menu_label.place(
  x=200,
  y=250,
)
thought_menu_entry.place(
  x=200,
  y=280,
  width=200,
)




app.mainloop()