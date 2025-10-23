import pytest
from package.hello import Hello
from package.goodbye import Goodbye


class HelloTest:
    @pytest.mark.parametrize("name", ["NOVA", "NJU", "CAC"])
    def test_get_name(self, name):
        instance = Hello(name)
        assert instance.get_name() == name

    @pytest.mark.parametrize("name", ["NOVA", "NJU", "CAC"])
    def test_set_name(self, name):
        instance = Hello("NONONO")
        instance.set_name(name)
        assert instance.get_name() == name and instance.get_name() != "NONONO"

    @pytest.mark.parametrize("name", ["NOVA", "NJU", "CAC"])
    def test_say(self, name):
        instance = Hello(name)
        instance.say()


class GoodbyeTest:
    @pytest.mark.parametrize("name", ["NOVA", "NJU", "CAC"])
    def test_get_name(self, name):
        instance = Goodbye(name)
        assert instance.get_name() == name

    @pytest.mark.parametrize("name", ["NOVA", "NJU", "CAC"])
    def test_set_name(self, name):
        instance = Goodbye("NONONO")
        instance.set_name(name)
        assert instance.get_name() == name and instance.get_name() != "NONONO"

    @pytest.mark.parametrize("name", ["NOVA", "NJU", "CAC"])
    def test_say(self, name):
        instance = Goodbye(name)
        instance.say()
