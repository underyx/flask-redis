from flask_redis import client as uut


def test_constructor_app(mocker):
    """Test that the constructor passes the app to FlaskRedis.init_app"""
    mocker.patch.object(uut.FlaskRedis, "init_app", autospec=True)
    app_stub = mocker.stub(name="app_stub")

    uut.FlaskRedis(app_stub)

    uut.FlaskRedis.init_app.assert_called_once_with(mocker.ANY, app_stub)
