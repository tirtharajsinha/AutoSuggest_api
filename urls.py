import views

# config your urls here


def add_url(app):
    app.add_url_rule("/", view_func=views.index, methods=["GET", "POST"])
    app.add_url_rule(
        "/complete/<host>", view_func=views.complete, methods=["GET", "POST"]
    )
    return app
