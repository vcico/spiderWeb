#!/usr/bin/python
# -*- coding:utf-8 -*-

import os  
 

class Config:
    """
    配置项
        爬虫节点数据传递格式 可用的选项 json 、 xml(暂不可用)
        data_struct = json
    """

    config_file = 'setting.conf'



    config_handle = {

    }
    
    array_delimiter = '|'

    def __init__(self):
        if not os.path.isfile("%s/%s" % (os.path.dirname(__file__),self.config_file)):
            raise Exception('configure file is not exist')
        self.config = {}

    def getConfig(self):
        f = open("%s/%s" % (os.path.dirname(__file__),self.config_file),'r')
        for line in f.readlines():
            data=line.strip()
            if len(data) != 0:
                if data[0] == '#':
                    continue
                key,value = data.split('=')
                self.config[key.strip()] = value.strip()
        return self.convConfig()
        
    def convConfig(self):
        for handle_str,fields in self.config_handle.iteritems():
            handle = getattr(self,'%sHandle' % handle_str)
            for field in fields:
                try:
                    self.config[field] = handle(field)
                except KeyError,e:
                    raise Exception("Missing configuration items: %s " % field)
        return self.config
            
    def arrayHandle(self,field):
        return self.config[field].split(self.array_delimiter)

    def integerHandle(self,field):
        try:
            result = int(self.config[field])
        except ValueError,e:
            raise Exception("Configuration format error: %s Must be number " % field)
        return result

configure = Config().getConfig()

if __name__ == '__main__':
    pass