def hotel_cost(nights):
    return 140*nights
#define a function called plane_ride_cost that
def plane_ride_cost(city):
    if "charlotte" == city:
        return 183
    elif "tampa" == city:
        return 220
    elif "pittsburgh" == city:
        return 222
    elif "los angeles" == city:
        return 475
        
def rental_car_cost(days):
    if days>=7 :
        return 40*days - 50
    elif days>=3 :
        return 40*days - 20
    else:
        return 40*days

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print("cost of car rental: ", rental_car_cost(5))
print("cost of plane ride: ", plane_ride_cost("los angeles"))

print("cost of hotel room: ", hotel_cost(7))

print("total cost of trip:", trip_cost("los angeles", 7, 500))

print(trip_cost("tampa", 6, 500))