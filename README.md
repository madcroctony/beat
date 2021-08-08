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

https://user-images.githubusercontent.com/76951687/128635535-171e5b2c-6a23-4b65-ab48-950ecec31a8e.mov

https://user-images.githubusercontent.com/76951687/128635549-5cd99cf6-7fff-4c90-9bd3-07edc3149c37.mp4

https://user-images.githubusercontent.com/76951687/128635568-519749a1-f37d-4803-8e8b-a62b2502b6c7.mov

複数の同時対戦も可能<br>

https://user-images.githubusercontent.com/76951687/128635631-b10bbd5c-277a-41eb-be0f-154f45614a7c.mov

https://user-images.githubusercontent.com/76951687/128635664-eb9e029b-33e6-4c90-9c6d-91a708d05399.mp4

別のグループ

https://user-images.githubusercontent.com/76951687/128635687-86183ec6-08bd-4cf5-9e6c-2fd22be7c728.mov

