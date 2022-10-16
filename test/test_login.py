

def test_login(app):
    app.session.login(username, password)
    assert app.session.is_logged_in_as(username)
    app.session.logout()