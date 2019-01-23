'''
this app will allow you to add books and track them
you can log:
-how much you want to read
-when you are free to read/ when you want to read
-when you want to finish the book by
'''

book_log = {
    #book : page count, progress
    "A Farewell to Arms" : [332, 22],
    "Calypso" : [261, 130],
    "Anna and the French Kiss" : [300, 5]
}

title = ["   ___            __     __            ", "  / _ )___  ___  / /__  / /  ___  ___ _"," / _  / _ \/ _ \/  '_/ / /__/ _ \/ _ `/", "/____/\___/\___/_/\_\ /____/\___/\_, / ", "                                /___/  ","_______________________________________",""]
loading = ["-[==========]-{}%", "-[█=========]- {}%", "-[██========]- {}%", "-[███=======]- {}%", "-[████======]- {}%", "-[█████=====]- {}%", "-[██████====]- {}%", "-[███████===]- {}%" ,"-[████████==]- {}%" ,"-[█████████=]- {}%", "-[██████████]- {}%"]

for i in title:
    print(i)
#if book_log.get("A Farewell to Arms"[0])
#print(book_log)
print("Library:")
for i in book_log:
    percent = int(round(book_log[i][0]/book_log[i][1]))
    if percent < 10:
        print(i,loading[0].format(percent))
    elif percent < 20:
        print(i,loading[1].format(percent))
    elif percent < 30:
        print(i,loading[2].format(percent))
    elif percent < 40:
        print(i,loading[3].format(percent))
    elif percent < 50:
        print(i,loading[4].format(percent))
    elif percent < 60:
        print(i,loading[5].format(percent))
    elif percent < 70:
        print(i,loading[6].format(percent))
    elif percent < 80:
        print(i,loading[7].format(percent))
    elif percent < 90:
        print(i,loading[8].format(percent))
    else:
        print(i,loading[9].format(percent))
