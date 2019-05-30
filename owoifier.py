#!/usr/bin/env python
text = input("input text to owoify: \n")
final_text = ""
for letter in text:
    if letter == "R":
        final_text = final_text + "W"
    elif letter == "r":
        final_text = final_text + "w"
    elif letter == "L":
        final_text = final_text + "W"
    elif letter == "l":
        final_text = final_text + "w"
    else:
        final_text += letter
print("owoified text:" + "\n" + final_text + "\n")
end = input("Press enter to exit" + "\n")
