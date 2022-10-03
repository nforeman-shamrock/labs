def reward_function(params):
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    is_left_of_center = params['is_left_of_center']
    steering_angle = params['steering_angle']
    is_offtrack = params['is_offtrack']
    speed = params['speed']

    waypoints = params['waypoints']
    first_wp, second_wp = params['closest_waypoints']

    first = waypoints[first_wp]
    second = waypoints[second_wp]

    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    #Entering turn 
    x_change =  (first[0] / second[0]) != 1
    y_change =  (first[1] / second[1]) != 1
    reward = 0
    near_turn = False
    if x_change and y_change: 
        #right turn
        if steering_angle < 0 and (not is_offtrack) and not is_left_of_center:
            if speed < 4: 
                reward = 1.0
        #left turn
        if steering_angle > 0 and (not is_offtrack) and is_left_of_center:
            if speed < 4: 
                reward = 1.0
    else:
     if not is_offtrack: 
        if speed > 3:
            reward = 0.5
        if speed > 4:
            reward = 1.0      
    
    return float(reward)

