def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottem = symbol * len(formatted_text)
    return f"{top_bottem}\n{formatted_text}\n{top_bottem}"


# main routine
print(formatter("-", "welcome to the lucky unicorn game"))
print()
print(formatter("!", "congradtulations, you got a unicorn"))
print()
print(formatter("*", "goodbye"))
