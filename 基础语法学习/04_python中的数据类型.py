# 方式1
print(type("yyds"))
print(type(666))
print(type(13.14))

# 方式二
string_type = type("yyds")
int_type = type(6666)
float_type = type(11.3445)
print(string_type, float_type, int_type)

# 方式三
name = "yyds"
name_type = type(name)
print(name_type)