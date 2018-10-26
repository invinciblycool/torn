import os

from torn.plugins.console import runHandler, controllerHandler, newHandler
import shutil


class TestCLI:

    # Although a better approach is to use fixtures, but since the resource to be yielded in this case is a directory
    # and should be removed only after all tests are done, therefore using class methods and manual calls.
    @classmethod
    def setup_sampleapp(cls):
        newHandler()
        os.chdir("app")
        runHandler()

    @classmethod
    def remove_sampleapp(cls):
        os.chdir(os.curdir)
        print(os.curdir)
        shutil.rmtree("app")

    def test_runHandler_when_no_app_exists(self, capsys):
        runHandler()
        out, _ = capsys.readouterr()
        assert out == "Not a torn app\n"

    # Unable to proceed on this
    # def test_runHandler_when_app_exists(self):
    #     self.setup_sampleapp()
    #
    #     self.remove_sampleapp()

    def test_controllerHandler(self):
        controllerHandler()
        assert 'NoneController' in os.listdir('.')
        controllerHandler('test')
        assert 'testController' in os.listdir('.')
        os.remove("NoneController")
        os.remove("testController")

