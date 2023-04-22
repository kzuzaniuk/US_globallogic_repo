slowo_uzyt = input("Napisz jakieś słowo: ")
slowo_uzyt = slowo_uzyt.capitalize()

#lub
newstr = slowo_uzyt[0]
newstr = newstr.upper()
newstr = newstr + slowo_uzyt[1:]

print(newstr)
print(slowo_uzyt)