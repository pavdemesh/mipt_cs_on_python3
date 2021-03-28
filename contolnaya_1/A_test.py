w_truck = int(input())
h_truck = int(input())
w_piano = int(input())
h_piano = int(input())
w_fridge = int(input())
h_fridge = int(input())
max_weight = int(input())
max_height = int(input())


def find_route():
    if (w_truck + w_piano > max_weight) or (h_truck + h_fridge > max_height):
        return "NO"

    if (w_fridge + w_piano + w_truck > max_weight) and (h_piano + h_truck > max_height):
        return "NO"

    return "YES"


print(find_route())
