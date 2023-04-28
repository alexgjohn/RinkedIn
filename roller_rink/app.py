from flask import Flask, render_template
# from controllers.skaters_controller import skaters_blueprint
# from controllers.lessons_controller import lessons_blueprint
# from controllers.levels_controller import levels_blueprint
app = Flask(__name__)

# app.register_blueprint(skaters_blueprint)
# app.register_blueprint(lessons_blueprint)
# app.register_blueprint(levels_bleuprint)

@app.route('/')
def home():
    return render_template('index.jinja')

if __name__ == '__main__':
    app.run(debug=True)