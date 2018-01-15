#coding=utf-8
import  logging,os,time

# log_path=os.path.dirname(os.getcwd())+"/log"
# logging.basicConfig(filename='%s/one.log'% log_path,level=logging.DEBUG,format='%(asctime)s%(message)s', datefmt='%Y/%m/%d %I:%M:%S %p')
# logging.warning('is when this event was logged.')
class Logger(object):
    def __init__(self):
        # 第一步，创建一个logger
        self.logger =logging.getLogger()
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            # 第二步，创建一个handler，用于写入日志文件
            log_path="F:\hf/log/%s.log"%time.strftime('%Y-%m-%d',time.localtime(time.time()))#os.path.dirname(os.getcwd())+
            rz=logging.FileHandler(log_path, mode='a', encoding=None, delay=False)
            rz.setLevel(logging.INFO)
            # 第三步，再创建一个handler，用于输出到控制台
            sy=logging.StreamHandler()
            sy.setLevel(logging.INFO)
            # 第四步，定义handler的输出格式
            formatter=logging.Formatter('%(asctime)s %(levelname)s 函数名：%(funcName)s 操作:%(message)s','%Y/%m/%d %H:%M:%S')
            rz.setFormatter(formatter)
            sy.setFormatter(formatter)
            # 第五步，将logger添加到handler里面
            self.logger.addHandler(rz)
            self.logger.addHandler(sy)
    def get_loger(self):
        return self.logger
