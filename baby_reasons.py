

'''
This is a program of reasons to compare with my Wife why we should or should not
find out the gender of our child at the 20 week mark
'''

# i will create another version where i will just read from txt file

reasons = "I would like to  prepare for what I am having; Knowing at 20 weeks will be two joys during the process, instead of just finding out once at 40 weeks; \
Finding out will immediately create a bond with unborn babies; Finding out will lower gender disappointment at the birthing process; \
Finding out can help us budget for future plans; You'll get better baby shower gifts if you find out; \
You have time to accept the gender in case you were set on a specific gender; \
You can buy gender specific nursery decorations ahead of time; \
You wont have to worry about getting things setup for the baby after birth, everything will be done".split("; ")


print("These are my  9 reason's for wanting to know the gender of my child! \n")
num = 1

while num < 10:
    for i in num and reasons:
        input("What is your #{} reason?: ".format(num))
        print("My #{} reason is ".format(num) + i + "\n")
        num+=1


print("\n"*3 + "Thank you for taking the time to compare your reasons with my reasons.")