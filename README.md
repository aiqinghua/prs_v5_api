# 接口自动化测试框架 pytest+requests+allure+yaml+excle
## 使用说明
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

