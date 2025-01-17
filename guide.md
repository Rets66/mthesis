# 修士論文のガイド資料


---
<!--TOC-->
* [ガイド](#guide)
 - [論文に含めたい内容](#content)
 - [骨組み](#chapter)
 - [Comment from Taenaka](#taenaka)
* [はじめに](#intro)
 - [論文テーマ](#theme)
 - [新規性・貢献点](#contribution)
 - [脅威モデル](#model)
 - [方向性](#direction)
* [研究背景](#background)
* [準備](#pre)
 - [DNS](#dns)
 - [分散ハッシュテーブル](#dht)
* [既存研究](#related-works)
 - [DNS Tunneling検知における課題](#problem)
  * [バイパス手法](#bypass)
* [提案手法](#idea)
 - [課題](#issue)
* [評価](#analsys)
 - [実装]
* [議論](#discussion)
 - [ノードにおいて障害が発生した際の対策]



---
<h3 id='guide'>ガイド</h3>
<h4 id='content'>論文に含めたい内容・焦点</h4>
* 検知アプローチの開発
* 既存の検知手法へのバイパス手法の検証テスト
* 再帰問い合わせにおけるハッシュアルゴリズム導入によるTunneling通信への対策
* ドメイン検証を利用したTunneling手法
* 次世代DNS Exfiltration
* DoHを利用したOutcoming手法
* 一般ユーザにおけるDNSプライバシーの課題に対するDoHのソリューションの利用モチベーション

<h4 id='chapter'>骨組み</h4>
* 序論 : 研究全体を俯瞰し，本論の導入に位置づく内容
 - 背景
 - 課題
 - 目的
* 準備 : 本体導入で核となる要素に関する定義及び説明
 - DNSプロトコル
 - 秘匿通信
 - 暗号学的ハッシュ関数
* 関連研究
* 提案手法
* 課題
* 議論
* 結論

<h4 id='taenaka'>Comment from Taenaka</h4>
* Tunnelingへの対応は，定性的な評価で示す

### 既存のDNSと比べた優位性は，定量的に示される必要がある
* 地理的情報をについては，応答する遅延速度で表現すればよい
* TLDがコンテンツをストアしないという脅威は一旦保留
 - ちなみに，BGP的な考えでKVSノードは実際には特定の国のみだけでなく，複数の地理的位置に分布している可能性がある
* ハッシュ値の計算する主体は，複数パターンある
 - ハッシュ値の主体のためのノードを増やしたところで，結局そのノードに負荷が高まってしまう
 - そこで，評価の対象として，それぞれのパターンを検証することで実際の負荷の集中具合を評価することは可能である

---
<h3 id='intro'>序論</h3>
<h4 id='theme'>論文テーマ</h4>

"DNS Exfiltration緩和のためのハッシュ機構に基づいたDNS再帰問い合わせ"
English : "Conventional DNS-friendly Name Resolution System based on DHT against DNS Exfiltration"


<h4 id='purpose'>研究の目的と対象</h4>
- DNS Tunnelingの効率的な検知システムの構築．
- ドメインサイズの長さが長いものに対して，ホワイトリストを作成することによって大きく対処することができるのはないか．
- 過去の研究では，検知率に焦点が向かっているが**スピード**に焦点が当てられている論文が確認することができない．
* DNS のQNAME および レコード領域を利用することによって，各種検知システムをバイパスできる脆弱性がある．
  - シグネチャの場合は，通信に用いられるドメインは都度変わるため本質的な解決に繋がらない
本研究では，予想される秘匿手法を網羅的に実装することで，それらの特徴量を事前に把握することによって，将来攻撃者が当該手法を利用した場合へのカウンターメジャーを提供する
 これまでの既存研究では，一般的に流布している秘匿手法に対する検知に注力されてきた．しかし，実際の攻撃シナリオでは，このような明白なパケットが送信されることは予想されず，より秘匿性の高いパケットを利用した手法による情報流出およびマルウェアの機能追加処理が実施されると予想される．
 そこで，本研究では，上記のような秘匿性の高めた手法を実際に実装し，そのパケットにおけるデータマイニングを通じて，特徴を調査していく．
 ＊双方向通信ではなく，片方向通信による特徴削減：Malware->C2には特徴量としてsubdomainに制約，C2->MalwareにはRRをTXTとするなど．



<h4 id='contribution'>貢献点</h4>
従来の検知手法には使用されることがなかった，ホスト名に関するwhitelistを適用することの検証してみた
* DNSは，その通信ログについて全て保存管理することは容易ではないとうい特性をもっている．そこで，保存or処理するトラフィックを削減することを実現できるのではあればそれは，貢献点として評価することができる．

<h4 id='model'>脅威モデル</h4>

<h4 id='direction'>方向性</h4>
DNS Tunnelingが発生しないDNSのコンセプトから，その実現過程でやってきたことをまとめればいいのではないだろうか．


---
<h3 id='background'>研究背景</h3>
DNS Tunnelingは，タイミングベースの転送手法とデータベースの検知手法があるが，本研究ではデータベースの転送手法の検知に焦点を当てている．

<h4 id='detection'>悪性クエリの検知における課題</h4>
* `Low & Slow`転送手法への対策
 - `Low`  : 一パケットあたりに注入文字列長が少ない
 - `Slow` : 時間あたりのクエリ頻度が少ない



* 1・2・3文字といった非常に少ない転送量による通信への対策
 - 1・2文字などはエントロピーによる評価も困難である : そこで完全に緩和するのであれば，セキュリティポリシーによってルールベースのフィルタリングを実施する他ない
 - 3文字について，一般的なhostnameとして最も使用される : すなわち攻撃者は，3文字による転送が最も検知バイパス性が高いのではないだろうか
 ＊どの程度の文字列からエントロピーがジップの法則に従うのだろうか
* リアルタイム検知の困難性
 - 参照する特徴量がペイロードのみしかないので，

<h5 id='bypass'>バイパス手法</h5>
* 転送する際のホスト名として，AlexaTOP100などで出現するラベルと，アルファベットおよび数字のバリエーションを対応させる手法．
 - トラフィック量の増加は予想されるが，宛先となる権威サーバを分散させることによって，同一ドメインあたりのトラフィック頻度を特徴量とする検知システムもバイパすることを可能にする．

<h4 id='hash'>Qnameハッシュ化の限界</h4>
* 転送文字列長が事前にデータ転送者に認知されている場合，転送文字列長ビットのセキュリティに収束してしまうため，本質的な解決にはならない．

---
<h3 id='pre'>準備</h3>
<h4 id='dht'>分散ハッシュテーブル</h4>


<h3 id='related-works'>既存研究</h3>

<h4 id='problem'>既存検知手法における課題</h4>
* これまでDNS Tunnelingの検知に関わる研究領域で，検知する対象に扱われていたものは，iodine/dnscat2/dns2tcpなどで，これらは明らかにランダムで長文なドメイン名をもつ．
* Tunnelingパケットのデータマイニングによる検知：検知対象が限定的で，新規に考案された秘匿手法には効果がない
* 正規パケットのデータマイニングによるTunnelingパケットのアノマリ検知は，低スループットを与えた場合に対しての効果が不透明
* 実際に攻撃者がDNS Tunnelingを利用することを想定すると，利用するドメインおよびRRなどに綿密な設計を通じて，またDGAを用いるなど正規パケットに似せたクエリを使用することが予想される．
* また別の手法としては，エントロピーを下げるために，事前に用意した対応法を用いて英単語など怪しまれないラベルの生成を試みるものも登場している．これらの手法の課題は，オーバーブロッキングという課題がある．
* 十分にエントリーが少ない場合，分散サーバが能動的にエントリーを収集する操作を実現しなくてはならない．


---
<h3 id='idea'>提案手法</h3>
提案手法では，m bit空間上にレコードを分散させて並べ，各レコードはTLDによって管理される．
テーブル空間は，ハッシュ値の衝突が無視できる程度に大きくする必要がある．
既存の分散ハッシュテーブルとは異なり，ノード自身はハッシュテーブル上には存在せず，通常のIPアドレスで参照される．
レコードを管理するノードをマネージャと呼ばれ，全てのマネージャは，`Digest-ManagerAddress Table`と呼ばれるマネージャがどこからどこまでのハッシュ値の範囲を管理するのかをまとめたテーブルを持ち，リクエストすべき宛先情報を保持する．

#### 前提条件
* DNSアーキテクチャにおいて，DHTのコンテンツの管理するノードはTLDによって管理されるため，
を構成するノード数の増減は多くはない
 - ノード数は，事前に決め打ちで構わない
 - ノード数が決まったら，コンテンツIDを管理するハッシュ空間を決める
```
gTLD = {'com', 'net', 'org'...}
ccTLD = {'jp', 'us', 'cn', 'br'...}
IDN_ccTLD = {'日本', '한국', 'المغرب'...}
node = [gTLD, ccTLD, IDN_ccTLD]

area = [2 ** 256 -1 / len(node)]
for 
```




<h4 id='issue'>課題</h4>
* RRエントリーメカニズムに対するアクセス管理
 現在の提案手法において，同一のデータIDを生成することができた場合に，正当な第三者以外からRRの改ざんおよび更新が勝手に実現され得る．
* DHTに登録されたエントリーRRのTTL管理の問題
* DNS Tunneling(流入)への対策
* ハッシュ値のコリジョンへの対策
* 分散計算リソース上でのハッシュテーブルの共有方法

---
<h3 id='analysis'>評価</h3>
従来の研究で評価されてきた評価項目
* 代表ノードの数の増減に伴うパフォーマンス比較
* トラフィックに関する従来のDNSのと差分評価
 - 従来のDNSアーキテクチャに比べて，どの程度改善できるのか・できないのか
* Lookup Hopの数比較
* 名前解決速度
* 計算リソースの消費
* コンテンツの数は，ハッシュテーブル上にマップできるだけの量を満たすのか

---
<h3 id='discussion'>議論</h3>
* DNSSECの扱いはどうするのか
 - すなわち，権威サーバからフルサービスリゾルバ宛の応答パケットの完全性について

<h4 id='problem-proposal'>研究の課題</h4>
この手法によって，生成されたラベルは，抽出情報の内容秘匿のために暗号処理が施される傾向にある．
そのため，そのラベルは，'laksdlkfhlkjdsnflka.example.com'のように高いエントロピーを示す傾向がある．

またさらに，近年非暗号方式のDNSプロトコルをHTTPSやTLSなどの暗号処理を施そうといて試みが登場している．
例えば，DOH(DNS over HTTPS)は，スタブリゾルバからフルリゾルバまでの通信はHTTPSを利用して暗号化する技術が登場している．
この技術では，Man in the middle攻撃など中間地点からの覗きを防止することには繋がるが，ペイロードが暗号化される分，DNS Covert Channelとしては，攻撃者優位の環境になる可能性が考えられる．
また，これまでの研究では，DNSログの取得によって，不審なリクエストを機械学習的アプローチで判別しようとする試みがある．
しかし，DNSクエリは，ウェブリクエストごとに登場しているため，ログの使用によって，膨大なデータが求められるだけでなく，ネットワークパフォーマンスを低下することが懸念される．
  さらに，サブドメインを利用した手法は，ランダムサブドメイン攻撃(DNS水責め攻撃)というDos攻撃として機能するため，サブドメインに制約を付与することによって，ネットワーク全体に不審なクエリをもつパケットを減少させることは非常に重要であると考える．

      - 問題を深刻にさせている要因：gTLDの増加(Now over 1,200)
      - 英語以外の言語を利用したドメインの普及
    - ネットワークパフォーマンスを低下させない不審ラベルの検知の実現

---
### Comment
* 提案手法のアーキテクチャは，2011のSong&KoyanagiのHybrid DNSに非常に類似している．
 - ストア方法が違い？
* 通信プロトコル
 - リカーシブサーバからのクエリは，ハッシュ値のみをメッセージとする
  * rtypeは，ハッシュ値に内包するため，nullバイトで埋められる
 - DHTからの応答パケットには，contentIDとそれに対する応答のみが返る
