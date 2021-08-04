import tkinter as tk
import re

class Application(tk.Frame):
    # entry Widget用変数
    entry = None
    weight_entry = None
    height_entry = None
    bmi_result = None

    # 入力制限に失敗した場合に呼ばれる関数
    def invalidText(self):
        print('入力に失敗しました。')

    # 1. 入力制限の条件を設けて検証する関数の名前を決める
    # 4. 入力制限の条件を設けて検証する関数を実装する
    def onValidate(self, S):
        # 入力された文字が半角数字の場合
        # reについて : https://note.nkmk.me/python-re-match-search-findall-etc/
        if re.match(re.compile('[0-9]+'), S): 
            return True
        else:
            # 入力不正のブザーを鳴らす。
            self.bell()
            return False

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("250x150")

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)

        # Windowを親要素とした場合に、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # 2. 1で決めた関数名を、register関数を用いて登録する
        # register : 入力制限を行うための関数の登録を行う。パラメータと関数を紐づけるために必要。
        vcmd = self.register(self.onValidate)

        # frame Widget(Frame)を親要素として、entry Widgetを作成する。
        # width : 幅の設定
        # validate : 入力制限するオプションの値を設定。
        # validatecommand or vcmd : 入力制限用関数の設定。(3. entryのvalidatecommand option or vcmd optionへ、2の戻り値とパラメータを渡す)
        # invalidcommand : 入力制限により、入力不正が発生した場合に呼ばれる関数の設定。
        # Entryについて : https://kuroro.blog/python/PUZp77YFxrXvMCjpZbUg/
        self.entry = tk.Entry(frame, width=15, validate="key", validatecommand=(vcmd, '%S'), invalidcommand=self.invalidText)

        # frame Widget(Frame)を親要素とした場合に、entry Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        #self.entry.pack()

        # 体重入力欄
        self.weight_label = tk.Label(text="体重")#ラベル名
        self.weight_label.pack()#ラベルの配置場所を.packつまりpackオブジェクトで中央に配置
        self.weight_entry = tk.Entry(Application.entry,justify='right', validate="key", validatecommand=(vcmd, '%S'), invalidcommand=self.invalidText)#右寄せ？
        #↑tk.Entry()テキストボックスキーボードで入力する箇所justify複数行テキストの寄せ位置center（デフォルト）,left,right
        self.weight_entry.pack()#入力箇所を上中央に配置　
        # 身長入力欄
        height_label = tk.Label(text="身長")
        height_label.pack()
        # 配置場所はデフォルト(上中央)
        self.height_entry = tk.Entry(Application.entry,justify='right', validate="key", validatecommand=(vcmd, '%S'), invalidcommand=self.invalidText)
        self.height_entry.pack()
        # 計算結果
        bmi_label = tk.Label(text="BMI計算結果")
        bmi_label.pack()
        self.bmi_result = tk.StringVar()#ウィジェットのテキストを編集するために使用。ラベルやボタンの。
        bmi_label = tk.Label(text="", textvariable=self.bmi_result)
        bmi_label.pack()

        def calc_bmi():
            """ BMI 計算 """
            weight = int(app.weight_entry.get())#身長の入力された文字数字をget()で取得
            height = int(app.height_entry.get()) / 100#取得した文字を100で割ってるし割るために数値で整数(int)になおしてる
            bmi = weight / (height * height)#BMIそのものの計算定義
            self.bmi_result.set(str(bmi))#BMIを文字列として結果に出力

        # 計算ボタン
        button = tk.Button(text="計算", command=calc_bmi)
        button.pack()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    # Windowを生成する。
    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()
    app = Application(master=root)
    root.title("BMI計算ツール")#ウィンドウ名もとい画面タイトル
    root.geometry('250x150')#ウィンドウのデフォルトでの画面比率
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()