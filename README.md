# beat
madcroctony/orangeの三人対戦版（二人対戦も可能）<br>
神経衰弱のオンラインゲーム<br>
a～rのアルファベットのカードを2枚ずつ用意し，同じスペルのカードめくった場合，カードを獲得できる<br>
フレームワークはDjango，サーバはPythonAnywhereを使用<br>
acount：ユーザー名<br>
entry：ログインしているユーザーの人数<br>
turn：1，2の場合，操作できる。3，100の場合，loadボタンをクリックし，相手にターンを渡す<br>
      0：操作できない，1：1枚目のカードを選択できる，2：2枚目のカードを選択できる<br>
      3：カードのアルファベットが間違っている，100：合っている<br>
group：ユーザーが対戦しているグループのメンバー（2人か3人）<br>
get：獲得したカードのスペル<br>
※二人目がログインした後，1分間ログインがない場合（三人目がログインしない場合）は，二人での対戦となる<br>
三人で対戦している動画<br>

https://user-images.githubusercontent.com/76951687/127227371-603001be-f85f-40d7-b147-0bc23b196d5b.mov

https://user-images.githubusercontent.com/76951687/127227466-631ba88f-512b-417b-8025-5211ce215ff8.mov

https://user-images.githubusercontent.com/76951687/127227560-9de18b24-7f80-4c8e-9cbc-9f5819a81b7d.mov

複数の同時対戦も可能<br>

https://user-images.githubusercontent.com/76951687/127227717-7282907e-a5b1-4acd-83bc-a8aef8816e12.mov

https://user-images.githubusercontent.com/76951687/127228023-d6fb7646-537d-4dd5-9bc4-aa7b3fad5f8c.mov

別のグループ

https://user-images.githubusercontent.com/76951687/127227867-6bbb3b80-0310-4104-962e-529309e92c55.mov

