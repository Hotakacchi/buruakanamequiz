import sys
import random
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

# 問題リスト
quiz_data = [
    {"image": "hosino.png", "answer": ["小鳥遊", "たかなし"], "description": "このキャラクターの名字は？ ヒント: 〇〇〇ホシノ"},
    {"image": "yuka.png", "answer": ["早瀬", "はやせ"], "description": "このキャラクターの名字は？ ヒント: 〇〇ユウカ"},
    {"image": "airi.png", "answer": ["栗村", "くりむら"], "description": "このキャラクターの名字は？ ヒント: 〇〇アイリ"},
    {"image": "aoi.png", "answer": ["扇喜", "おき"], "description": "このキャラクターの名字は？ ヒント: 〇〇アオイ"},
    {"image": "aoba.png", "answer": ["内海", "うつみ"], "description": "このキャラクターの名字は？ ヒント: 〇〇アオバ"},
    {"image": "akane.png", "answer": ["室笠", "むろかさ"], "description": "このキャラクターの名字は？ ヒント: 〇〇アカネ"},
    {"image": "akari.png", "answer": ["鰐渕", "わにぶち"], "description": "このキャラクターの名字は？ ヒント: 〇〇アカリ"},
    {"image": "akira.png", "answer": ["清澄", "きよすみ"], "description": "このキャラクターの名字は？ ヒント: 〇〇アキラ"},
    {"image": "akemi.png", "answer": ["栗浜", "くりはま"], "description": "このキャラクターの名字は？ ヒント: 〇〇アケミ"},
    {"image": "ako.png", "answer": ["天雨", "あまう"], "description": "このキャラクターの名字は？ ヒント: 〇〇アコ"},
    {"image": "azusa.png", "answer": ["白洲", "しらす"], "description": "このキャラクターの名字は？ ヒント: 〇〇アズサ"},
    {"image": "asuna.png", "answer": ["一之瀬", "いちのせ"], "description": "このキャラクターの名字は？ ヒント: 〇〇〇アスナ"},
    {"image": "atuko.png", "answer": ["秤", "はかり"], "description": "このキャラクターの名字は？ ヒント: 〇アツコ"},
    {"image": "ayane.png", "answer": ["奥空", "おくそら"], "description": "このキャラクターの名字は？ ヒント: 〇〇アヤネ"},
    {"image": "ayumu.png", "answer": ["岩櫃", "いわびつ"], "description": "このキャラクターの名字は？ ヒント: 〇〇アユム"},
    {"image": "arisu.png", "answer": ["天童", "てんどう"], "description": "このキャラクターの名字は？ ヒント: 〇〇アリス"},
    {"image": "aru.png", "answer": ["陸八魔", "りくはちま"], "description": "このキャラクターの名字は？ ヒント: 〇〇〇アル"},
    {"image": "iori.png", "answer": ["銀鏡", "しろみ"], "description": "このキャラクターの名字は？ ヒント: 〇〇イオリ"},
    {"image": "izuna.png", "answer": ["久田", "くだ"], "description": "このキャラクターの名字は？ ヒント: 〇〇イズナ"},
    {"image": "izumi.png", "answer": ["獅子堂", "ししどう"], "description": "このキャラクターの名字は？ ヒント: 〇〇〇イズミ"},
    {"image": "itika.png", "answer": ["仲正", "なかまさ"], "description": "このキャラクターの名字は？ ヒント: 〇〇イチカ"},
    {"image": "ibuki.png", "answer": ["丹花", "たんが"], "description": "このキャラクターの名字は？ ヒント: 〇〇イブキ"},
    {"image": "iroha.png", "answer": ["棗", "なつめ"], "description": "このキャラクターの名字は？ ヒント: 〇イロハ"},
    {"image": "ui.png", "answer": ["古関", "こぜき"], "description": "このキャラクターの名字は？ ヒント: 〇〇ウイ"},
    {"image": "utaha.png", "answer": ["白石", "しらいし"], "description": "このキャラクターの名字は？ ヒント: 〇〇ウタハ"},
    {"image": "eimi.png", "answer": ["和泉元", "いずみもと"], "description": "このキャラクターの名字は？ ヒント: 〇〇〇エイミ"},
    {"image": "kai.png", "answer": ["申谷", "しんたに"], "description": "このキャラクターの名字は？ ヒント: 〇〇カイ"},
    {"image": "kaede.png", "answer": ["勇美", "いさみ"], "description": "このキャラクターの名字は？ ヒント: 〇〇カエデ"},
    {"image": "erika.png", "answer": ["旗見", "はたみ"], "description": "このキャラクターの名字は？ ヒント: 〇〇エリカ"},
    {"image": "kaguya.png", "answer": ["漆原", "うるしばら"], "description": "このキャラクターの名字は？ ヒント: 〇〇カグヤ"},
    {"image": "kazusa.png", "answer": ["杏山", "きょうやま"], "description": "このキャラクターの名字は？ ヒント: 〇〇カズサ"},
    {"image": "kasumi.png", "answer": ["鬼怒川", "きぬがわ"], "description": "このキャラクターの名字は？ ヒント: 〇〇〇カスミ"},
    {"image": "kaho.png", "answer": ["桑上", "くわかみ"], "description": "このキャラクターの名字は？ ヒント: 〇〇カホ"},
    {"image": "kaya.png", "answer": ["不知火", "しらぬい"], "description": "このキャラクターの名字は？ ヒント: 〇〇〇カヤ"},
    {"image": "kayoko.png", "answer": ["鬼方", "おにかた"], "description": "このキャラクターの名字は？ ヒント: 〇〇カヨコ"},
    {"image": "karin.png", "answer": ["角楯", "かくだて"], "description": "このキャラクターの名字は？ ヒント: 〇〇カリン"},
    {"image": "kanna.png", "answer": ["尾刃", "おがた"], "description": "このキャラクターの名字は？ ヒント: 〇〇カンナ"},
    {"image": "kikyou.png", "answer": ["桐生", "きりゅう"], "description": "このキャラクターの名字は？ ヒント: 〇〇キキョウ"},
    {"image": "kisaki.png", "answer": ["竜華", "りゅうげ"], "description": "このキャラクターの名字は？ ヒント: 〇〇キサキ"},
    {"image": "kirara.png", "answer": ["夜桜", "よざくら"], "description": "このキャラクターの名字は？ ヒント: 〇〇キララ"},
    {"image": "kirino.png", "answer": ["中務", "なかつかさ"], "description": "このキャラクターの名字は？ ヒント: 〇〇キリノ"},
    {"image": "kokona.png", "answer": ["春原", "すのはら"], "description": "このキャラクターの名字は？ ヒント: 〇〇ココナ"},
    {"image": "kotama.png", "answer": ["音瀬", "おとせ"], "description": "このキャラクターの名字は？ ヒント: 〇〇コタマ"},
    {"image": "kotori.png", "answer": ["豊見", "とよみ"], "description": "このキャラクターの名字は？ ヒント: 〇〇コトリ"},
    {"image": "koharu.png", "answer": ["下江", "しもえ"], "description": "このキャラクターの名字は？ ヒント: 〇〇コハル"},
    {"image": "koyuki.png", "answer": ["黒崎", "くろさき"], "description": "このキャラクターの名字は？ ヒント: 〇〇コユキ"},
    {"image": "saori.png", "answer": ["錠前", "じょうまえ"], "description": "このキャラクターの名字は？ ヒント: 〇〇サオリ"},
    {"image": "saki.png", "answer": ["空井", "そらい"], "description": "このキャラクターの名字は？ ヒント: 〇〇サキ"},
    {"image": "sakurako.png", "answer": ["歌住", "うたずみ"], "description": "このキャラクターの名字は？ ヒント: 〇〇サクラコ"},
    {"image": "satuki.png", "answer": ["京極", "きょうごく"], "description": "このキャラクターの名字は？ ヒント: 〇〇サツキ"},
    {"image": "saya.png", "answer": ["薬子", "やくし"], "description": "このキャラクターの名字は？ ヒント: 〇〇サヤ"},
    {"image": "sigure.png", "answer": ["間宵", "まよい"], "description": "このキャラクターの名字は？ ヒント: 〇〇シグレ"},
    {"image": "sizuko.png", "answer": ["河和", "かわわ"], "description": "このキャラクターの名字は？ ヒント: 〇〇シズコ"},
    {"image": "sinon.png", "answer": ["川流", "かわる"], "description": "このキャラクターの名字は？ ヒント: 〇〇シノン"},
    {"image": "simiko.png", "answer": ["円堂", "えんどう"], "description": "このキャラクターの名字は？ ヒント: 〇〇シミコ"},
    {"image": "zyuri.png", "answer": ["牛牧", "うしまき"], "description": "このキャラクターの名字は？ ヒント: 〇〇ジュリ"},
    {"image": "syuro.png", "answer": ["箭吹", "やぶき"], "description": "このキャラクターの名字は？ ヒント: 〇〇シュロ"},
    {"image": "syun.png", "answer": ["春原", "すのはら"], "description": "このキャラクターの名字は？ ヒント: 〇〇シュン"},
    {"image": "zyunko.png", "answer": ["赤司", "あかし"], "description": "このキャラクターの名字は？ ヒント: 〇〇ジュンコ"},
    {"image": "siroko.png", "answer": ["砂狼", "すなおおかみ"], "description": "このキャラクターの名字は？ ヒント: 〇〇シロコ"},
    {"image": "suou.png", "answer": ["朝霧", "朝霧"], "description": "このキャラクターの名字は？ ヒント: 〇〇スオウ"},
    {"image": "suzumi.png", "answer": ["守月", "もりづき"], "description": "このキャラクターの名字は？ ヒント: 〇〇スズミ"},
    {"image": "sumire.png", "answer": ["乙花", "おとはな"], "description": "このキャラクターの名字は？ ヒント: 〇〇スミレ"},
    {"image": "seia.png", "answer": ["百合園", "ゆりぞの"], "description": "このキャラクターの名字は？ ヒント: 〇〇〇セイア"},
    {"image": "sena.png", "answer": ["氷室", "ひむろ"], "description": "このキャラクターの名字は？ ヒント: 〇〇セナ"},
    {"image": "serika.png", "answer": ["黒見", "くろみ"], "description": "このキャラクターの名字は？ ヒント: 〇〇セリカ"},
    {"image": "serina.png", "answer": ["鷲見", "すみ"], "description": "このキャラクターの名字は？ ヒント: 〇〇セリナ"},
    {"image": "takane.png", "answer": ["三善", "みよし"], "description": "このキャラクターの名字は？ ヒント: 〇〇タカネ"},
    {"image": "tiaki.png", "answer": ["元宮", "もとみや"], "description": "このキャラクターの名字は？ ヒント: 〇〇チアキ"},
    {"image": "tyerino.png", "answer": ["連河", "れんかわ"], "description": "このキャラクターの名字は？ ヒント: 〇〇チェリノ"},
    {"image": "tise.png", "answer": ["和楽", "わらく"], "description": "このキャラクターの名字は？ ヒント: 〇〇チセ"},
    {"image": "tinatu.png", "answer": ["火宮", "ひのみや"], "description": "このキャラクターの名字は？ ヒント: 〇〇チナツ"},
    {"image": "tihiro.png", "answer": ["各務", "かがみ"], "description": "このキャラクターの名字は？ ヒント: 〇〇チヒロ"},
    {"image": "tukuyo.png", "answer": ["大野", "おおの"], "description": "このキャラクターの名字は？ ヒント: 〇〇ツクヨ"},
    {"image": "tubaki.png", "answer": ["春日", "かすが"], "description": "このキャラクターの名字は？ ヒント: 〇〇ツバキ"},
    {"image": "tumugi.png", "answer": ["椎名", "しいな"], "description": "このキャラクターの名字は？ ヒント: 〇〇ツムギ"},
    {"image": "turugi.png", "answer": ["剣先", "けんざき"], "description": "このキャラクターの名字は？ ヒント: 〇〇ツルギ"},
    {"image": "toki.png", "answer": ["飛鳥馬", "あすま"], "description": "このキャラクターの名字は？ ヒント: 〇〇〇トキ"},
    {"image": "tomoe.png", "answer": ["佐城", "さしろ"], "description": "このキャラクターの名字は？ ヒント: 〇〇トモエ"},
    {"image": "nagisa.png", "answer": ["桐藤", "きりふじ"], "description": "このキャラクター名字は？ ヒント: 〇〇ナギサ"},
    {"image": "nagusa.png", "answer": ["御稜", "ごりょう"], "description": "このキャラクターの名字は？ ヒント: 〇〇ナグサ"},
    {"image": "natu.png", "answer": ["柚鳥", "ゆとり"], "description": "このキャラクターの名字は？ ヒント: 〇〇ナツ"},
    {"image": "niya.png", "answer": ["天地", "あまち"], "description": "このキャラクターの名字は？ ヒント: 〇〇ニヤ"},
    {"image": "neru.png", "answer": ["美甘", "みかも"], "description": "このキャラクターの名字は？ ヒント: 〇〇ネル"},
    {"image": "noa.png", "answer": ["生塩", "うしお"], "description": "このキャラクターの名字は？ ヒント: 〇〇ノア"},
    {"image": "nozomi.png", "answer": ["橘", "たちばな"], "description": "このキャラクターの名字は？ ヒント: 〇ノゾミ"},
    {"image": "nodoka.png", "answer": ["天見", "あまみ"], "description": "このキャラクターの名字は？ ヒント: 〇〇ノドカ"},
    {"image": "nonomi.png", "answer": ["十六夜", "いざよい"], "description": "このキャラクターの名字は？ ヒント: 〇〇〇ノノミ"},
    {"image": "hasumi.png", "answer": ["羽川", "はねかわ"], "description": "このキャラクターの名字は？ ヒント: 〇〇ハスミ"},
    {"image": "hanae.png", "answer": ["朝顔", "あさがお"], "description": "このキャラクターの名字は？ ヒント: 〇〇ハナエ"},
    {"image": "hanako.png", "answer": ["浦和", "うらわ"], "description": "このキャラクターの名字は？ ヒント: 〇〇ハナコ"},
    {"image": "haruka.png", "answer": ["伊草", "いぐさ"], "description": "このキャラクターの名字は？ ヒント: 〇〇ハルカ"},
    {"image": "haruna.png", "answer": ["黒舘", "くろだて"], "description": "このキャラクターの名字は？ ヒント: 〇〇ハルナ"},
    {"image": "hare.png", "answer": ["小鈎", "おまがり"], "description": "このキャラクターの名字は？ ヒント: 〇〇ハレ"},
    {"image": "hikari.png", "answer": ["橘", "たちばな"], "description": "このキャラクターの名字は？ ヒント: 〇ヒカリ"},
    {"image": "hina.png", "answer": ["空崎", "そらさき"], "description": "このキャラクターの名字は？ ヒント: 〇〇ヒナ"},
    {"image": "hinata.png", "answer": ["若葉", "わかば"], "description": "このキャラクターの名字は？ ヒント: 〇〇ヒナタ"},
    {"image": "hibiki.png", "answer": ["猫塚", "ねこづか"], "description": "このキャラクターの名字は？ ヒント: 〇〇ヒビキ"},
    {"image": "hifumi.png", "answer": ["阿慈谷", "あじたに"], "description": "このキャラクターの名字は？ ヒント: 〇〇〇ヒフミ"},
    {"image": "himari.png", "answer": ["明星", "あけぼし"], "description": "このキャラクターの名字は？ ヒント: 〇〇ヒマリ"},
    {"image": "hiyori.png", "answer": ["槌永", "つちなが"], "description": "このキャラクターの名字は？ ヒント: 〇〇ヒヨリ"},
    {"image": "fi-na.png", "answer": ["朝比奈", "あさひな"], "description": "このキャラクターの名字は？ ヒント: 〇〇〇フィーナ"},
    {"image": "fuka.png", "answer": ["愛清", "あいきよ"], "description": "このキャラクターの名字は？ ヒント: 〇〇フウカ"},
    {"image": "fubuki.png", "answer": ["合歓垣", "ねむがき"], "description": "このキャラクターの名字は？ ヒント: 〇〇〇フブキ"},
    {"image": "mai.png", "answer": ["風巻", "かざまき"], "description": "このキャラクターの名字は？ ヒント: 〇〇マイ"},
    {"image": "maki.png", "answer": ["小塗", "こぬり"], "description": "このキャラクターの名字は？ ヒント: 〇〇マキ"},
    {"image": "makoto.png", "answer": ["羽沼", "はぬま"], "description": "このキャラクターの名字は？ ヒント: 〇〇マコト"},
    {"image": "masiro.png", "answer": ["静山", "しずやま"], "description": "このキャラクターの名字は？ ヒント: 〇〇マシロ"},
    {"image": "mari-.png", "answer": ["伊落", "いおち"], "description": "このキャラクターの名字は？ ヒント: 〇〇マリー"},
    {"image": "marina.png", "answer": ["池倉", "いけくら"], "description": "このキャラクターの名字は？ ヒント: 〇〇マリナ"},
    {"image": "mika.png", "answer": ["聖園", "みその"], "description": "このキャラクターの名字は？ ヒント: 〇〇ミカ"},
    {"image": "misaki.png", "answer": ["戒野", "いましの"], "description": "このキャラクターの名字は？ ヒント: 〇〇ミサキ"},
    {"image": "mitiru.png", "answer": ["千鳥", "ちどり"], "description": "このキャラクターの名字は？ ヒント: 〇〇ミチル"},
    {"image": "midori.png", "answer": ["才羽", "さいば"], "description": "このキャラクターの名字は？ ヒント: 〇〇ミドリ"},
    {"image": "mina.png", "answer": ["近衛", "このえ"], "description": "このキャラクターの名字は？ ヒント: 〇〇ミナ"},
    {"image": "mine.png", "answer": ["蒼森", "あおもり"], "description": "このキャラクターの名字は？ ヒント: 〇〇ミネ"},
    {"image": "minori.png", "answer": ["安守", "やすもり"], "description": "このキャラクターの名字は？ ヒント: 〇〇ミノリ"},
    {"image": "mimori.png", "answer": ["水羽", "みずは"], "description": "このキャラクターの名字は？ ヒント: 〇〇ミモリ"},
    {"image": "miyako.png", "answer": ["月雪", "つきゆき"], "description": "このキャラクターの名字は？ ヒント: 〇〇ミヤコ"},
    {"image": "miyu.png", "answer": ["霞沢", "かすみざわ"], "description": "このキャラクターの名字は？ ヒント: 〇〇ミユ"},
    {"image": "mutuki.png", "answer": ["浅黄", "あさぎ"], "description": "このキャラクターの名字は？ ヒント: 〇〇ムツキ"},
    {"image": "megu.png", "answer": ["下倉", "しもくら"], "description": "このキャラクターの名字は？ ヒント: 〇〇メグ"},
    {"image": "meru.png", "answer": ["姫木", "ひめき"], "description": "このキャラクターの名字は？ ヒント: 〇〇メル"},
    {"image": "moe.png", "answer": ["風倉", "かぜくら"], "description": "このキャラクターの名字は？ ヒント: 〇〇モエ"},
    {"image": "momizi.png", "answer": ["秋泉", "あきいずみ"], "description": "このキャラクターの名字は？ ヒント: 〇〇モミジ"},
    {"image": "momoi.png", "answer": ["才羽", "さいば"], "description": "このキャラクターの名字は？ ヒント: 〇〇モモイ"},
    {"image": "momoka.png", "answer": ["由良木", "ゆらき"], "description": "このキャラクターの名字は？ ヒント: 〇〇〇モモカ"},
    {"image": "yakumo.png", "answer": ["新槇", "あらまき"], "description": "このキャラクターの名字は？ ヒント: 〇〇ヤクモ"},
    {"image": "yukari.png", "answer": ["勘解由小路", "かでのこうじ"], "description": "このキャラクターの名字は？ ヒント: 〇〇〇〇〇ユカリ"},
    {"image": "yukino.png", "answer": ["七度", "しちど"], "description": "このキャラクターの名字は？ ヒント: 〇〇ユキノ"},
    {"image": "yuzu.png", "answer": ["花岡", "はなおか"], "description": "このキャラクターの名字は？ ヒント: 〇〇ユズ"},
    {"image": "yume.png", "answer": ["梔子", "くちなし"], "description": "このキャラクターの名字は？ ヒント: 〇〇ユメ"},
    {"image": "yosimi.png", "answer": ["伊原木", "いばらぎ"], "description": "このキャラクターの名字は？ ヒント: 〇〇〇ヨシミ"},
    {"image": "rabu.png", "answer": ["河駒風", "こまかぜ"], "description": "このキャラクターの名字は？ ヒント: 〇〇〇ラブ"},
    {"image": "rio.png", "answer": ["調月", "つかつき"], "description": "このキャラクターの名字は？ ヒント: 〇〇リオ"},
    {"image": "rin.png", "answer": ["七神", "なながみ"], "description": "このキャラクターの名字は？ ヒント: 〇〇リン"},
    {"image": "rumi.png", "answer": ["朱城", "あけしろ"], "description": "このキャラクターの名字は？ ヒント: 〇〇ルミ"},
    {"image": "rei.png", "answer": ["野正", "のまさ"], "description": "このキャラクターの名字は？ ヒント: 〇〇レイ"},
    {"image": "reisa.png", "answer": ["宇沢", "うざわ"], "description": "このキャラクターの名字は？ ヒント: 〇〇レイサ"},
    {"image": "reijo.png", "answer": ["鹿山", "かやま"], "description": "このキャラクターの名字は？ ヒント: 〇〇レイジョ"},
    {"image": "renge.png", "answer": ["不破", "ふわ"], "description": "このキャラクターの名字は？ ヒント: 〇〇レンゲ"},
    {"image": "wakamo.png", "answer": ["狐坂", "こさか"], "description": "このキャラクターの名字は？ ヒント: 〇〇ワカモ"},
    # 他の問題もここに追加 {"image": "image_path.png", "answer": ["答え"], "description": "説明文"},
]

class QuizWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ブルアカクイズ")
        self.setGeometry(100, 100, 800, 600)
        self.font = QFont("Meiryo", 18)
        self.remaining_quiz = quiz_data.copy()
        self.quiz = random.choice(quiz_data)
        self.correct_count = 0

        # 画面端に表示するラベル（例：右下に表示）
        # ※変更禁止
        self.corner_label = QLabel("Hotakacchi作 ©Yostar", self)
        self.corner_label.setFont(QFont("Meiryo", 10))
        self.corner_label.setStyleSheet("color: gray;")
        self.corner_label.setAlignment(Qt.AlignRight | Qt.AlignBottom)

        # 画像
        self.image_label = QLabel(self)
        self.set_image(self.quiz["image"])

        # 説明文
        self.desc_label = QLabel(self.quiz["description"], self)
        self.desc_label.setFont(self.font)

        # 入力欄
        self.input = QLineEdit(self)
        self.input.setFont(self.font)
        self.input.returnPressed.connect(self.check_answer)

        # ボタン
        self.button = QPushButton("答える", self)
        self.button.setFont(self.font)
        self.button.clicked.connect(self.check_answer)

        # レイアウト
        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.desc_label)
        vbox.addWidget(self.input)
        vbox.addWidget(self.button)
        self.setLayout(vbox)

        # 右下にラベルを置くためのレイアウト
        hbox_bottom = QHBoxLayout()
        hbox_bottom.addStretch()
        hbox_bottom.addWidget(self.corner_label)
        vbox.addLayout(hbox_bottom)

    def set_image(self, image_path):
        abs_path = os.path.join(os.path.dirname(__file__), image_path)
        pixmap = QPixmap(abs_path)
        if pixmap.isNull():
            self.image_label.setText("画像が見つかりません")
            self.image_label.setPixmap(QPixmap())  # 画像をクリア
        else:
            pixmap = pixmap.scaled(300, 300)
            self.image_label.setPixmap(pixmap)
            self.image_label.setFixedSize(300, 300)

    def check_answer(self):
        user_input = self.input.text()
        answers = self.quiz["answer"]
        if isinstance(answers, list):
            correct = user_input in answers
            answer_text = " / ".join(answers)
        else:
            correct = user_input == answers
            answer_text = answers

        if correct:
            self.correct_count += 1
            QMessageBox.information(self, "結果", f"正解！\n正解は: {answer_text}")
        else:
            QMessageBox.warning(self, "結果", f"不正解！\n正解は: {answer_text}")
        self.next_quiz()

    def next_quiz(self):
        self.remaining_quiz.remove(self.quiz)
        total = len(quiz_data)
        done = total - len(self.remaining_quiz)
        bar_length = 50  # バーの長さ
        filled = int(bar_length * done / total)
        bar = "■" * filled + " " * (bar_length - filled)
        print(f"\r[{bar}] {done}/{total} 正解数: {self.correct_count}", end = "")
        sys.stdout.flush()

        if not self.remaining_quiz:
            print()
            print(f"最終正解数: {self.correct_count}")
            QMessageBox.information(self, "終了", "全ての問題が終了しました！")
            self.close()
            return
        self.quiz = random.choice(self.remaining_quiz)
        self.set_image(self.quiz["image"])
        self.desc_label.setText(self.quiz["description"])
        self.input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuizWindow()
    window.show()
    sys.exit(app.exec_())