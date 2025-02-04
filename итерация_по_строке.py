def are_you_playing_banjo(name):
    first_letter = name[0]
    if first_letter.lower() == 'r':
        return f'{name} plays banjo'
    return f'{name} does not play banjo'
    # Implement me!
    return name


print(are_you_playing_banjo("martin"))
print(are_you_playing_banjo("Rikke"))
