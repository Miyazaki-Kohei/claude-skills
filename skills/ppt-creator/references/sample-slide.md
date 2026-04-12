---
marp: true
theme: fj
paginate: true
title: サンプルスライド
description: FJ Marp テーマの全機能を 1 ファイルで実演するサンプル。Claude はこのファイルを読んでクラスの正しい使い方とレイアウトの組み合わせ方を学ぶ。
---

<!--
このファイルは FJ Marp テーマの全クラスを 1 つのデッキで実演するリファレンス。
新しいデッキを作るときに「このクラスはどう書くんだっけ？」と迷ったら、ここを引く。
-->

<!-- _class: title -->
<!-- _paginate: false -->

![w:400px](https://placehold.jp/2C67E5/ffffff/400x80.png?text=FJ)

# このページはタイトルに適しています

20XX/XX/XX ここには日付や執筆者の名前など
必要な情報を入力して下さい

---

<!-- _class: section -->
<!-- _paginate: false -->

## レイアウト：中扉・セクション
テキストは左寄せの中央に配置、背景色はグレーになります

---

# 基本のレイアウト

基本のレイアウトを使用する際は必ずスライドタイトルに h1 を利用してください

# 最初のh1以外でもh1を使うことができます

スライドタイトルの下に一本の線が引かれるのでタイトルと内容がハッキリと区別できます

---

# 通常のマークダウン記法

通常のマークダウン記法はそのまま利用することができます。

# 見出し

**太字**, *斜体*, ***太字斜体***, ~~取り消し線~~, `インライン`, [リンク](https://example.com)


- リスト
1. 番号付きリスト


> 引用


```ts
// コードブロック
console.log("Hello, World!");
```

| テーブル | 列2 | 列3 |
| -------- | --- | --- |
| A        | B   | C   |

---
# 通常のMarp記法(よく使うものを抜粋)

## 見出しの一部を**青色のアクセントカラー**にする

```md
## 見出しの一部を**青色のアクセントカラー**にする
見出し内で**に囲まれた部分は青色のアクセントカラーになります
```

画像の横幅・縦幅を変える

![w:100](https://placehold.jp/150x150.png)

```md
![w:100](https://placehold.jp/150x150.png)
w:100 幅100pxで表示
h:100 縦100pxで表示
```

---

<!-- _class: no-header -->

# ヘッダーなしレイアウト（no-header）

このスライドではヘッダー部分が非表示になります
フルスクリーンでコンテンツを表示したい場合に便利です

---

<!-- _class: image -->

# タイトル・図のみ

![w:800px](https://placehold.jp/300x200.png)

---

<!-- _class: image image-shadow -->

# タイトル・図のみ(影付き)

![w:800px](https://placehold.jp/ffffff/8c8c8c/300x200.png)

---

<!-- _class: image -->

# タイトル・図のみ(複数)

![w:500px](https://placehold.jp/300x200.png)
![w:500px](https://placehold.jp/300x200.png)

---


<!-- _class: content-image -->

# レイアウト：タイトル・図・テキスト

![w:700px](https://placehold.jp/300x200.png)

ここにテキストを入れてください。

---

<!-- _class: content-image -->

# レイアウト：タイトル・図・テキスト(複数)

![w:500px](https://placehold.jp/300x200.png)
![w:500px](https://placehold.jp/300x200.png)

ここにテキストを入れてください

---


<!-- _class: content-image-right -->
<!-- 幅を変えたい場合の設定「content-image-right content-60」など -->


# 文章と図を横並びに表現(図が右側)

![w:500px](https://placehold.jp/300x200.png)
- content-image-rightクラスは、右側に画像を配置するレイアウトを提供
- デフォルトでは右側50%の幅になります
- `content-xx`で左側のテキスト領域の幅を調整できます
  - content-30: テキスト領域30%
  - content-40: テキスト領域40%
  - content-60: テキスト領域60%
  - content-70: テキスト領域70%
  - content-80: テキスト領域80%

---

<!-- _class: content-image-left content-60 -->
<!-- 幅を変えたい場合の設定「content-image-left content-60」など -->

# 文章と図を横並びに表現(図が左側)

![w:400px](https://placehold.jp/300x200.png)
![w:400px](https://placehold.jp/300x200.png)

- content-image-leftクラスは、左側に画像を配置するレイアウトを提供
- デフォルトでは左側50%の幅になります
- `content-xx`で左側のテキスト領域の幅を調整できます
  - content-30: テキスト領域30%
  - content-40: テキスト領域40%
  - content-60: テキスト領域60%
  - content-70: テキスト領域70%
  - content-80: テキスト領域80%


---

<!-- _class: column-layout -->

# 横並びレイアウト（column-layout）

<div class="column">

## 左カラム
- ポイント1
- ポイント2
- ポイント3
</div>

<div class="column">

## 中央カラム
1. 手順1
2. 手順2
3. 手順3
</div>

<div class="column">

## 右カラム
1. 方法1
2. 方法2
3. 方法3
</div>

---

<!-- _class: card-grid -->

# card-grid (既定 2 列) は 4 個の同格カードに最適

<div class="card">

## 戦略
現状分析と方針決定を**3 週間**で完了

</div>
<div class="card">

## 設計
アーキ図と API 仕様を**4 週間**で作成

</div>
<div class="card">

## 実装
機能開発と結合を**8 週間**で実施

</div>
<div class="card">

## 検証
受入テストと本番切替を**2 週間**で完了

</div>

---

<!-- _class: card-grid cols-3 -->

# cols-3 は 3 個または 6 個の並びに使う

<div class="card">

## 短期
- 直近 3 ヶ月で着手する施策
- 既存チームで実行可能

</div>
<div class="card">

## 中期
- 3〜12 ヶ月の投資を伴う施策
- 新規採用 2 名が前提

</div>
<div class="card">

## 長期
- 1 年以上を要する構造改革
- 経営層のコミットが必須

</div>

---

<!-- _class: card-grid cols-4 -->

# cols-4 は 4 つの KPI 指標を並べるのに最適 (1 行の数字 + ラベルのみ)

<div class="card">

# 75%

SWE-bench Verified

</div>
<div class="card">

# 89%

GPQA Diamond

</div>
<div class="card">

# 2M

コンテキスト長

</div>
<div class="card">

# $2

Input / 1M tok

</div>

<!--
cols-4 はカード幅が狭いので本文を書かない。`# 大きい数字` + 1 行ラベルに限定する。
長文を入れたいなら cols-3 に落とすか、2 枚に分ける。
-->

---

<!-- _class: all-text-center -->

<!-- ↑ここをtext-center, h1-text-center, h2-text-center, h3-text-center, h4-text-center, h5-text-center, h6-text-centerに変更すると、それぞれの見出しレベルごとに中央揃えになります -->

<!-- all-text-centerに変更すると、スライド内のすべてのテキストが中央揃えになります -->

# テキストの中央揃え（text-center）
<!-- タイトルは影響を受けません -->

# 見出しレベル1のテキスト h1-text-center
## 見出しレベル2のテキスト h2-text-center
### 見出しレベル3のテキスト h3-text-center
#### 見出しレベル4のテキスト h4-text-center
##### 見出しレベル5のテキスト h5-text-center
###### 見出しレベル6のテキスト h6-text-center
通常のテキスト text-center

---

<!-- _class: align-center -->

# スライド全体のテキストの縦方向中央揃え（align-center）
<!-- タイトルは影響を受けません -->

# 見出しレベル1のテキスト
## 見出しレベル2のテキスト
### 見出しレベル3のテキスト

---

<!-- _class: all-text-red -->

<!-- ↑ここをall-text-red, h1-text-red, h2-text-red, h3-text-red, h4-text-red, h5-text-red, h6-text-red, text-redに変更すると、それぞれの見出しレベルごとに赤色になります -->

<!-- all-text-redに変更すると、スライド内のすべてのテキストが赤色になります -->

# テキストの色変更（red）
<!-- タイトルは影響を受けません -->

#  見出しレベル1のテキスト h1-text-red
## 見出しレベル2のテキスト h2-text-red
### 見出しレベル3のテキスト h3-text-red
#### 見出しレベル4のテキスト h4-text-red
##### 見出しレベル5のテキスト h5-text-red
###### 見出しレベル6のテキスト h6-text-red
通常のテキスト text-red


---

<!-- _class: text-blue -->

# テキストの色変更（blue）

## 見出しは通常色のまま

text-blueクラスを使用すると、段落テキストのみが青色になります。見出しは元の色を保持します。

---

# コードブロック

```ts
type User = {
  id: number;
  name: string;
  email: string;
  isActive: boolean;
};

const users: User[] = [
  { id: 1, name: "山田太郎", email: "taro@example.com", isActive: true },
  { id: 2, name: "鈴木花子", email: "hanako@example.com", isActive: false },
  { id: 3, name: "佐藤次郎", email: "jiro@example.com", isActive: true },
];

function printActiveUsers(userList: User[]) {
  console.log("アクティブなユーザー一覧:");
  userList
    .filter(user => user.isActive)
    .forEach(user => {
      console.log(`ID: ${user.id}, 名前: ${user.name}, メール: ${user.email}`);
    });
}

function activateUser(userList: User[], id: number) {
  const user = userList.find(u => u.id === id);
  if (user) {
    user.isActive = true;
    console.log(`${user.name} をアクティブにしました。`);
  } else {
    console.log("該当ユーザーが見つかりません。");
  }
}

printActiveUsers(users);
activateUser(users, 2);
printActiveUsers(users);
```

コードの大きさに合わせて自動でコードブロック内のテキストが小さくなります

---
# その他

## 数式の表示
$$
\sum_{i=1}^{n} x_i = x_1 + x_2 + \cdots + x_n
$$


## 折りたたみ
<details>
<summary>詳細を開く</summary>
詳細内容をここに記載します
</details>


## カスタムCSSの適用
<style>
.highlight-box {
    background-color: #e3f2fd;
    border-left: 4px solid #2196f3;
    padding: 16px;
    margin: 16px 0;
}
</style>

<div class="highlight-box">
このスライド専用のカスタムスタイルを適用できます
</div>

---

<!-- _paginate: false -->

# ページネーション制御

このスライドはページ番号がスキップされます（`_paginate: skip`）。
このスライドはページ番号が表示されなくなります（`_paginate: false`）。

目次や表紙などでページ番号を表示したくない場合に使用します

---

<!-- _class: small-text -->

# 文字を小さくする

`small-text` クラスを使用すると、スライド全体のフォントサイズが20%程度縮小されます。

情報量が多いスライドや、通常のサイズでは収まりきらない内容を表示する際に便利です。

---

<!-- _class: all-text-center align-center -->

![w:450px](https://placehold.jp/2C67E5/ffffff/450x90.png?text=FJ)

# ぜひお試しください！
