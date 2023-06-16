from flask import Flask    #ライブラリ(Flask)のインポート

app = Flask(__name__)    #Flaskのインスタンスを作成


@app.route('/')        #ルーティングの設定 http://xxx以降のURLのパスを指定
def hello():        #’/’にアクセスした際に呼び出されるメソッド
    return 'Hello, World!'    #Hello World!を返す 
