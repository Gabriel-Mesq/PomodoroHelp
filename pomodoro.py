from pyautogui import alert
import PySimpleGUI as sg
import winsound
import time

sg.theme('Black')

layout = [[sg.Text('Pomodoro Timer:')],
          [sg.Text('', size=(8, 2), font=('Helvetica', 20),
                justification='center', key='text')],
          [sg.Exit(button_color=('white', 'firebrick4'), key='Exit')]]

window = sg.Window('Running Timer', layout,
                   no_titlebar=True,
                   auto_size_buttons=False,
                   keep_on_top=True,
                   grab_anywhere=True,
                   element_padding=(0, 0),
                   finalize=True,
                   element_justification='c')

def Pomodoro(time_sec):
    while time_sec > -1:
        
        event, values = window.read(timeout=10)
        mins, secs = divmod(time_sec, 60)
        current_time = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        time_sec -= 1

        if event in (sg.WIN_CLOSED, 'Exit'):      
            exit() 

        window['text'].update(current_time)
                                                                                            
while True:
   
    for i in range(4):
        
        winsound.Beep(500, 1000)
        alert('Confirme para iniciar sua sessão de pomodoro.\n25 minutos de foco')
        Pomodoro(25*60)
   
        if i < 3:
            winsound.Beep(500, 1000)
            alert('Confirme para inciar sua sessão de desacanso.\n5 minutos de intervalo')
            Pomodoro(5*60)
        else:
            winsound.Beep(500, 1000)
            alert('Confirme para inciar sua sessão de desacanso extendido.\n15 minutos de intervalo')
            Pomodoro(15*60)
            
            
'''
focused word: 25 min
brek: 5 min

every 4 pomodoros, take 15-30 break
'''
