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

lesson1 = Lesson("Speed Skating", "Monday", 10, False)
lesson_repo.save(lesson1)
lesson2 = Lesson("Artistic Skating", "Wednesday", 12, False)
lesson_repo.save(lesson2)

level1 = Level(skater1, lesson1, "Beginner")
level_repo.save(level1)
level2 = Level(skater2, lesson1, "Intermediate")
level_repo.save(level2)

