import pyautogui as ag
import time

while True:
   
    for i in range(4):
        
        print("Ciclo = ", i)

        ag.alert('Confirme para iniciar sua sessão de pomodoro.\n25 minutos de foco')
        time.sleep(1)
   
        if i < 3:
            ag.alert('Confirme para inciar sua sessão de desacanso.\n5 minutos de intervalo')
            time.sleep(1)
        else:
            ag.alert('Confirme para inciar sua sessão de desacanso extendido.\n15 minutos de intervalo')
            time.sleep(1)
            

'''
focused word: 25 min
brek: 5 min

every 4 pomodoros, take 15-30 break
'''