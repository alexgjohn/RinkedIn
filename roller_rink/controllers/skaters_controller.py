from flask import Flask, render_template, request, redirect, flash
from flask import Blueprint
from models.skater import Skater
from models.lesson import Lesson
from models.level import Level
import repositories.lesson_repository as lesson_repo
import repositories.skater_repository as skater_repo
import repositories.level_repository as level_repo

skaters_blueprint = Blueprint("skaters", __name__)


@skaters_blueprint.route('/skaters')
def skaters():
    skaters = skater_repo.select_all()
    premium_skaters = skater_repo.get_premium_skaters()
    return render_template('skaters/index.jinja', skaters = skaters, premium_skaters = premium_skaters, title = "Meet Our Skaters!")

@skaters_blueprint.route('/skaters/<id>', methods = ['GET'])
def show(id):
    skater = skater_repo.select(id)
    lessons_for_skater = lesson_repo.get_lessons_for_skater(skater)
    title = skater.full_name
    return render_template('skaters/show.jinja', skater = skater, lessons_for_skater = lessons_for_skater, title = title)

@skaters_blueprint.route('/skaters/new', methods = ['GET'])
def new_skater():
    return render_template('skaters/new.jinja', title = "Register a New Skater")


@skaters_blueprint.route('/skaters', methods = ['POST'])
def add_skater():
    full_name = request.form['full_name']
    premium_member = request.form['premium_member']
    skater = Skater(full_name, premium_member)
    skater_repo.save(skater)
    return redirect('/skaters')

@skaters_blueprint.route('/skaters/<id>/edit', methods = ['GET'])
def edit_skater(id):
    skater = skater_repo.select(id)
    return render_template('skaters/edit.jinja', skater = skater, title = "Update Skater Details")


@skaters_blueprint.route('/skaters/<id>', methods = ['POST'])
def update_skater(id):
    full_name = request.form['full_name']
    premium_member = request.form['premium_member']
    skater = Skater(full_name, premium_member, id)
    skater_repo.update(skater)
    return redirect('/skaters')

@skaters_blueprint.route('/skaters/<id>/book', methods = ['GET'])
def book_skater_to_lesson(id):
    skater = skater_repo.select(id)
    all_lessons = lesson_repo.select_all()
    not_premium_lessons = lesson_repo.get_lessons_not_premium()
    return render_template('skaters/book.jinja', skater = skater, all_lessons = all_lessons, not_premium_lessons = not_premium_lessons, title = "Add this skater to a lesson!")


@skaters_blueprint.route('/skaters/<id>/book', methods = ['POST'])
def add_level_for_skater(id):
    lesson_id = request.form['lesson_id']
    skater_id = request.form['skater_id']
    skater = skater_repo.select(skater_id)
    lesson = lesson_repo.select(lesson_id)
    level_reached = request.form['level']
    level = Level(skater, lesson, level_reached)
    result = level_repo.check_for_duplicate(level)
    if result == True:
        flash("This skater is already booked to this lesson")
        return redirect('/skaters/<id>')
    else:
        level_repo.save(level)
        return redirect('/skaters/<id>')