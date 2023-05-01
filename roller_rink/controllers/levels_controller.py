from flask import Flask, render_template, request, redirect, flash
from flask import Blueprint
from models.skater import Skater
from models.lesson import Lesson
from models.level import Level
import repositories.lesson_repository as lesson_repo
import repositories.skater_repository as skater_repo
import repositories.level_repository as level_repo

levels_blueprint = Blueprint("levels", __name__)

@levels_blueprint.route('/levels')
def levels():
    skaters = skater_repo.select_all()
    lessons = lesson_repo.select_all()
    levels = level_repo.select_all()
    return render_template('levels/index.jinja', title = "Our Skaters' Bookings and Levels", skaters = skaters, lessons = lessons, levels = levels)

@levels_blueprint.route('/levels/new')
def new_level():
    skaters = skater_repo.select_all()
    lessons = lesson_repo.select_all()
    return render_template('levels/new.jinja', skaters = skaters, lessons = lessons, title = "Add a registered skater to one of our lessons!")


@levels_blueprint.route('/levels', methods = ['POST'])
def add_level():
    skater_id = request.form['skater_id']
    lesson_id = request.form['lesson_id']
    skater = skater_repo.select(skater_id)
    lesson = lesson_repo.select(lesson_id)
    level_reached = request.form['level']
    level = Level(skater, lesson, level_reached)
    result = level_repo.check_for_duplicate(level)
    if result == True:
        flash("This skater is already booked to this lesson")
        return redirect('/levels')
    else:
        level_repo.save(level)
        return redirect('/levels')
# check if works, then tackle issue of double booking someone


