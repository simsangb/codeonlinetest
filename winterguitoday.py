import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits import mplot3d
from scipy.stats import zscore
import torch
import torch.nn as nn
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import webbrowser
# from IPython import display 


df1= round(pd.read_excel("heatgs.xlsm", 'Data Normalize', skiprows=17 ,na_values=['NA','?'] ),3)
med1 = df1['temper'].median()
df1['temper'] = df1['temper'].fillna(med1)

val_list = df1['temper'].values.tolist()
# print(val_list2[0])



def create_plot(year, unemployment_rate):
    plt.plot(year, unemployment_rate, color='red', marker='o')
    plt.title('Heat Guess', fontsize=14)
    plt.xlabel('Hour', fontsize=14)
    plt.ylabel('Gcal/Hr', fontsize=14)
    plt.grid(True)
    return plt.gcf()
urls = {
    '기상청 바로가기':'https://www.weather.go.kr/w/weather/forecast/short-term.do'
  
}

items = sorted(urls.keys())


sg.theme('Darkblue6')
layout = [[sg.Text('선택 →'),sg.Radio('평일','dday', key ='-normalday-',default=True),sg.Radio('휴일','dday', key='-holiday-')],
          [sg.Text('시간',size=(16,1),font='gothic',text_color='white'),sg.Text('00',size=(3,1),font='gothic',text_color='white'),sg.Text('01',size=(3,1),font='gothic',text_color='white'),sg.Text('02',size=(3,1),font='gothic',text_color='white'),sg.Text('03',size=(3,1),font='gothic',text_color='white'),sg.Text('04',size=(3,1),font='gothic',text_color='white'),sg.Text('05',size=(3,1),font='gothic',text_color='white'),sg.Text('06',size=(3,1),font='gothic',text_color='white'),sg.Text('07',size=(3,1),font='gothic',text_color='white'),sg.Text('08',size=(3,1),font='gothic',text_color='white'),sg.Text('09',size=(3,1),font='gothic',text_color='white'),sg.Text('10',size=(3,1),font='gothic',text_color='white'),sg.Text('11',size=(3,1),font='gothic',text_color='white'),sg.Text('12',size=(3,1),font='gothic',text_color='white'),sg.Text('13',size=(3,1),font='gothic',text_color='white'),sg.Text('14',size=(3,1),font='gothic',text_color='white'),sg.Text('15',size=(3,1),font='gothic',text_color='white'),sg.Text('16',size=(3,1),font='gothic',text_color='white'),sg.Text('17',size=(3,1),font='gothic',text_color='white'),sg.Text('18',size=(3,1),font='gothic',text_color='white'),sg.Text('19',size=(3,1),font='gothic',text_color='white'),sg.Text('20',size=(3,1),font='gothic',text_color='white'),sg.Text('21',size=(3,1),font='gothic',text_color='white'),sg.Text('22',size=(3,1),font='gothic',text_color='white'),sg.Text('23',size=(3,1),font='gothic',text_color='white')],
          [sg.Text('예상 온도(입력)',size=(16,1),font='gothic',text_color='white'),sg.InputText(size=(3,1),font='gothic',background_color='white',default_text=val_list[0],text_color='black',key='-in0-'),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in1-',default_text=val_list[1]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in2-',default_text=val_list[2]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in3-',default_text=val_list[3]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in4-',default_text=val_list[4]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in5-',default_text=val_list[5]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in6-',default_text=val_list[6]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in7-',default_text=val_list[7]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in8-',default_text=val_list[8]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in9-',default_text=val_list[9]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in10-',default_text=val_list[10]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in11-',default_text=val_list[11]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in12-',default_text=val_list[12]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in13-',default_text=val_list[13]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in14-',default_text=val_list[14]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in15-',default_text=val_list[15]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in16-',default_text=val_list[16]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in17-',default_text=val_list[17]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in18-',default_text=val_list[18]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in19-',default_text=val_list[19]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in20-',default_text=val_list[20]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in21-',default_text=val_list[21]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in22-',default_text=val_list[22]),sg.InputText(size=(3,1),font='gothic',background_color='white',text_color='black',key='-in23-',default_text=val_list[23])],
          [sg.Text('예상 공급량',size=(16,1),font='gothic',text_color='white'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te0-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te1-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te2-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te3-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te4-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te5-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te6-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te7-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te8-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te9-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te10-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te11-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te12-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te13-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te14-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te15-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te16-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te17-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te18-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te19-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te20-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te21-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te22-'),sg.Text(size=(3,1),font='gothic',background_color='yellow',text_color='black',key='-te23-')],
          [sg.Button('ok',bind_return_key=True),sg.Button('cancel')],
          [sg.Text('예상 총 공급량',text_color='yellow'),sg.Text(size=(6, 1), key='-LIST-')],
          [sg.Canvas(size=(460, 460), key='-CANVAS-')],
          [[sg.Text(txt, tooltip=urls[txt], enable_events=True,  key=f'URL {urls[txt]}')] for txt in items]]

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg
window = sg.Window('겨울철 예상 열공급량(평일 : 최근 2년 2500개, 휴일 : 최근 3년간 1700개 시간data),winternomal.pt와 winterholiday.pt도 필요, graph.png와 heatgusee.txt 파일 생성됨',layout)

# def _clear():
#     for item in canvas.get_tk_widget().find_all():
#        canvas.get_tk_widget().delete(item)

# print("{:,}".format(int((int(values['-in-'])*3.024/5)*1000/60)))
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

while True:
    event, values =window.read() 
    if event == 'cancel' or event==sg.WIN_CLOSED:
        break
    
    if values['-normalday-'] == True:

        new_model = MLPModel() # Model을 생성해줍니다.
        new_model.load_state_dict(torch.load('winternormal.pt'))
        new_model.eval()
    if values['-holiday-'] == True:

        new_model = MLPModel() # Model을 생성해줍니다.
        new_model.load_state_dict(torch.load('winterholiday.pt'))
        new_model.eval()
    
    if event.startswith("URL "):
        url = event.split(' ')[1]
        webbrowser.open(url)


    if event == 'ok':
        # window['-LIST-'].update(str("{:,}".format((float(values['-in-'])/3600*4/3.141519/float(values['_in2_'])/float(values['_in2_'])))))
        ttlist2=[]
        ttlist2.append(float(values['-in0-']))
        ttlist2.append(float(values['-in1-']))
        ttlist2.append(float(values['-in2-']))
        ttlist2.append(float(values['-in3-']))
        ttlist2.append(float(values['-in4-']))
        ttlist2.append(float(values['-in5-']))
        ttlist2.append(float(values['-in6-']))
        ttlist2.append(float(values['-in7-']))
        ttlist2.append(float(values['-in8-']))
        ttlist2.append(float(values['-in9-']))
        ttlist2.append(float(values['-in10-']))
        ttlist2.append(float(values['-in11-']))
        ttlist2.append(float(values['-in12-']))
        ttlist2.append(float(values['-in13-']))
        ttlist2.append(float(values['-in14-']))
        ttlist2.append(float(values['-in15-']))
        ttlist2.append(float(values['-in16-']))
        ttlist2.append(float(values['-in17-']))
        ttlist2.append(float(values['-in18-']))
        ttlist2.append(float(values['-in19-']))
        ttlist2.append(float(values['-in20-']))
        ttlist2.append(float(values['-in21-']))
        ttlist2.append(float(values['-in22-']))
        ttlist2.append(float(values['-in23-']))

        # print(ttlist2)
        if values['-normalday-'] == True:
            ttlist1 = [-0.884222251,-0.75559504,-0.626967829,-0.498340618,-0.369713408,-0.241086197,-0.112458986,0.016168225,0.144795436,0.273422646,0.402049857,0.530677068,0.659304279,0.78793149,0.9165587,1.045185911,1.173813122,1.302440333,1.431067544,1.559694754,1.688321965,1.816949176,1.945576387,2.074203597]
        if values['-holiday-'] == True:
            ttlist1 = [-0.600210243,-0.455220185,-0.310230126,-0.165240067,-0.020250008,0.124740051,0.269730109,0.414720168,0.559710227,0.704700286,0.849690345,0.994680403,1.139670462,1.284660521,1.42965058,1.574640639,1.719630697,1.864620756,2.009610815,2.154600874,2.299590932,2.444580991,2.58957105,2.734561109]
 
        # ttlist2 = [-11,-12,-12,-13,-13,-13,-13,-14,-14,-13,-12,-11,-10,-9,-8,-8,-7,-8,-9,-9,-9,-9,-10,-10]
        testX = np.array([ttlist1, ttlist2]).T
        input_Ttt = torch.Tensor(testX)
        pred_test = new_model(input_Ttt)
        arrattest = pred_test.detach().numpy()

        print("예상공급총량 : ",arrattest.sum())
        window['-LIST-'].update(str(int(arrattest.sum())))
        myt00=arrattest[0:1,:].tolist()
        myt01=arrattest[1:2,:].tolist()
        myt02=arrattest[2:3,:].tolist()
        myt03=arrattest[3:4,:].tolist()
        myt04=arrattest[4:5,:].tolist()
        myt05=arrattest[5:6,:].tolist()
        myt06=arrattest[6:7,:].tolist()
        myt07=arrattest[7:8,:].tolist()
        myt08=arrattest[8:9,:].tolist()
        myt09=arrattest[9:10,:].tolist()
        myt10=arrattest[10:11,:].tolist()
        myt11=arrattest[11:12,:].tolist()
        myt12=arrattest[12:13,:].tolist()
        myt13=arrattest[13:14,:].tolist()
        myt14=arrattest[14:15,:].tolist()
        myt15=arrattest[15:16,:].tolist()
        myt16=arrattest[16:17,:].tolist()
        myt17=arrattest[17:18,:].tolist()
        myt18=arrattest[18:19,:].tolist()
        myt19=arrattest[19:20,:].tolist()
        myt20=arrattest[20:21,:].tolist()
        myt21=arrattest[21:22,:].tolist()
        myt22=arrattest[22:23,:].tolist()
        myt23=arrattest[23:24,:].tolist()

        ysupply = []
        ysupply=myt00+myt01+myt02+myt03+myt04+myt05+myt06+myt07+myt08+myt09+myt10+myt11+myt12+myt13+myt14+myt15+myt16+myt17+myt18+myt19+myt20+myt21+myt22+myt23        

        myt00 =str(myt00)
        myt01 =str(myt01)
        myt02 =str(myt02)
        myt03 =str(myt03)
        myt04 =str(myt04)
        myt05 =str(myt05)
        myt06 =str(myt06)
        myt07 =str(myt07)
        myt08 =str(myt08)
        myt09 =str(myt09)
        myt10 =str(myt10)
        myt11 =str(myt11)
        myt12 =str(myt12)
        myt13 =str(myt13)
        myt14 =str(myt14)
        myt15 =str(myt15)
        myt16 =str(myt16)
        myt17 =str(myt17)
        myt18 =str(myt18)
        myt19 =str(myt19)
        myt20 =str(myt20)
        myt21 =str(myt21)
        myt22 =str(myt22)
        myt23 =str(myt23)

        myt00=myt00.replace("[","").replace("]","")
        myt01=myt01.replace("[","").replace("]","")
        myt02=myt02.replace("[","").replace("]","")
        myt03=myt03.replace("[","").replace("]","")
        myt04=myt04.replace("[","").replace("]","")
        myt05=myt05.replace("[","").replace("]","")
        myt06=myt06.replace("[","").replace("]","")
        myt07=myt07.replace("[","").replace("]","")
        myt08=myt08.replace("[","").replace("]","")
        myt09=myt09.replace("[","").replace("]","")
        myt10=myt10.replace("[","").replace("]","")
        myt11=myt11.replace("[","").replace("]","")
        myt12=myt12.replace("[","").replace("]","")
        myt13=myt13.replace("[","").replace("]","")
        myt14=myt14.replace("[","").replace("]","")
        myt15=myt15.replace("[","").replace("]","")
        myt16=myt16.replace("[","").replace("]","")
        myt17=myt17.replace("[","").replace("]","")
        myt18=myt18.replace("[","").replace("]","")
        myt19=myt19.replace("[","").replace("]","")
        myt20=myt20.replace("[","").replace("]","")
        myt21=myt21.replace("[","").replace("]","")
        myt22=myt22.replace("[","").replace("]","")
        myt23=myt23.replace("[","").replace("]","")

        
        window['-te0-'].update(int(float(myt00)))
        window['-te1-'].update(int(float(myt01)))
        window['-te2-'].update(int(float(myt02)))
        window['-te3-'].update(int(float(myt03)))
        window['-te4-'].update(int(float(myt04)))
        window['-te5-'].update(int(float(myt05)))
        window['-te6-'].update(int(float(myt06)))
        window['-te7-'].update(int(float(myt07)))
        window['-te8-'].update(int(float(myt08)))
        window['-te9-'].update(int(float(myt09)))
        window['-te10-'].update(int(float(myt10)))
        window['-te11-'].update(int(float(myt11)))
        window['-te12-'].update(int(float(myt12)))
        window['-te13-'].update(int(float(myt13)))
        window['-te14-'].update(int(float(myt14)))
        window['-te15-'].update(int(float(myt15)))
        window['-te16-'].update(int(float(myt16)))
        window['-te17-'].update(int(float(myt17)))
        window['-te18-'].update(int(float(myt18)))
        window['-te19-'].update(int(float(myt19)))
        window['-te20-'].update(int(float(myt20)))
        window['-te21-'].update(int(float(myt21)))
        window['-te22-'].update(int(float(myt22)))
        window['-te23-'].update(int(float(myt23)))
        xtemp = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
        heatguest=[]
        heatguest=myt00[0:3]+"\n"+myt01[0:3]+"\n"+myt02[0:3]+"\n"+myt03[0:3]+"\n"+myt04[0:3]+"\n"+myt05[0:3]+"\n"+myt06[0:3]+"\n"+myt07[0:3]+"\n"+myt08[0:3]+"\n"+myt09[0:3]+"\n"+myt10[0:3]+"\n"+myt11[0:3]+"\n"+myt12[0:3]+"\n"+myt13[0:3]+"\n"+myt14[0:3]+"\n"+myt15[0:3]+"\n"+myt16[0:3]+"\n"+myt17[0:3]+"\n"+myt18[0:3]+"\n"+myt19[0:3]+"\n"+myt20[0:3]+"\n"+myt21[0:3]+"\n"+myt22[0:3]+"\n"+myt23[0:3]+"\n"
  
        # draw_figure(window['-CANVAS-'].TKCanvas, display.clear_output(wait=True))
        
        window['-CANVAS-'].TKCanvas.delete("all")# draw_figure(window['-CANVAS-'].TKCanvas, _clear())
        draw_figure(window['-CANVAS-'].TKCanvas, create_plot(xtemp, ysupply))
        image_file = 'graph.png'
        # txt_file = "text1.txt"
        print(heatguest)
        # with   open(txt_file, 'w')   as file:
        #    for name in heatguest:
        #         file.write(name+'\n')
        file_name = 'heatguess.txt'

        with open(file_name, 'w+') as file:
           file.write(''.join(heatguest)) 


        plt.savefig(image_file, dpi = 400)  
window.close()