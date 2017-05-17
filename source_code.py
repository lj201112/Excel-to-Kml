import pandas as pd
import simplekml

df = pd.read_excel("测试.xls").fillna('')

位置集合 = []
[位置集合.append(i) for i in list(df['位置1']) if not i in 位置集合]
kml = simplekml.Kml()
doc = kml.newdocument(name = '测试位置')
fld = []
pnt = []
for i in range(len(位置集合)):
    fld.append(doc.newfolder(name = 位置集合[i]))

sharedstyle = simplekml.Style()
sharedstyle.labelstyle.scale = 0.85
sharedstyle.iconstyle.color = 'ff0000aa'
sharedstyle.iconstyle.scale = 0.7
sharedstyle.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
      

for j in range(len(df['样号'])):
    pnt.append(fld[位置集合.index(df.ix[j]['位置1'])].newpoint())
    pnt[j].name = df.ix[j]['样号']
    pnt[j].description = df.ix[j]['岩性'] + ',' + df.ix[j]['位置1'] + ',' + df.ix[j]['位置2'] + ',' + df.ix[j]['位置3'] + ',' + df.ix[j]['描述'] 
    pnt[j].coords = [(df.ix[j]['经度'], df.ix[j]['纬度'])]
    pnt[j].style = sharedstyle

kml.save('测试.kml')