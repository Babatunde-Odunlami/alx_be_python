#creating a weather advice program
weather = input("what is the weather like today? (sunny/rainy/cold").lower()
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Mak sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have a recommendation for this weather.")

