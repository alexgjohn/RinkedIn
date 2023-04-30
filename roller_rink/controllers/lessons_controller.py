from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.lesson import Lesson
import repositories.lesson_repository as lesson_repo
import repositories.skater_repository as skater_repo
import repositories.level_repository as level_repo

lessons_blueprint = Blueprint("lessons", __name__)

# route for lessons - get 
@lessons_blueprint.route('/lessons')
def lessons():
    lessons = lesson_repo.select_all()
    return render_template('lessons/index.jinja', lessons = lessons)

# route for lesson - get 

# route for new lesson - get 

# route for create lesson - post
    
# route for change lesson - post 

# route for update lesson - post
    
# route for delete lesson - post - NOT MVP
