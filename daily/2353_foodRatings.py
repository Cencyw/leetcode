from collections import defaultdict
from typing import List
from sortedcontainers import SortedList
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_map = {}
        self.cuisine_map = defaultdict(SortedList)
        for food, cuisine, rating in zip(foods,cuisines,ratings):
            self.food_map[food] = [cuisine,rating]
            self.cuisine_map[cuisine].add((-rating,food))
        

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine,rating = self.food_map[food]
        self.food_map[food][1] = newRating
        sl = self.cuisine_map[cuisine]
        sl.discard((-rating,food))
        sl.add((-newRating,food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_map[cuisine][0][1]

if __name__ == "__main__":
    
    order = [ "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
    food = [["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]]
    foods = food[0]
    cuisines = food[1]
    ratings = food[2]
    data = [["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
    f = FoodRatings(foods,cuisines,ratings)
    for i in range(len(order)):
        o = order[i]
        d = data[i]
        if o == "highestRated":
            print(f.highestRated(d[0]))
        elif o == "changeRating":
            print(f.changeRating(d[0],d[1]))




# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)