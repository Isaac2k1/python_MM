def f(a, **keywords):
    print(a)
    for kw in sorted(keywords):
        print(keywords[kw])

f("A", user="finxter42", elo=2500, title="Grand Master")


