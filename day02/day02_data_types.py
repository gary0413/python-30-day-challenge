# 宣告不同型態的變數
a_string = "我是個字串"
an_integer = 100
a_float = 3.14159

# 使用 type() 函式檢查它們的型態
print( type(a_string) )
print( type(an_integer) )
print( type(a_float) )

# 字串即使內容是數字，它仍然是字串
numeric_string = "123"
print( type(numeric_string) )