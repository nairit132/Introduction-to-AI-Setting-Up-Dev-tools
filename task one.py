print("Hello! I am a AI Bot. Whats your name?")
name = input()
print(f"Nice to meet you, {name}!")
print("How are you feeing today? (good or bad?) : ")
mood = input().lower()
if mood == "good":
    print("I am glad to hear that!")
elif mood == "bad":
    print(f"I'm sorry to hear that {name}, hope things get better soon.")    
else: 
    print("I understand that puttting feelings into words is hard, thanks for trying")
print(f"It was nice to chat with you today {name}. 👋👋👋👋  Goodbye")