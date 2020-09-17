# coding:utf-8
import random
import tkinter as tk
import tkinter.messagebox as tmsg

def ButtonClick():
    b = editbox1.get()
    tmsg.showinfo("入力されたテキスト",b)

    isok = False
    if len(b) != 4:
        tmsg.showerror("エラー","4桁の数字を入力してください")
    else:
        kazuok = True
        for i in range(4):
            if(b[i] < "0") or (b[i] > "9") :
                tmsg.showerror("エラー","数字ではありません")
                kazuok = False
                break
        if kazuok :
            isok = True
                
    if isok:
#ヒットを判定 P,146
        hit = 0
        for i in range(4):
          if a [i] == int(b[i]):
            hit = hit + 1

#ブロー判定
        blow = 0
        for j in range(4):
          for i in range(4):
            if (int(b[j]) == a[i]) and (a[i] != int(b[i])) and (a[j] != int(b[j])):
             blow = blow + 1
             break
      
#ヒットが４つならあたりで終了
    if hit == 4:
        tmsg.showinfo("あたり！","おめでとうございます。あたりです。")
        #終了
        root.destroy()
    else:
        #ヒット数とブロー数の表示
        rirekibox.insert(tk.END, b + "　／H:" + str(hit) + " B:" + str(blow) + "\n")
        
#最初の４つの数字をランダム表示
a = [random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9)]
 
#ウィンドウを作る
root = tk.Tk()
root.geometry("600x400")
root.title("数あてげーむ")

# 履歴の表示(テキストボックスの表示)
rirekibox = tk.Text(root, font=("Helvetica", 14))
rirekibox.place(x=400, y=0, width=200, height=400)

#ラベルの作成
labell = tk.Label(root, text="数を入力してね", font=("Helvetica", 14))
labell.place(x = 20, y= 20)

#テキストボックスの作成
editbox1 = tk.Entry(width = 4,font=("Helvetica", 28))
editbox1.place(x = 120, y = 60)

#ボタンの作成
buttonl = tk.Button(root, text = "チェック",font=("Helvetica", 14), command=ButtonClick)
buttonl.place(x = 220, y = 70)

#ウィンドウの表示
root.mainloop()
