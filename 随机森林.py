import pandas as pd
from sklearn.ensemble import RandomForestRegressor  # 用于回归问题
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False #显示负号
import numpy as np

df=pd.read_excel(r"C:\Users\韩行风\Desktop\5.xlsx")
name=pd.get_dummies(df['试样'])
pb=df['配比']
char=df['焦油产率']
wather=df['水产率']
coke=df['焦渣产率']
Y=df[['焦油产率','水产率','焦渣产率']]
X=df[['试样','配比']]
dummy_encoded = pd.get_dummies(X['试样'], prefix='试样')
X_dropped = X.drop('试样', axis=1)
X = pd.concat([X_dropped, dummy_encoded], axis=1)

model=RandomForestRegressor(n_estimators=100,random_state=36)
model.fit(X,Y)
score=model.score(X,Y)
print(f'分数为:{score}')
print('----------------------------------------------------------------------------------')
x=pd.read_excel(r"C:\Users\韩行风\Desktop\12551.xlsx")
xz=pd.get_dummies(x,columns=['试样'])
y_pred=model.predict(xz)

cshn_wather=[]
cshn_char=[]
cshn_pew=[]

cssm_wather=[]
cssm_char=[]
cssm_pew=[]

cshs_wather=[]
cshs_char=[]
cshs_pew=[]

sdhs_wather=[]
sdhs_char=[]
sdhs_pew=[]

sdsm_wather=[]
sdsm_char=[]
sdsm_pew=[]


gahn_wather=[]
gahn_char=[]
gahn_pew=[]

ganm_wather=[]
ganm_char=[]
ganm_pew=[]

gasm_wather=[]
gasm_char=[]
gasm_pew=[]

rhhn_wather=[]
rhhn_char=[]
rhhn_pew=[]

rhsm_wather=[]
rhsm_char=[]
rhsm_pew=[]

for i in range(len(y_pred)):
    if 0<=i and i<50:
        cshn_char.append(y_pred[i][0])
        cshn_wather.append(y_pred[i][1])
        cshn_pew.append(y_pred[i][2])
    elif 50<=i and i<100:
        cssm_char.append(y_pred[i][0])
        cssm_wather.append(y_pred[i][1])
        cssm_pew.append(y_pred[i][2])
    elif 100<=i and i<150:
        cshs_char.append(y_pred[i][0])
        cshs_wather.append(y_pred[i][1])
        cshs_pew.append(y_pred[i][2])
    elif 150<=i and i<200:
        sdhs_char.append(y_pred[i][0])
        sdhs_wather.append(y_pred[i][1])
        sdhs_pew.append(y_pred[i][2])
    elif 200<=i and i<250:
        sdsm_char.append(y_pred[i][0])
        sdsm_wather.append(y_pred[i][1])
        sdsm_pew.append(y_pred[i][2])
    elif 250<=i and i<300:
        gahn_char.append(y_pred[i][0])
        gahn_wather.append(y_pred[i][1])
        gahn_pew.append(y_pred[i][2])
    elif 300<=i and i<350:
        ganm_char.append(y_pred[i][0])
        ganm_wather.append(y_pred[i][1])
        ganm_pew.append(y_pred[i][2])
    elif 350<=i and i<400:
        gasm_char.append(y_pred[i][0])
        gasm_wather.append(y_pred[i][1])
        gasm_pew.append(y_pred[i][2])
    elif 400<=i and i<450:
        rhhn_char.append(y_pred[i][0])
        rhhn_wather.append(y_pred[i][1])
        rhhn_pew.append(y_pred[i][2])
    elif 450<=i and i<500:
        rhsm_char.append(y_pred[i][0])
        rhsm_wather.append(y_pred[i][1])
        rhsm_pew.append(y_pred[i][2])

cshn_max=max(cshn_char)
cshn_max_index=cshn_char.index(cshn_max)
cssm_max=max(cssm_char)
cssm_max_index=cssm_char.index(cssm_max)
cshs_max=max(cshs_char)
cshs_max_index=cshs_char.index(cshs_max)
sdhs_max=max(sdhs_char)
sdhs_max_index=sdhs_char.index(sdhs_max)
sdsm_max=max(sdsm_char)
sdsm_max_index=sdsm_char.index(sdsm_max)
gahn_max=max(gahn_char)
gahn_max_index=gahn_char.index(gahn_max)
ganm_max=max(ganm_char)
ganm_max_index=ganm_char.index(ganm_max)
gasm_max=max(gasm_char)
gasm_max_index=gasm_char.index(gasm_max)
rhhn_max=max(rhhn_char)
rhhn_max_index=rhhn_char.index(rhhn_max)
rhsm_max=max(rhsm_char)
rhsm_max_index=rhsm_char.index(rhsm_max)

print(f'棉杆淮南煤焦油产率最大比例：{cshn_max_index},为{cshn_max}')
print(f'棉杆神木煤焦油产率最大比例：{cssm_max_index},为{cssm_max}')
print(f'棉杆黑山煤焦油产率最大比例：{cshs_max_index},为{cshs_max}')
print(f'木屑黑山煤焦油产率最大比例：{sdhs_max_index},为{sdhs_max}')
print(f'木屑神木煤焦油产率最大比例：{sdsm_max_index},为{sdsm_max}')
print(f'小球藻淮南煤焦油产率最大比例：{gahn_max_index},为{gahn_max}')
print(f'小球藻内蒙褐煤煤焦油产率最大比例：{ganm_max_index},为{ganm_max}')
print(f'小球藻神木煤焦油产率最大比例：{gasm_max_index},为{gasm_max}')
print(f'稻壳淮南煤焦油产率最大比例：{rhhn_max_index},为{rhhn_max}')
print(f'稻壳神木煤焦油产率最大比例：{rhsm_max_index},为{rhsm_max}')
print('----------------------------------------------------------------------------------')
cshn_min=min(cshn_pew)
cshn_min_index=cshn_pew.index(cshn_min)
cssm_min=min(cssm_pew)
cssm_min_index=cssm_pew.index(cssm_min)
cshs_min=min(cshs_pew)
cshs_min_index=cshs_pew.index(cshs_min)
sdhs_min=min(sdhs_pew)
sdhs_min_index=sdhs_pew.index(sdhs_min)
sdsm_min=min(sdsm_pew)
sdsm_min_index=sdsm_pew.index(sdsm_min)
gahn_min=min(gahn_pew)
gahn_min_index=gahn_pew.index(gahn_min)
ganm_min=min(ganm_pew)
ganm_min_index=ganm_pew.index(ganm_min)
gasm_min=min(gasm_pew)
gasm_min_index=gasm_pew.index(gasm_min)
rhhn_min=min(rhhn_pew)
rhhn_min_index=rhhn_pew.index(rhhn_min)
rhsm_min=min(rhsm_pew)
rhsm_min_index=rhsm_pew.index(rhsm_min)

print(f'棉杆淮南煤焦渣产率最小比例：{cshn_min_index},为{cshn_min}')
print(f'棉杆神木煤焦渣产率最小比例：{cssm_min_index},为{cssm_min}')
print(f'棉杆黑山煤焦渣产率最小比例：{cshs_min_index},为{cshs_min}')
print(f'木屑黑山煤焦渣产率最小比例：{sdhs_min_index},为{sdhs_min}')
print(f'木屑神木煤焦渣产率最小比例：{sdsm_min_index},为{sdsm_min}')
print(f'小球藻淮南煤焦渣产率最小比例：{gahn_min_index},为{gahn_min}')
print(f'小球藻内蒙褐煤煤焦渣产率最小比例：{ganm_min_index},为{ganm_min}')
print(f'小球藻神木煤焦渣产率最小比例：{gasm_min_index},为{gasm_min}')
print(f'稻壳淮南煤焦渣产率最小比例：{rhhn_min_index},为{rhhn_min}')
print(f'稻壳神木煤焦渣产率最小比例：{rhsm_min_index},为{rhsm_min}')

x=[]
for i in range(1,51):
    x.append(i*0.01)
plt.figure(figsize=(10,5))
for i in range(1,11):

    ax=plt.subplot(2,5,i)
    if i==1:
        y1=cshn_char
        y2=cshn_wather
        y3=cshn_pew
        title='棉杆/淮南煤'
    elif i==2:
        y1=cssm_char
        y2=cssm_wather
        y3=cssm_pew
        title='棉杆/神木煤'
    elif i==3:
        y1=cshs_char
        y2=cshs_wather
        y3=cshs_pew
        title='棉杆/黑山煤'
    elif i==4:
        y1=sdhs_char
        y2=sdhs_wather
        y3=sdhs_pew
        title='木屑/黑山煤'
    elif i==5:
        y1=sdsm_char
        y2=sdsm_wather
        y3=sdsm_pew
        title='木屑/神木煤'
    elif i==6:
        y1=gahn_char
        y2=gahn_wather
        y3=gahn_pew
        title='小球藻/淮南煤'
    elif i==7:
        y1=ganm_char
        y2=ganm_wather
        y3=ganm_pew
        title='小球藻/内蒙褐煤'
    elif i==8:
        y1=gasm_char
        y2=gasm_wather
        y3=gasm_pew
        title='小球藻/神木煤'
    elif i==9:
        y1=rhhn_char
        y2=rhhn_wather
        y3=rhhn_pew
        title='稻壳/淮南煤'
    elif i==10:
        y1=rhsm_char
        y2=rhsm_wather
        y3=rhsm_pew
        title='稻壳/神木煤'
    ax.plot(x,y1,label='焦油产率')
    ax.plot(x,y2,label='水产率')
    ax.plot(x,y3,label='焦渣产率')
    ax.set_title(title)
    ax.legend()
plt.tight_layout()
plt.show()
ind=['焦油产率','水产率','焦渣产率']
col=[]
for i in range(1,51):
    inder=str(i)
    inder=inder+'/'+'100'
    col.append(inder)
cshn=pd.DataFrame([cshn_char,cshn_wather,cshn_pew],columns=col,index=ind)
cssm=pd.DataFrame([cssm_char,cssm_wather,cssm_pew],index=ind,columns=col)
cshs=pd.DataFrame([cshs_char,cshs_wather,cshs_pew],index=ind,columns=col)
sdhs=pd.DataFrame([sdhs_char,sdhs_wather,sdhs_pew],index=ind,columns=col)
sdsm=pd.DataFrame([sdsm_char,sdsm_wather,sdsm_pew],index=ind,columns=col)
gahn=pd.DataFrame([gahn_char,gahn_wather,gahn_pew],index=ind,columns=col)
ganm=pd.DataFrame([ganm_char,ganm_wather,ganm_pew],index=ind,columns=col)
gasm=pd.DataFrame([gasm_char,gasm_wather,gasm_pew],index=ind,columns=col)
rhhn=pd.DataFrame([rhhn_char,rhhn_wather,rhhn_pew],index=ind,columns=col)
rhsm=pd.DataFrame([rhsm_char,rhsm_wather,rhsm_pew],index=ind,columns=col)
cl=['棉杆/淮南煤(CS/HN)','棉杆/神木煤（CS/SM)','棉杆/黑山煤(CS/HS)','木屑/黑山煤(SD/HS)',
    '木屑/神木煤(SD/SM)','小球藻/淮南煤(GA/HN)','小球藻/内蒙褐煤 (GA/NM)','小球藻/神木煤(GA/SM)','稻壳/淮南煤(RH/HN)','稻壳/神木煤(RH/SM)']

'''cshn.to_excel(r"C:\\Users\韩行风\Desktop\棉杆淮南煤(CSHN).xlsx")
cssm.to_excel(r"C:\\Users\韩行风\Desktop\棉杆神木煤（CSSM).xlsx")
cshs.to_excel(r"C:\\Users\韩行风\Desktop\棉杆黑山煤(CSHS).xlsx")
sdhs.to_excel(r"C:\\Users\韩行风\Desktop\木屑黑山煤(SDHS).xlsx")
sdsm.to_excel(r"C:\\Users\韩行风\Desktop\木屑神木煤(SDSM).xlsx")
gahn.to_excel(r"C:\\Users\韩行风\Desktop\小球藻淮南煤(GAHN).xlsx")
ganm.to_excel(r"C:\\Users\韩行风\Desktop\小球藻内蒙褐煤 (GANM).xlsx")
gasm.to_excel(r"C:\\Users\韩行风\Desktop\小球藻神木煤(GASM).xlsx")
rhhn.to_excel(r"C:\\Users\韩行风\Desktop\稻壳淮南煤(RHHN).xlsx")
rhsm.to_excel(r"C:\\Users\韩行风\Desktop\稻壳神木煤(RHSM).xlsx")'''