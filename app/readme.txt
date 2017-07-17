该目录下都是一些比较实用的小程序。

smalltool/automount.py: 用来在mac电脑上自动加载NTFS格式移动硬盘，解决只读不可写问题。但是好像有bug。
smalltool/modifier.py: 主要用来自动修改混乱的N集电视剧文件名。需要输入文件夹的绝对路径，然后再输入电视剧的名字，最后确定输入音频格式。
12306: 主要用来实现火车票的终端查询功能。使用12306 -dg 南京 上海 2017-07-07指令运行。
    12306/drawstation.py:  用来获取各个站台中文对应编码重新定向为文件stations.py。
    12306/stations.py:  生成的站台编码文件，需要import主程序中进行使用。
    12306/tickets.py:  是主程序，获取数据并进行查询显示。
    12306/setup.py:  打包工具，在终端下直接运行python setup.py install进行安装。
oa: 主要用来实现加班申请功能。
    oa/oa.py:  是主程序。
    oa/setup.py:  打包工具。
doxygen/doxygen.py:  实现C语言函数声明和定义的自动单文件批量注释。
     		     Ubuntu14.04以上的一般都有python3.5，直接运行即可。如果是Ubuntu12.04请查看Python版本，安装python3.5才可以运行。
    		     一般使用方式：将doxygen.py放到xxxxxxxx/profile目录下，使用find ./ -name '*.c' | xargs ./doxygen.py或./doxygen.py <单文件相对路径>
    		     未包含的处理有：（1）分行写的函数定义或者声明
                                    （2）函数参数不符合一般规则，会有异常打印信息提示
fly/shootfly.py:  
