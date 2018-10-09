#!/usr/bin/python
# -*- coding:utf-8 -*-

# https://validatorpy.readthedocs.io/en/latest/index.html
#from formatter import getFormatter

#getFormatter()

from validator import Required, Not,Truthy,Blank,Range,Equals,In,validate

"""
Required 必须定义
Truthy() 为真  非空list  非0 非空字符
Range(1,11,inclusive=False) 范围区间  后面的 inclusive=false 指排除此区间
Pattern('\d\d%') 正则 40%
In(['a','sd','gdsg'])
Not(验证器) 验证器如：上述的In
InstanceOf(类名) 检查类对象 
SubclassOf(类名) 值(也是类名)是不是该类的子类
Length(0, maximum=5) 检查list的长度 minimum 和 maximum 两个参数 
Equals('value') 相等
嵌套验证 https://validatorpy.readthedocs.io/en/latest/index.html#nested-validations
== 根据参数 使用不同的验证器 ==
    pet = {
        "name": "whiskers",
	    "type": "cat"
	}
	cat_name_rules = {
	    "name": [In(["whiskers", "fuzzy", "tiger"])]
	}
	dog_name_rules = {
	    "name": [In(["spot", "ace", "bandit"])]
	}
	validation = {
	    "type": [
	        If(Equals("cat"), Then(cat_name_rules)),
	        If(Equals("dog"), Then(dog_name_rules))
	    ]
	}

>>> validate(validation, pet)
(True, {})
# Success!

"""

rules = {
	'foo' : [Required,Equals(123)],
	'bar': [Truthy()],
}

data = {
	'foo':123,
}

print validate(rules,data).valid
print validate(rules,data).errors

