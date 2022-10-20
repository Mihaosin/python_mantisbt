

def test_login(app):
    username = app.username
    password = app.password
    app.session.ensure_login(username, password)
    assert app.session.is_logged_in_as(username)
    app.session.logout()