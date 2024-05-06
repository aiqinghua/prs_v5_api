from utils.remove_file_util import remove_file



if __name__ == '__main__':
    # 每次执行前删除日志文件
    remove_file("/logs")
    remove_file("/temp")
    remove_file("/report")