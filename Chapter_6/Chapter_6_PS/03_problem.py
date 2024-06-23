# “Make a lot of money”, “buy now”, “subscribe this”, “click this”

comment = input("Enter Your Comment: ")
smpLst = ["Make a lot of money", "buy now", "subscribe this", "click this"]

if (
    smpLst[0].lower() in comment.lower()
    or smpLst[1].lower() in comment.lower()
    or smpLst[2].lower() in comment.lower()
    or smpLst[3].lower() in comment.lower()
):
    print("This is a spam")
else:
    print("This is not a spam")
