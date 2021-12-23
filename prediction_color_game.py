def find_number(color,np):
    non_index=n.array([0,1,2,3,4,5,6,7,8,9])
    np=n.concatenate([np,non_index])
    np=n.bincount(np)
    if(color=="GREEN"):
        gre={1:np[1],3:np[3],7:np[7],9:np[9]}
        return min(gre, key=gre.get)
    elif(color=="RED"):
        re={2:np[2],4:np[4],6:np[6],8:np[8]}
        return min(re, key=re.get)
    else:
        ora={0:np[0],5:np[5]}
        return min(ora, key=ora.get)
def color_getter(color):
    least_colour=[]
    deleter = min(color, key=color.get)
    least_colour.append(deleter)
    color.pop(deleter)
    deleter = min(color, key=color.get)
    least_colour.append(deleter)
    color.pop(deleter)
    return random.choice(least_colour)
def color_counter(colors):
    c=["RED","GREEN","ORANGE"]
    colors=n.concatenate([colors,c])
    red=(colors=="RED").sum()
    green=(colors=="GREEN").sum()
    orange=((colors=="ORANGE").sum())
    return red,green,orange
if __name__ == '__main__':
    import random
    import numpy as n
    colors = n.array(list(map(str,input().split())))  # INPUT FROM MULTII USER
    numbers =n.array(list(map(int,input().split()))) # INPUT FROM MULTII USER
    print(len(colors))
    print(len(numbers))
    red,green,orange=(color_counter(colors))
    color = {"RED": red, "GREEN": green, "ORANGE": orange}
    final_color=(color_getter(color))
    final_number=find_number(final_color,numbers)
    print(final_color,final_number)
