
def create_app():
    from flask import Flask

    app = Flask(__name__)
    
    from app.core.blueprints.routes.route import main
    
    app.register_blueprint(main)
    
    return app
    
__all__ = [
    'create_app'
]