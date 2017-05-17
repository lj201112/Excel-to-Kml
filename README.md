# Excel to Kml

## 1.介绍

​    该脚本可以将excel中的经纬度坐标生成'.kml'格式坐标数据。并且可以根据“位置1”建立文件夹自动归档。

## 2.依赖

​    该脚本使用python3.6.0编写。

​    导入pandas库操作excel数据，使用simplekml库生成'.kml'文件

    import pandas as pd
    import simplekml

## 3.使用

![](https://raw.githubusercontent.com/lj201112/Excel-to-Kml/master/1.png)

excel文件格式如上。除了经纬度之外尽量避免数字字符，否则会报错。

运行脚本后会在脚本同文件夹下生成kml文件，直接导入google earth即可

![](https://raw.githubusercontent.com/lj201112/Excel-to-Kml/master/2.png)

## 4.注意事项

###### 1.使用之前需修改文件名以及生成的文件名，将下面“测试”修改为自己文件名。
    df = pd.read_excel("测试.xls").fillna('')
    kml.save('测试.kml')
###### 2.建议阅读simplekml库的文档(http://simplekml.readthedocs.io/en/latest/)，以获取更多信息及功能。

