dict_len, code_len = map(int, input().strip().split())
letters = {}
for _ in range(dict_len):
    key, val = input().split(': ')
    letters[key] = val

code = input()

result = ''
count = 0
while len(code) > 0:
    for key, val in letters.items():
        if code.startswith(val):
            result += key
            code = code[len(val):]
            break
print(result)