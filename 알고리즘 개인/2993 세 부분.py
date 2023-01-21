s = input()
result = s
for i in range(1, len(s)):
    for j in range(i+1, len(s)):
        result = min(result, s[:i][::-1] + s[i:j][::-1] + s[j:][::-1])
print(result)