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

loading = "-[██████████]-100%"
half_loading = "-[█████=====]-50%"

for i in title:
    print(i)

print(loading)
print(half_loading)