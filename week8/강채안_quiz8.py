class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, comletion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.comletion_year = comletion_year

    # 매물 정보
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.comletion_year)

# house = []
house1 = House('강남', '아파트', '매매', '10억', '2010년')
house1.show_detail()