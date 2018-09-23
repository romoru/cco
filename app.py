# coding: utf-8
from flask import Flask, render_template
app = Flask(__name__) #インスタンス生成

@app.route("/") #アリケーションルートにアクセスが合った場合
def hello(): #hello関数が動作します。
  return "Hello World!" #ブラウザ画面に"Hello World!"と出力されます。

@app.route("/index") #アプリケーション/indexにアクセスが合った場合
def index():
   return render_template('index.html') #/indexにアクセスが来たらtemplates内のindex.htmlが開きます
#ここがサーバーサイドからクライアントサイドへなにかを渡すときのポイントになります。

if __name__ == "__main__":
    # webサーバー立ち上げ
    app.run()
    
