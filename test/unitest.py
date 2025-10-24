import pytest
from package.hello import Hello
from package.goodbye import Goodbye

# 这个文件存放单元测试类，而且必须写在这个文件里面


class HelloTest:
    # 这个类是示例，大家把它替换成自己写的类就行。测试类名必须是**Test，测试方法名必须是test_**，如果不想类或方法被pytest运行就明明成其他不符合格式的名字就行
    # 这个装饰器是用来给name这个参数输入样例的
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
    # 这是第二个测试类，往下还可以有第三、第四个测试类。
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
