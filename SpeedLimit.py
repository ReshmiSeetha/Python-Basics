def SpeedLimit(speed):
    if(speed<70):
        return "OK!!!";
    elif(speed>70):
        point=(speed-70)/5;
        if(point>12):
            return "License cancelled!!!";
        else:
            return "Reduce Speed";
    else:
        return "Reduce speed";
    
