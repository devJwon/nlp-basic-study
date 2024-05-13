

class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = House("Gangnam", "Apartment", "for sale", "100.000", "year: 2010")
house2 = House("Mapo-Gu", "Studio", "전세", "50.000", "year: 2007")
house3 = House("Songpa-Gu", "House", "Monthly Rent", "5000 deposit/500 rent", "year: 2000")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("total {0} info.".format(len(houses)))
for house in houses:
    house.show_detail()