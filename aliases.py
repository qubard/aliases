import sys

def generate_cmd(name, key, messages):
    for i in range(0,len(messages)):
        d = "; alias " + name + " " + name + str(i+1 if i != len(messages)-1 else 0) + '"'
        print('alias ' + name + str(i) + ' "say ' + messages[i] + d + ";")
    print("alias " + name + " " + name + str(0) + ";")
    print("bind " + key + " " + name)

text = sys.argv[1].split(' ')
s = ""
newText = []
for i in range(0, len(text)):
    if(i != len(text)-1):
        text[i] = text[i] + " "
    if(len(s+text[i]) <= 126):
        s = s + text[i]
    else:
        newText.append(s[:-1])
        s = text[i]

newText.append(s)
generate_cmd(sys.argv[2], 'k', newText)