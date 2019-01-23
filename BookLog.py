'''
this app will allow you to add books and track them
you can log:
-how much you want to read
-when you are free to read/ when you want to read
-when you want to finish the book by
'''

book_log = {
    #book : page count, progress
    "book" : [""]
}

title = ["   ___            __     __            ", "  / _ )___  ___  / /__  / /  ___  ___ _"," / _  / _ \/ _ \/  '_/ / /__/ _ \/ _ `/", "/____/\___/\___/_/\_\ /____/\___/\_, / ", "                                /___/  ","_______________________________________"]
loading = ["-[==========]-{}%", "-[█=========]-1{}%", "-[██========]-2{}%", "-[███=======]-3{}%", "-[████======]-4{}%", "-[█████=====]-5{}%", "-[██████====]-6{}%", "-[███████===]-7{}%" ,"-[████████==]-8{}%" ,"-[█████████=]-9{}%", "-[██████████]-100%"]

for i in title:
    print(i)