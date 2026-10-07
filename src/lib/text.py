def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    text = text.split()
    return " ".join(text)


def tokenize(text: str) -> list[str]:
    ans = []
    word = ""
    for i in range(len(text)):
        if text[i].isalpha() or '0' <= text[i] <= '9' or (text[i] == '-' and i > 0 and i < len(text) - 1):
            word += text[i]
        elif len(word) != 0:
            ans.append(word)
            word = ""
    if len(word) != 0:
        ans.append(word)

    return ans

def count_freq(tokens: list[str]) -> dict[str, int]:
    ans = {}
    for i in tokens:
        if i in ans:
            ans[i] += 1
        else:
            ans[i] = 1

    return ans

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    ans = list(freq.items())
 
    ans = sorted(ans, key=lambda x: (-x[1], x[0]))

    return ans[:n]

print()
print("1. normalize")
print()
print('"ПрИвЕт\\nМИр\\t"', '->', normalize("ПрИвЕт\nМИр\t"))
print('"ёжик, Ёлка"', "->", normalize("ёжик, Ёлка"))
print('"Hello\\r\\nWorld"', "->", normalize("Hello\r\nWorld"))
print('"  двойные   пробелы  "', "->", normalize("  двойные   пробелы  "))
print()

print("2. tokenize")
print()
print('"привет мир"', "->", tokenize("привет мир"))
print('"hello,world!!!"', "->", tokenize("hello,world!!!"))
print('"по-настоящему круто"', "->", tokenize("по-настоящему круто"))
print('"2025 год"', "->", tokenize("2025 год"))
print('"emoji 😀 не слово"', "->", tokenize("emoji 😀 не слово"))
print()

print("3. count_freq + top_n")
print()
print("Токены", ["a","b","a","c","b","a"], "-> частоты", count_freq(["a","b","a","c","b","a"]))
print("top_n(..., n=2) ->", top_n(count_freq(["a","b","a","c","b","a"]), 2))
print("Токены", ["bb","aa","bb","aa","cc"], "-> частоты", count_freq(["bb","aa","bb","aa","cc"]))
print("top_n(..., n=2) ->", top_n(count_freq(["bb","aa","bb","aa","cc"]), 2))
print()