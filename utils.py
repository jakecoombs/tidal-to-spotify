def stripTrackName(trackName: str) -> str:
    # Remove any text in () or after -
    trackName = trackName.strip()

    splitName = trackName.split(" ")
    for i, word in enumerate(splitName):
        if i > 0 and (word[0] == "(" or word == "-"):
            splitName = splitName[:i]

    joinedName = " ".join(splitName)
    return joinedName.lower()
