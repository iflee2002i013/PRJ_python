from name_function import get_formatted_name

# 直接运行这个代码不会有任何输出
# 只有在终端中执行：python -m pytest 才会运行测试

def test_first_last_name():
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_middle_last_name():
    formatted_name = get_formatted_name('john', 'hooker', 'lee')
    assert formatted_name == 'John Lee Hooker'

