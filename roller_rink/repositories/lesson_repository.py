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

def get_lessons_by_day(day):
    lessons = select_all()
    lessons_by_day = []
    for lesson in lessons:
        if lesson.day == day:
            lessons_by_day.append(lesson)
    return lessons_by_day

def get_lessons_in_day_order():
    lessons_in_day_order = []
    monday = get_lessons_by_day("Monday")
    tuesday = get_lessons_by_day("Tuesday")
    wednesday = get_lessons_by_day("Wednesday")
    thursday = get_lessons_by_day("Thursday")
    friday = get_lessons_by_day("Friday")
    saturday = get_lessons_by_day("Saturday")
    sunday = get_lessons_by_day("Sunday")
    lessons_in_day_order.extend(monday)
    lessons_in_day_order.extend(tuesday)
    lessons_in_day_order.extend(wednesday)
    lessons_in_day_order.extend(thursday)
    lessons_in_day_order.extend(friday)
    lessons_in_day_order.extend(saturday)
    lessons_in_day_order.extend(sunday)
    return lessons_in_day_order

def get_lessons_for_skater(skater):
    lessons_for_skater = []
    sql = "SELECT lessons.* FROM lessons INNER JOIN levels ON levels.lesson_id = lessons.id WHERE skater_id = %s"
    values = [skater.id]
    results = run_sql(sql, values)
    for row in results:
        lesson = Lesson(row['name'], row['day'], row['capacity'], row['premium'])
        lessons_for_skater.append(lesson)
    return lessons_for_skater

