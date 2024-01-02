import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits import mplot3d
import xlsxwriter
from scipy.stats import zscore
# ====== Generating Dataset ====== #
# num_data = 3600
# x1 = np.random.rand(num_data) * 10
# x2 = np.random.rand(num_data) * 10
# e = np.random.normal(0, 0.5, num_data)

df1= round(pd.read_excel("heatguess4.xlsm", 'Data Normalize', skiprows=17 ,na_values=['NA','?'] ),3)
df2= round(pd.read_excel("heatguess4.xlsm", 'data2', skiprows=17 ),3)
df3= round(pd.read_excel("heatguess4.xlsm", 'data3', skiprows=17 ),3)
df4= round(pd.read_excel("heatguess4.xlsm", 'data4', skiprows=17 ),3)
df5= round(pd.read_excel("heatguess4.xlsm", 'data5', skiprows=17 ),3)
df6= round(pd.read_excel("heatguess4.xlsm", 'data6', skiprows=17 ),3)
df7= round(pd.read_excel("heatguess4.xlsm", 'data7', skiprows=17 ),3)

# df1= round(pd.read_excel("hzhz.xlsm", 'Data Normalize', skiprows=17 ),4)
# df2= pd.read_excel("hzhz.xlsm", 'data2', skiprows=17 )
# df3= pd.read_excel("hzhz.xlsm", 'data3', skiprows=17 )
# df4= pd.read_excel("hzhz.xlsm", 'data4', skiprows=17 )
# df5= pd.read_excel("hzhz.xlsm", 'data5', skiprows=17 )
# df6= pd.read_excel("hzhz.xlsm", 'data6', skiprows=17 )
# df7= pd.read_excel("hzhz.xlsm", 'data7', skiprows=17 )
# Standardize ranges
df1['freq'] = df1['freq'].dropna()
df1['temper'] =df1['temper'].dropna()
med1 = df1['temper'].median()
df1['temper'] = df1['temper'].fillna(med1)
med11 = df1['freq'].median()
df1['freq'] = df1['freq'].fillna(med11)

df2['freq'] = df2['freq'].dropna()
df2['temper'] =df2['temper'].dropna()
med2 = df2['temper'].median()
df2['temper'] = df2['temper'].fillna(med2)
med22 = df2['freq'].median()
df2['freq'] = df2['freq'].fillna(med22)

df3['freq'] = df3['freq'].dropna()
df3['temper'] =df3['temper'].dropna()
med3 = df3['temper'].median()
df3['temper'] = df3['temper'].fillna(med3)
med33 = df3['freq'].median()
df3['freq'] = df3['freq'].fillna(med33)

df4['freq'] = df4['freq'].dropna()
df4['temper'] =df4['temper'].dropna()
med4 = df4['temper'].median()
df4['temper'] = df4['temper'].fillna(med4)
med44 = df4['freq'].median()
df4['freq'] = df4['freq'].fillna(med44)

df5['freq'] = df5['freq'].dropna()
df5['temper'] =df5['temper'].dropna()
med5 = df5['temper'].median()
df5['temper'] = df5['temper'].fillna(med5)
med55 = df5['freq'].median()
df5['freq'] = df5['freq'].fillna(med55)

df6['freq'] = df6['freq'].dropna()
df6['temper'] =df6['temper'].dropna()
med6 = df6['temper'].median()
df6['temper'] = df6['temper'].fillna(med6)
med66 = df6['freq'].median()
df6['freq'] = df6['freq'].fillna(med66)

df7['freq'] = df7['freq'].dropna()
df7['temper'] =df7['temper'].dropna()
med7 = df7['temper'].median()
df7['temper'] = df7['temper'].fillna(med7)
med77 = df7['freq'].median()
df7['freq'] = df7['freq'].fillna(med77)




print(df1['temper'])
df1['freq'] = zscore(df1['freq'])
df2['freq'] = zscore(df2['freq'])
df3['freq'] = zscore(df3['freq'])
df4['freq'] = zscore(df4['freq'])
df5['freq'] = zscore(df5['freq'])
df6['freq'] = zscore(df6['freq'])
df7['freq'] = zscore(df7['freq'])

# df1['temper'] = zscore(df1['temper'].dropna())
# df2['temper'] = zscore(df2['temper'].dropna())
# df3['temper'] = zscore(df3['temper'].dropna())
# df4['temper'] = zscore(df4['temper'].dropna())
# df5['temper'] = zscore(df5['temper'].dropna())
# df6['temper'] = zscore(df6['temper'].dropna())
# df7['temper'] = zscore(df7['temper'].dropna())

# df1['mw'] = zscore(df1['mw'].dropna())
print(df1['freq'],df2['freq'],df3['freq'],df4['freq'],df5['freq'],df6['freq'],df7['freq'])
print(df1['temper'],df2['temper'],df3['temper'],df4['temper'],df5['temper'],df6['temper'],df7['temper'])





va1_list1 = df1['freq'].values.tolist()
val_list2 = df1['temper'].values.tolist()
# print(len(va1_list1))


va1_list122 = df2['freq'].values.tolist()
val_list222 = df2['temper'].values.tolist()

va1_list133 = df3['freq'].values.tolist()
val_list233 = df3['temper'].values.tolist()

va1_list144 = df4['freq'].values.tolist()
val_list244 = df4['temper'].values.tolist()

va1_list155 = df5['freq'].values.tolist()
val_list255 = df5['temper'].values.tolist()

va1_list166 = df6['freq'].values.tolist()
val_list266 = df6['temper'].values.tolist()

va1_list177 = df7['freq'].values.tolist()
val_list277 = df7['temper'].values.tolist()



x122 = va1_list122
x222 = val_list222
x133 = va1_list133
x233 = val_list233
x144 = va1_list144
x244 = val_list244
x155 = va1_list155
x255 = val_list255
x166 = va1_list166
x266 = val_list266
x177 = va1_list177
x277 = val_list277
# x3 = val_list3



x1 = va1_list1
x2 = val_list2


# X2 = np.array([x3, x2]).T
X2 = np.array([x122, x222]).T
X3 = np.array([x133, x233]).T
X4 = np.array([x144, x244]).T
X5 = np.array([x155, x255]).T
X6 = np.array([x166, x266]).T
X7 = np.array([x177, x277]).T


X = np.array([x1, x2]).T

# y = 2*np.sin(x1) + np.log(0.5*x2**2) + e


# df1['mw'].dropna()
y =  df1['mw'].values.tolist()
# print(df1['mw'].dropna())


# ====== Split Dataset into Train, Validation, Test ======#
train_X, train_y = X[:2500, :], y[:2500]
print(train_X)
val_X, val_y = X[1000:2500, :], y[1000:2500]
test_X, test_y = X[1000:2500, :], y[1000:2500]
# mytest_X,mytest_Y = X[:5,:], y[:5]
# print(test_X)

train_X1 = X[:2580, :]
train_X2 = X2[:3600, :]
train_X3 = X3[:3600, :]
train_X4 = X4[:3600, :]
train_X5 = X5[:3600, :]
train_X6 = X6[:3600, :]
train_X7 = X7[:3600, :]




# ====== Visualize Each Dataset ====== #
fig = plt.figure(figsize=(15,13))
ax1 = fig.add_subplot(1, 1, 1, projection='3d')
ax1.scatter(train_X[:, 0], train_X[:, 1], train_y, c=train_y, cmap='jet')

ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
ax1.set_zlabel('y')
ax1.set_title('Train Set Distribution')
ax1.set_zlim(-10, 500)   #500으로 바꿈(원래6)
ax1.view_init(40, -60)
ax1.invert_xaxis()


# ax2 = fig.add_subplot(1, 3, 2, projection='3d')
# ax2.scatter(val_X[:, 0], val_X[:, 1], val_y, c=val_y, cmap='jet')

# ax2.set_xlabel('x1')
# ax2.set_ylabel('x2')
# ax2.set_zlabel('y')
# ax2.set_title('Validation Set Distribution')
# ax2.set_zlim(-10, 500)   #500으로 바꿈(원래6)
# ax2.view_init(40, -60)
# ax2.invert_xaxis()

# ax3 = fig.add_subplot(1, 3, 3, projection='3d')
# ax3.scatter(test_X[:, 0], test_X[:, 1], test_y, c=test_y, cmap='jet')

# ax3.set_xlabel('x1')
# ax3.set_ylabel('x2')
# ax3.set_zlabel('y')
# ax3.set_title('Test Set Distribution')
# ax3.set_zlim(-10, 500)  #500으로 바꿈(원래6)
# ax3.view_init(40, -60)
# ax3.invert_xaxis()

plt.show()
import torch
import torch.nn as nn


class LinearModel(nn.Module):
    def __init__(self): 
        super(LinearModel, self).__init__()
        self.linear = nn.Linear(in_features=2, out_features=1, bias=True)

    def forward(self, x):
    # 인스턴스(샘플) x가 인풋으로 들어왔을 때 모델이 예측하는 y값을 리턴합니다.
        return self.linear(x)


class MLPModel(nn.Module):
    def __init__(self): 
        super(MLPModel, self).__init__()
        self.linear1 = nn.Linear(in_features=2, out_features=50)
        self.linear2 = nn.Linear(in_features=50, out_features=25)
        self.linear3 = nn.Linear(in_features=25, out_features=1)
        self.relu = nn.ReLU()

    def forward(self, x):
    # 인스턴스(샘플) x가 인풋으로 들어왔을 때 모델이 예측하는 y값을 리턴합니다.
        x = self.linear1(x)
        x = self.relu(x)
        x = self.linear2(x)
        x = self.relu(x)
        x = self.linear3(x)

        return x

reg_loss = nn.MSELoss()
import torch.optim as optim
from sklearn.metrics import mean_absolute_error


# ====== Construct Model ====== #
# model = LinearModel()
# print(model.linear.weight)
# print(model.linear.bias)

model = MLPModel() # Model을 생성해줍니다.
print('{} parameters'.format(sum(p.numel() for p in model.parameters() if p.requires_grad))) # 복잡해보이지만 간단히 모델 내에 학습을 당할 파라미터 수를 카운팅하는 코드입니다.

# ===== Construct Optimizer ====== #
lr = 0.00002 # Learning Rate를 하나 정해줍니다. (원할한 학습을 위해 손을 많이 탑니다)
optimizer = optim.SGD(model.parameters(), lr=lr) # Optimizer를 생성해줍니다.

# 매 학습 단계에서의 epoch값과 그 때의 loss 값을 저장할 리스트를 만들어줍시다.
list_epoch = [] 
list_train_loss = []
list_val_loss = []
list_mae = []
list_mae_epoch = []


epoch = 200000 # 학습 횟수(epoch)을 지정해줍시다.
for i in range(epoch):

    # ====== Train ====== #
    model.train() # model을 train 모드로 세팅합니다. 반대로 향후 모델을 평가할 때는 eval() 모드로 변경할 겁니다 (나중 실습에서 쓸 겁니다)
    optimizer.zero_grad() # optimizer에 남아있을 수도 있는 잔여 그라디언트를 0으로 다 초기화해줍니다.

    input_x = torch.Tensor(train_X)
    true_y = torch.Tensor(train_y)
    pred_y = model(input_x)
    #print(input_x.shape, true_y.shape, pred_y.shape) # 각 인풋과 아웃풋의 차원을 체크해봅니다.

    loss = reg_loss(pred_y.squeeze(), true_y)
    loss.backward() # backward()를 통해서 그라디언트를 구해줍니다.
    optimizer.step() # step()을 통해서 그라디언틀르 바탕으로 파라미터를 업데이트 해줍니다. 
    list_epoch.append(i)
    list_train_loss.append(loss.detach().numpy())


    # ====== Validation ====== #
    model.eval()
    optimizer.zero_grad()
    input_x = torch.Tensor(val_X)
    true_y = torch.Tensor(val_y)
    pred_y = model(input_x)   
    loss = reg_loss(pred_y.squeeze(), true_y)
    list_val_loss.append(loss.detach().numpy())
  

    # ====== Evaluation ======= #
    if i % 60000 == 0: # 2000회의 학습마다 실제 데이터 분포와 모델이 예측한 분포를 그려봅니다.

        # ====== Calculate MAE ====== #
        model.eval()
        optimizer.zero_grad()
        input_x = torch.Tensor(test_X)
        true_y = torch.Tensor(test_y)
        pred_y = model(input_x).detach().numpy() 
        mae = mean_absolute_error(true_y, pred_y) # sklearn 쪽 함수들은 true_y 가 먼저, pred_y가 나중에 인자로 들어가는 것에 주의합시다
        list_mae.append(mae)
        list_mae_epoch.append(i)
        

        # mypred = model(input_x)
        # #--------------
        # print(true_y,mypred)
        # print(true_y,pred_y)

        fig = plt.figure(figsize=(15,5))

        # ====== True Y Scattering ====== #
        ax1 = fig.add_subplot(1, 3, 1, projection='3d')
        ax1.scatter(test_X[:, 0], test_X[:, 1], test_y, c=test_y, cmap='jet')

        ax1.set_xlabel('x1')
        ax1.set_ylabel('x2')
        ax1.set_zlabel('y')
        ax1.set_zlim(-10, 500)
        ax1.view_init(40, -40)
        ax1.set_title('True test y')
        ax1.invert_xaxis()

        # ====== Predicted Y Scattering ====== #
        ax2 = fig.add_subplot(1, 3, 2, projection='3d')
        ax2.scatter(test_X[:, 0], test_X[:, 1], pred_y, c=pred_y[:,0], cmap='jet')

        ax2.set_xlabel('x1')
        ax2.set_ylabel('x2')
        ax2.set_zlabel('y')
        ax2.set_zlim(-10, 500)
        ax2.view_init(40, -40)
        ax2.set_title('Predicted test y')
        ax2.invert_xaxis()

        # ====== Just for Visualizaing with High Resolution ====== #
        input_x = torch.Tensor(train_X)
        pred_y = model(input_x).detach().numpy() 


 
        #print(pred_y)

        ax3 = fig.add_subplot(1, 3, 3, projection='3d')
        ax3.scatter(train_X[:, 0], train_X[:, 1], pred_y, c=pred_y[:,0], cmap='jet')

        # print(train_X[:, 0], train_X[:, 1], pred_y,)
        

        ax3.set_xlabel('x1')
        ax3.set_ylabel('x2')
        ax3.set_zlabel('y')
        ax3.set_zlim(-10, 500)
        ax3.view_init(40, -40)
        ax3.set_title('Predicted train y')
        ax3.invert_xaxis()

        plt.show()
        print(i, loss)

fig = plt.figure(figsize=(15,5))

# ====== Loss Fluctuation ====== #
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(list_epoch, list_train_loss, label='train_loss')
ax1.plot(list_epoch, list_val_loss, '--', label='val_loss')
ax1.set_xlabel('epoch')
ax1.set_ylabel('loss')
ax1.set_ylim(0, 5)
ax1.grid()
ax1.legend()
ax1.set_title('epoch vs loss')

# ====== Metric Fluctuation ====== #
ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(list_mae_epoch, list_mae, marker='x', label='mae metric')

ax2.set_xlabel('epoch')
ax2.set_ylabel('mae')
ax2.grid()
ax2.legend()
ax2.set_title('epoch vs mae')


plt.show()   

torch.save(model.state_dict(),'winternormal.pt')
#-----------------------------------------
ttlist1 = [-0.884222251,-0.75559504,-0.626967829,-0.498340618,-0.369713408,-0.241086197,-0.112458986,0.016168225,0.144795436,0.273422646,0.402049857,0.530677068,0.659304279,0.78793149,0.9165587,1.045185911,1.173813122,1.302440333,1.431067544,1.559694754,1.688321965,1.816949176,1.945576387,2.074203597]
ttlist2 = [-10,-11,-11,-12,-12,-13,-13,-13,-13,-13,-12,-11,-10,-9,-8,-8,-7,-8,-9,-9,-9,-10,-10,-11]
testX = np.array([ttlist1, ttlist2]).T
input_Ttt = torch.Tensor(testX)
pred_test = model(input_Ttt)
arrattest = pred_test.detach().numpy()
print(arrattest)
#--------------------------------------------------




# for jj in range(2,7):
input_my1 = torch.Tensor(train_X1)
input_my2 = torch.Tensor(train_X2)
input_my3 = torch.Tensor(train_X3)
input_my4 = torch.Tensor(train_X4)
input_my5 = torch.Tensor(train_X5)
input_my6 = torch.Tensor(train_X6)
input_my7 = torch.Tensor(train_X7)



pred_mymy1 = model(input_my1)
pred_mymy2 = model(input_my2)
pred_mymy3 = model(input_my3)
pred_mymy4 = model(input_my4)
pred_mymy5 = model(input_my5)  
pred_mymy6 = model(input_my6)
pred_mymy7 = model(input_my7)


array1 = pred_mymy1.detach().numpy()
array2 = pred_mymy2.detach().numpy()
array3 = pred_mymy3.detach().numpy()
array4 = pred_mymy4.detach().numpy()
array5 = pred_mymy5.detach().numpy()
array6 = pred_mymy6.detach().numpy()
array7 = pred_mymy7.detach().numpy()


df11 = pd.DataFrame(array1)
df22 = pd.DataFrame(array2)
df33 = pd.DataFrame(array3)
df44 = pd.DataFrame(array4)
df55 = pd.DataFrame(array5)
df66 = pd.DataFrame(array6)
df77 = pd.DataFrame(array7)


excel_file2 = '2023년12월19일.xlsx'
# excel_file3 = '2023년6월3일.xlsx'


excel_writer = pd.ExcelWriter(excel_file2, engine='xlsxwriter')

df11.to_excel(excel_writer, index=False, sheet_name= 'Sheet1',startcol=0)
df22.to_excel(excel_writer, index=False, sheet_name= 'Sheet1',startcol=1)
df33.to_excel(excel_writer, index=False, sheet_name= 'Sheet1',startcol=2)
df44.to_excel(excel_writer, index=False, sheet_name= 'Sheet1',startcol=3)
df55.to_excel(excel_writer, index=False, sheet_name= 'Sheet1',startcol=4)
df66.to_excel(excel_writer, index=False, sheet_name= 'Sheet1',startcol=5)
df77.to_excel(excel_writer, index=False, sheet_name= 'Sheet1',startcol=6)
df1.to_excel(excel_writer, index=False, sheet_name= 'Sheet1',startcol=8)

excel_writer.save()