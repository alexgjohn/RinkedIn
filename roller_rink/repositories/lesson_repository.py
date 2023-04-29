from db.run_sql import run_sql
from models.skater import Skater
from models.lesson import Lesson
from models.level import Level


def save(lesson):
    sql = "INSERT INTO lessons (name, day, capacity, premium) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [lesson.name, lesson.day, lesson.capacity, lesson.premium]
    results = run_sql(sql, values)
    id = results[0]['id']
    lesson.id = id
    return lesson


def select_all():
    lessons = []
    sql = "SELECT * FROM lessons"
    results = run_sql(sql)
    for row in results:
        lesson = Lesson(row['name'], row['day'], row['capacity'], row['premium'], row['id'])
        lessons.append(lesson)
    return lessons 


def select(id):
    lesson = None
    sql = "SELECT * FROM lessons WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        lesson = Lesson(result['name'], result['day'], result['capacity'], result['premium'], result['id'])
    return lesson


def delete_all():
    sql = "DELETE FROM lessons"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM lessons WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(lesson):
    sql = "UPDATE lessons SET (name, day, capacity, premium) = (%s, %s, %s, %s) WHERE id = %s"
    values = [lesson.name, lesson.day, lesson.capacity, lesson.premium, lesson.id]
    run_sql(sql, values)