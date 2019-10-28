# Research Draft

<!-- TOC -->
* [Introduction]
* [Background]
* [Prior Solution]
 - [Taxonomy]
* [System of Tunneling]
 - [Taxonomy]
* [Hyperthesis]
* [Proposal Idea]

---
# About DNS Tunneling
DNS Tunnelingは，初めに，`strage`と`timing`という二つの仕組みに分類することができる．
`timing`の場合には，転送する情報量は少ないが秘匿性が高く維持できるという特徴がある．
他方で，`strage`手法では秘匿性こそ高くないが転送できる量を増やすことができるという特徴がある．
DNS Tunnelingの対策に関する研究では，多くの場合に`strage`メソッドによるものを検知対象としているものが多い．
実際の攻撃のシーンにおいても，DNS Tunnelingをさらに秘匿化しようというモチベーションというよりは，DNSが多くの場合でモニタリングされていないという事実に基づいてこのDNS Tunnelingメソッドが利用されている背景がある．


---
# System of Tunneling Technique
攻撃自体の仕組みついては，2000年のslashdot(https://slashdot.org/story/00/09/10/2230242/ip-tunneling-through-nameservers)にて報告されている．
2004年には，OzymanDNSがダンカミンスキーによってブラックハットで報告される．

## Client-Server
DNSの権威サーバとして，`server.com`を持っているとするとどんなホスト名を持つDNSクエリも`server.com`へ転送される．すなわち，任意の文字列を権威サーバに送信することができることを意味する．
## Server-Client
DNSは，`リクエスト-レスポンス`の仕組みがベースになっているため，サーバを基点にデータ転送することはできない．
そのため，権威サーバにおいては事前にリソースレコードを転送メディアとして，転送情報を用意をおく．用意された情報をclientサイドから取ってくる．
これによって，サーバからクライアント宛に情報を転送することができるという仕組みである．
この時に使用するリソースレコードにおいては，`A`では4byteと少ないので，一般的な`CNAME`が広く使用される．
`data_from_the_client  = CNAME data_from_the_server.domain.com`

## Tanonomy(分類)
* Strage
* Timing

---
# Prior Solution
* Detection
* プロトコルの拡張・改変

## Detection Taxonomy(分類)
* Payload Analysis
* Traffic Analysis
