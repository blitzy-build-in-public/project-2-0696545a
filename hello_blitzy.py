with open("hello_blitzy.txt", "w", encoding="utf-8", newline="\n") as f:
    for _ in range(50000):
        f.write("Hello Blitzy\n")
