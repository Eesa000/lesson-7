def summer_clothing_advice():
    print("🌞 Welcome to the Summer Clothing Advisor! 🌞")
    
    try:
        temp = float(input("Please enter the current temperature in Celsius: "))

        if temp >= 35:
            print("🥵 It's extremely hot! Wear very light clothes, stay hydrated, and avoid going out in the sun too much.")
        elif 30 <= temp < 35:
            print("🌡️ It's hot! Light clothes like shorts, t-shirts, and a hat are perfect.")
        elif 25 <= temp < 30:
            print("😊 Nice summer weather! You can wear light clothing, but maybe carry sunglasses or a hat.")
        elif 20 <= temp < 25:
            print("🌤️ It's warm but not too hot. Light layers or breathable clothes are best.")
        elif 15 <= temp < 20:
            print("🌬️ Slightly cool. You might need a light jacket or sweater.")
        else:
            print("❄️ It's unusually cool for summer. Consider heavier clothes or layers.")
    
    except ValueError:
        print("⚠️ Invalid input. Please enter a valid number for temperature.")