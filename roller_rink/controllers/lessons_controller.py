from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.lesson import Lesson
from models.skater import Skater
from models.level import Level
import repositories.lesson_repository as lesson_repo
import repositories.skater_repository as skater_repo
import repositories.level_repository as level_repo

lessons_blueprint = Blueprint("lessons", __name__)


@lessons_blueprint.route('/lessons')
def lessons():
    lessons = lesson_repo.get_lessons_in_day_order()
    return render_template('lessons/index.jinja', lessons = lessons, title = "Our Upcoming Lessons!")

# route for lesson - get 
@lessons_blueprint.route('/lessons/<id>')
def show(id):
    lesson = lesson_repo.select(id)
    skaters_in_lesson = skater_repo.get_skaters_in_lesson(lesson)
    skater_count = len(skaters_in_lesson)
    spaces_in_lesson = lesson.capacity - skater_count
    return render_template('lessons/show.jinja', lesson = lesson, skaters_in_lesson = skaters_in_lesson, title = lesson.name, skater_count = skater_count, spaces_in_lesson = spaces_in_lesson)

# route for new lesson - get 
@lessons_blueprint.route('/lessons/new', methods = ['GET'])
def new_lesson():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return render_template('lessons/new.jinja', title = "Create a New Lesson", days = days)

# route for create lesson - post
@lessons_blueprint.route('/lessons', methods = ['POST'])
def add_lesson():
    name = request.form['name']
    day = request.form['day']
    capacity = int(request.form['capacity'])
    premium = request.form['premium']
    lesson = Lesson(name, day, capacity, premium)
    lesson_repo.save(lesson)
    return redirect('/lessons')

    
    
# route for edit lesson - post 
@lessons_blueprint.route('/lessons/<id>/edit', methods = ['GET'])
def edit_lesson(id):
    lesson = lesson_repo.select(id)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return render_template('lessons/edit.jinja', lesson = lesson, days = days, title = "Update Lesson Details")



# route for update lesson - post
@lessons_blueprint.route("/lessons/<id>", methods = ['POST'])
def update_lesson(id):
    name = request.form['name']
    day = request.form['day']
    capacity = int(request.form['capacity'])
    premium = request.form['premium']
    lesson = Lesson(name, day, capacity, premium, id)
    lesson_repo.update(lesson)
    return redirect('/lessons')


    
# route for delete lesson - post - NOT MVP
@lessons_blueprint.route('/lessons/<id>/delete', methods=['POST'])
def delete_lesson(id):
    lesson_repo.delete(id)
    return redirect('/lessons')


@lessons_blueprint.route('/lessons/<id>/book', methods=['GET'])
def book_skater_to_lesson(id):
    lesson = lesson_repo.select(id)
    skaters = skater_repo.select_all()
    premium_skaters = skater_repo.get_premium_skaters()
    return render_template('lessons/book.jinja', title = "Add a skater to this lesson!", lesson = lesson, skaters = skaters, premium_skaters = premium_skaters)


@lessons_blueprint.route('/lessons/<id>/book', methods = ['POST'])
def add_level_for_lesson(id):
    lesson_id = request.form['lesson_id']
    skater_id = request.form['skater_id']
    skater = skater_repo.select(skater_id)
    lesson = lesson_repo.select(lesson_id)
    level_reached = request.form['level']
    level = Level(skater, lesson, level_reached)
    result = level_repo.check_for_duplicate(level)
    if result == True:
        return redirect('/error')
    else:
        level_repo.save(level)
        return redirect('/lessons')


