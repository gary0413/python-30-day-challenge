# Day 1: Python 基礎與第一個程式

## 課程總結

- **環境設定**: 了解如何安裝 Python 直譯器和 VS Code 編輯器，並安裝必要的 Python 延伸模組。
- **`print()` 函式**: 學會使用 `print()` 將文字或變數的值輸出到終端機，這是檢視程式執行結果的基本方法。
- **變數 (Variables)**: 理解變數如同一個帶有標籤的容器，可以儲存資料（例如文字或數字）。學會了如何宣告變數 (`variable_name = value`) 以及如何更新變數的值。
- **字串拼接**: 掌握了使用 `+` 號將多個字串或字串變數連接成一個更長的句子的技巧。

---

## 資深工程師的建議

### 1. 變數命名風格 (Variable Naming Convention)

Python 的官方風格指南 (PEP 8) 建議所有變數都使用 `snake_case` 命名，也就是全小寫字母，並用底線 `_` 分隔單字。這能大幅提升程式碼的可讀性。

```python
# 推薦 👍
first_name = "Gary"
user_age = 30

# 不推薦 👎
# firstName = "Gary"   # 這是小駝峰 (lowerCamelCase)，在 JavaScript 中常見
# FirstName = "Gary"   # 這是大駝峰 (UpperCamelCase)，在 Python 中通常用於命名類別 (Class)
# userage = 30         # 難以閱讀
```

### 2. 程式碼註解 (Code Comments)

註解是寫給「人」看的，用來解釋程式碼背後的「為什麼」。好的註解能幫助自己和同事在未來快速理解程式碼的意圖。

```python
# 這是一個好的註解，解釋了為什麼需要這個變數
# 根據使用者需求，設定預設的城市為台北
default_city = "Taipei"

# 這是一個比較多餘的註解，因為程式碼本身已經很清楚
# 宣告一個變數 first_name
# first_name = "Gary"
```

### 3. 程式碼可讀性 (Readability)

「程式碼是寫給人看的，只是順便讓電腦執行而已。」在運算子 (`=`, `+`, `-` 等) 的兩側加上空格，是提升可讀性最簡單有效的方法。

```python
# 推薦 👍 (可讀性高)
user_name = "Alice" + " " + "Wonderland"
calculated_age = 30 - 5

# 不推薦 👎 (看起來很擁擠)
user_name="Alice"+" "+"Wonderland"
calculated_age=30-5
```

---

## 練習題

### 題目 1：個人資訊

1.  建立一個名為 `city` 的變數，並將您居住的城市名稱（字串）存入其中。
2.  建立一個名為 `country` 的變數，並將您所在的國家名稱（字串）存入其中。
3.  使用 `print()` 和這兩個變數，印出一句話，格式如下：
    `I live in [城市名], [國家名].`

### 題目 2：最愛的食物

1.  建立一個名為 `favorite_food` 的變數，並將您最愛的食物名稱（字串）存入其中。
2.  使用 `print()` 印出一句話，格式如下：
    `My favorite food is [食物名稱].`
3.  將 `favorite_food` 變數的值改成另一樣您喜歡的食物。
4.  再次使用 `print()` 印出同樣格式的句子，看看結果有何不同。