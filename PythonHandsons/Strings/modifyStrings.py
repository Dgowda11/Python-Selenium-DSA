a = "Hello World"
print(a.lower())
print(a.upper())

b = "    Hello World"
print(b.strip()) # Strip removes any whitespaces in the Begining

print(a.replace("l","e"))
b = ''
for s in a:
    if s == 'l':
        b += 'e'
    else:
        b += s

print(b)

x = "Darsha,n Gowda"
print(x.split(','))
