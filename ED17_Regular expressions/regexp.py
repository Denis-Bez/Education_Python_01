import re

markdown_table = """| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
|   Data1  |   Data2  |   Data3  |
|   Data4  |   Data5  |   Data6  |
|   Data4  |   Data5  |   Data7  |"""

# pattern = r'(\n\|([^-]+)\|(\n|$))'
# pattern = r'\n\|([^-]+?)\|\n'
# pattern = r'((\r?\n){2}|^)([^\r\n]*\|[^\r\n]*(\r?\n)?)+(?=(\r?\n){2}|$)'
#pattern = r'((\n)|^)([^\n]*\|[^\n]*(\n)?)+(?=(\n)|$)' # Последний элемент
# pattern = r'(?<=[-:]\|\n)\|(.*)\n' # Первая строка
# pattern = r'(((\n)|^)([^\n]*\|[^\n]*(\n)?)+)'
pattern = r"((?<=\n)^\|[^-].*\|$)" # все строки
rows = re.findall(pattern, markdown_table, re.MULTILINE)


print(rows)

# for row in rows:
#     cells = [cell.strip() for cell in row.split('|')]
#     print(cells)
