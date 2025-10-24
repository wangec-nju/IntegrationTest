# NOVA Test Framwork
这是为了NOVA的协作项目开发的测试框架
## 文件架构
- src/ 存储源代码
- test/ 存储测试文件
- hooks/ 存储写好的Git Hooks，具体使用方法见hooks/README.md
- resources/ 存储资源文件
- .github/ 存储Github Actions配置文件
- .vscode/ 存储VSC的配置文件
- pytest.ini pytest的配置文件，尽量不要修改
- requriements.txt 记录依赖的文件
## 怎么写样例JSON文件
样例JSON文件的最大的结构一定是一个列表结构，其中存储了多个对象结构，每个结构有method（代表HTTP请求方法）、request（代表请求体）、response（代表期望的返回体）
具体的例子请看 resources/cases.json