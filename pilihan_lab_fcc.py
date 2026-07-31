distance_mi = 0.5
is_raining = False 
has_bike = False
has_car = True 
has_ride_share_app = True

if not distance_mi :
    print(False)

elif distance_mi <= 1 :
    if is_raining :
        print(False)
    else :
        print(True)
elif distance_mi > 1 and distance_mi <= 6:
    if has_bike and not is_raining :
        print(True)
    else :
        print(False)
elif distance_mi > 6 :
    if has_car or has_ride_share_app :
        print(True)
    else :
        print(False)