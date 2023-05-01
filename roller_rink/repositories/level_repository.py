from db.run_sql import run_sql
from models.skater import Skater
from models.lesson import Lesson
from models.level import Level
import repositories.skater_repository as skater_repo
import repositories.lesson_repository as lesson_repo


# def save(level):
#     sql = "INSERT INTO levels (skater_id, lesson_id, level_reached) VALUES (%s, %s, %s) RETURNING id"
#     values = [level.skater.id, level.lesson.id, level.level_reached]
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     level.id = id
#     return level

#possible update to above to incorporate skater_count/capacity
def save(level):
    sql = "INSERT INTO levels (skater_id, lesson_id, level_reached) VALUES (%s, %s, %s) RETURNING id"
    values = [level.skater.id, level.lesson.id, level.level_reached]
    results = run_sql(sql, values)
    id = results[0]['id']
    level.id = id
    lesson_repo.update(level.lesson)
    return level


def select_all():
    levels = []
    sql = "SELECT * FROM levels"
    results = run_sql(sql)
    for row in results:
        skater = skater_repo.select(row['skater_id'])
        lesson = lesson_repo.select(row['lesson_id'])
        level = Level(skater, lesson, row['level_reached'], row['id'])
        levels.append(level)
    return levels


def select(id):
    level = None
    sql = "SELECT * FROM levels WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        skater = skater_repo.select(result['skater_id'])
        lesson = lesson_repo.select(result['lesson_id'])
        level = Level(skater, lesson, result['level_reached'], result['id'])
    return level


def delete_all():
    sql = "DELETE from levels"
    run_sql(sql)


def delete(id):
    sql = "DELETE from levels WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# bit confused about this one, so I might save it until Monday. Can't currently see the use for it either.
def update(level):
    sql = "UPDATE levels SET (level_reached) = (%s) WHERE id = %s"
    values = [level.level_reached, level.id]
    run_sql(sql, values)

# would also be useful to have:
    # get levels for lesson
    # get levels for skater