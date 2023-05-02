from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.lesson import Lesson
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
    return render_template('lessons/show.jinja', lesson = lesson, skaters_in_lesson = skaters_in_lesson, title = lesson.name, skater_count = skater_count)

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
    return render_template('home.jinja')


@lessons_blueprint.route('/lessons/<id>/book', methods=['GET'])
def book_skater_to_lesson(id):
    lesson = lesson_repo.select(id)
    skaters = skater_repo.select_all()
    premium_skaters = skater_repo.get_premium_skaters()
    return render_template('lessons/book.jinja', title = "Add a skater to this lesson!", lesson = lesson, skaters = skaters, premium_skaters = premium_skaters)

