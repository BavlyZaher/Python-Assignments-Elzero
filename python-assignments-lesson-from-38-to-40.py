#1
name = input("Put Your Name Here => ").strip().capitalize()
print(f"Hello {name}, Happy To See You Here.")

#2
age = int(input("Put Your Age Here => ").strip())
if age < 16 :
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
else:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")

#3
first_name = input("Put Your First Name Here => ").strip().capitalize()
second_name = input("Put Your Second Name Here => ").strip().capitalize()
print(f"Hello {first_name} {second_name:.1s}")

#4
email = input("Put Your email Here => ").strip().lower()
print(f"Your Name Is {email[ : email.index('@')].capitalize()}")
print(f"Email Service Provider Is {email[email.index('@') +1 : email.index('.')]}")
print(f"Email Service Provider Is {email[email.index('.') +1 : ]}")
