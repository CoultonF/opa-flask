class TestOpa():
    def test_opa(self, test_client):
        from casbin_flask import Casbin
        from flask import Flask

        app = Flask(__name__)