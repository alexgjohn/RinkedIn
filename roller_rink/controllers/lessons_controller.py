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
    skaters = skater_repo.select_all()
    spaces = lesson.capacity - lesson.skater_count
    return render_template('lessons/show.jinja', lesson = lesson, skaters = skaters, spaces = spaces, title = lesson.name)

# route for new lesson - get 

# route for create lesson - post
    
# route for change lesson - post 

# route for update lesson - post
    
# route for delete lesson - post - NOT MVP
