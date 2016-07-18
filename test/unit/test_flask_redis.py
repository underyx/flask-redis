from flask_redis import FlaskRedis


def test_constructor_app(mocker):
    """Test that the constructor passes the app to FlaskRedis.init_app"""
    mocker.patch.object(FlaskRedis, 'init_app', autospec=True)
    app_stub = mocker.stub(name='app_stub')

    FlaskRedis(app_stub)

    FlaskRedis.init_app.assert_called_once_with(mocker.ANY, app_stub)
