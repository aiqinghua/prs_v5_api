# 接口自动化测试框架 python+pytest+requests+allure+log+mysql+clickhouse+yaml+excle
## 使用说明
### 安装说明
+ 首先，执行本框架之后，需要搭建好 python、jdk、 allure环境
+ 搭建python教程：http://c.biancheng.net/view/4161.html
+ 搭建jdk环境：https://www.cnblogs.com/zll-wyf/p/15095664.html
+ 安装allure：https://blog.csdn.net/m0_49225959/article/details/117194318
+ 如上环境如都搭建好，则安装本框架的所有第三方库依赖，执行如下命令：
```text
pip install -r requirements.txt
```
### 配置文件修改
+ 修改配置文件config/config.ini配置文件，将测试环境改为自己测试环境
+ 数据库连接配置在config/config.ini配置文件

### 运行测试用例
+ 执行命令：python run.py

## 目录结构
```text
prs_v5:
    ├─ cache        # 缓存文件
    ├─ config       # 配置文件
    ├─ data         # 测试数据
    ├─ logs         # 日志文件
    ├─ report       # 测试报告
    ├─ temp         # allure测试报告临时文件
    ├─ test_case    # 测试用例
    ├─ utils        # 方法封装、工具类
    ├─ conftest.py  # 测试夹具
    ├─ environment.properties   # allure环境变量
    ├─ pytest.ini    # pytest配置文件
    ├─ run.py        # 程序主入口
    └─ requirements.txt  # 依赖包     
```

