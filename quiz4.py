import sys

message_dict = dict()
with open(sys.argv[1], "r", encoding="utf-8") as messagelines:
    for line in messagelines:
        if line != "\n":
            message_dict[(tuple(line.split("\t")[:2]))] = line.split("\t")[2]

key_list = sorted(list(message_dict.keys()))
message_ID = []
for i in key_list:
    if not i[0] in message_ID:
        message_ID.append(i[0])

outputfile = open(sys.argv[2], "w")
message_number = 1
for j in message_ID:
    outputfile.write("Message " + str(message_number) + "\n")
    for k in key_list:
        if k[0] == j:
            a = k[0], '\t', k[1], '\t', message_dict[k]
            outputfile.write("".join(a))
    message_number += 1
outputfile.close()
