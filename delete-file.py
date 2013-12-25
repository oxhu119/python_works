# -*-coding:utf-8-*-
#20131225 made by oxhu119
# 这个脚本是为了定时删除导入成功的fsn文件
import sys
import os
import datetime
import ConfigParser

code_type = sys.getfilesystemencoding()
now_time=datetime.date.today()
day_r=0

def rof_run(filepath):
    if os.path.isdir(filepath):
        for root,dirs,files in os.walk(filepath):
            for subfiles in files:
                rof_run(os.path.join(root,subfiles))
    else:
        if now_time-datetime.date.fromtimestamp(os.stat(filepath).st_ctime)  > datetime.timedelta(days=day_r):
            try:
                os.remove(filepath)
                f=open('dflog.txt','a')
                print >>f,datetime.datetime.now(),":   ",filepath
                f.close()
                print filepath
            except:
                result_output('文件删除错误退出')
                sys.exit(1)
            #print filepath
            

def result_output(output):
    f=open('dflog.txt','a')
    print >>f,datetime.datetime.now(),":   ",output.decode('UTF-8').encode(code_type)
    f.close()
              
def main():
    config = ConfigParser.ConfigParser()
    config.readfp(open("delete-file.ini","r"))
    filepath = config.get("info","Path")
    global day_r 
    day_r=int(config.get("info","days"))
    
    if not os.path.isdir(filepath) and not os.path.isfile(filepath):
        result_output('路径参数错误！')
        sys.exit(1)
    
    try:
        if day_r < 1:
            raise TimeError()
    except:
        result_output('时间参数错误!')
        sys.exit(1)                  
    rof_run(filepath)    
    
if __name__ == '__main__':
    main()
