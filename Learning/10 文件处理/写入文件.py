from pathlib import Path

path = Path('programming.txt')
path.write_text("I love programming.\n")

# 写入多行
contents = "I love creating new games.\n"
contents += "I love creating apps that can run in a browser.\n"
contents += "I also love working with data.\n"

path.write_text(contents)