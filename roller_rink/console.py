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
