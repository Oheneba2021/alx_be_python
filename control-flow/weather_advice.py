weather_list =["sunny", "rainy", "cold"]
ask_user = input("What's the weather like today? (sunny/rainy/cold): ").lower()
if ask_user == "sunny":
    print (" Wear a t-shirt and sunglasses.")
    
elif ask_user == "rainy":
    print (" Don't forget to take an umbrella and a raincoat.")

elif ask_user == "cold":
    print (" Make sure to wear a warm coat and a scarf")

else:
    print (" Sorry, I don't have advice for that weather condition.")