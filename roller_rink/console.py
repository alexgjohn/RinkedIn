import pdb
from models.skater import Skater
from models.lesson import Lesson
from models.level import Level
import repositories.skater_repository as skater_repo
import repositories.lesson_repository as lesson_repo
import repositories.level_repository as level_repo

level_repo.delete_all()
skater_repo.delete_all()
lesson_repo.delete_all()

skater1 = Skater("Wheels Smith", True)
skater_repo.save(skater1)
skater2 = Skater("Skate Beckingsale", False)
skater_repo.save(skater2)
skater3 = Skater("Reece Wheeliespoons", True)
skater_repo.save(skater3)

lesson1 = Lesson("Speed Skating", "Monday", 10, False)
lesson_repo.save(lesson1)
lesson2 = Lesson("Artistic Skating", "Wednesday", 12, False)
lesson_repo.save(lesson2)
lesson3 = Lesson("Wheelie Cool Disco Dancing", "Saturday", 8, True)
lesson_repo.save(lesson3)

level1 = Level(skater1, lesson3, "Beginner")
level_repo.save(level1)
level2 = Level(skater2, lesson2, "Intermediate")
level_repo.save(level2)
level3 = Level(skater3, lesson2, "Advanced")
level_repo.save(level3)
level4 = Level(skater1, lesson1, "Beginner")
level_repo.save(level4)

lesson1 = Lesson("Ice Skating", "Monday", 10, False)
lesson_repo.update(lesson1)

results = lesson_repo.get_lessons_not_premium()
for result in results:
    print(result.name)




