"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#
brevet_distances = {
200: 13.5,
300: 20,
400: 27,
600: 40,
1000: 75
}


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    if control_dist_km >= brevet_dist_km:
        control_dist_km = brevet_dist_km
    if control_dist_km == 0:
        return brevet_start_time
    elif control_dist_km <= 200:
        time = control_dist_km / 34
        mins = time % 1
        time -= mins
        mins *= 60
        mins = round(mins)
        return brevet_start_time.shift(hours=time, minutes=mins)
    elif control_dist_km <= 400:
        further = control_dist_km - 200
        time = 200 / 34 + further / 32
        mins = time % 1
        time -= mins
        mins *= 60
        mins = round(mins)
        return brevet_start_time.shift(hours=time, minutes=mins)
    elif control_dist_km <= 600:
        further = control_dist_km - 400
        time = 200 / 34 + 200 / 32 + further / 30
        mins = time % 1
        time -= mins
        mins *= 60
        mins = round(mins)
        return brevet_start_time.shift(hours=time, minutes=mins)
    else:
        further = control_dist_km - 600
        time = 200 / 34 + 200 / 32 + 200 / 30 + further / 28
        mins = time % 1
        time -= mins
        mins *= 60
        mins = round(mins)
        return brevet_start_time.shift(hours=time, minutes=mins)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    if control_dist_km == 0:
        return brevet_start_time.shift(hours=1)
    elif control_dist_km >= brevet_dist_km:
        return brevet_start_time.shift(hours=brevet_distances.get(brevet_dist_km))
    elif control_dist_km <= 60:
        time = control_dist_km / 20
        mins = time % 1
        time -= mins
        mins *= 60
        time += 1
        mins = round(mins)
        return brevet_start_time.shift(hours=time, minutes=mins)
    elif control_dist_km > 600:
        further = control_dist_km - 600
        time = 600 / 15 + further / 11.428
        mins = time % 1
        time -= mins
        mins *= 60 
        mins = round(mins)   
        return brevet_start_time.shift(hours=time, minutes=mins)
    else:
        time = control_dist_km / 15
        mins = time % 1    
        time -= mins
        mins *= 60 
        mins = round(mins)   
        return brevet_start_time.shift(hours=time, minutes=mins)
