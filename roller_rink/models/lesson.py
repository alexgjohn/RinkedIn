class Lesson:

    def __init__(self, name, day, capacity, premium, skater_count = 0, id = None):
        self.name = name
        self.day = day
        self.capacity = capacity
        self.premium = premium
        self.skater_count = skater_count
        self.id = id


    def increase_skater_count(self):
        self.skater_count += 1

    def lesson_has_space(self):
        return self.capacity > self.skater_count
        
        