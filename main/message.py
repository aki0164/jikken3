import requests

#LINEに通知する関数
def line_notify(message):
 line_notify_token = 'SJvVrgNYPHMTsaE5pRkrx46vVdbYEiHowRRjw7kokF8'
 line_notify_api = 'https://notify-api.line.me/api/notify'
 payload = {'message': message}  #引数として自由に入力することができます
 headers = {'Authorization': 'Bearer ' + line_notify_token}
 requests.post(line_notify_api, data=payload, headers=headers)

#実行したい処理
def hoge(a, b): #a+bの加算結果を返す
 return a + b

if __name__ == '__main__':
 try: #hoge関数を実行
  ans = hoge(1, 1)
 except Exception as e: #エラー時にはエラーメッセージを通知
  line_notify(e) #line_notify関数の引数にエラーメッセージを入力
 else: #エラーでない場合は、指定した文言に加えて、加算結果を通知
  text = "\n高齢者を検知しました。\n施錠する場合は以下のリンクからお願いします。\nhttps://apps.apple.com/jp/app/switchbot/id1087374760 "
  print(text)
  line_notify(text) #line_notify関数の引数に加算結果入力


#実行結果（コマンドプロンプト） プログラムの実行を完了しました