from db.run_sql import run_sql
from models.skater import Skater
from models.lesson import Lesson
from models.level import Level


def save(skater):
    sql = "INSERT INTO skaters (full_name, premium_member) VALUES (%s, %s) RETURNING *"
    values = skater.full_name, skater.premium_member
    results = run_sql(sql, values)
    id = results[0]['id']
    skater.id = id
    return skater

def select_all():
    skaters = []
    sql = "SELECT * FROM skaters"
    results = run_sql(sql)
    for row in results:
        skater = Skater(row['full_name'], row['premium_member'], row['id'])
        skaters.append(skater)
    return skaters

def select(id):
    skater = None
    sql = "SELECT * FROM skaters WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        skater = Skater(result['full_name'], result['premium_member'], result['id'])
    return skater


def delete_all():
    sql = "DELETE FROM skaters"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM skaters WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(skater):
    sql = "UPDATE skaters SET (full_name, premium_member) = (%s, %s) WHERE id = %s"
    values = [skater.full_name, skater.premium_member, skater.id]
    run_sql(sql, values)

def get_premium_skaters():
    skaters = select_all()
    premium_skaters = []
    for skater in skaters:
        if skater.premium_member:
            premium_skaters.append(skater)
    return premium_skaters

# to be added

# get skaters in lesson

# get skater by level? would need both lesson AND level as parameters. ambitious. 

