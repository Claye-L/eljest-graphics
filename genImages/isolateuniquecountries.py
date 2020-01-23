from shutil import copyfile
import os
basepath = os.getcwd() 

fileCountries = {"dk":"0","se":"5","tr":"11","sk":"12","ee":"13"
,"nl":"14","us":"15","ca":"18","bg":"24","au":'25','no':'26','nz':'29'
,'fr':'30','gb':'34','ua':'35','ru':'37','ba':'46','lv':'48','br':'49'
,'fi':'50','it':'58','ar':'59','rs':'60','jo':'68','pl':'69','kz':'75'
,'mt':'83','cn':'100','hk':'103','kr':'104','unknown':'114','my':'119','be':'120'
,'de':'125','sk':'126','me':'127','lt':'133','cz':'194','za':'200','sg':'250'
,'id':'254','co':'280','gt':'282','mx':'287','by':'290'}

for countryname,filename in fileCountries.items():
    copyfile(basepath +'\\country_sources\\'+filename+'.png',basepath +'\\countries\\'+countryname+'.png')
