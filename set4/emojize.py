import emoji
# emojize: converts emojis if use_aliases = True or language = "alias" in nevwer so i need an extra argument

# prompt for a string in English

in_eng = input()
in_emoji = emoji.emojize(in_eng, language="alias")

# output emojized ver
print(in_emoji)
