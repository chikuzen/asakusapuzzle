#!/usr/bin/env python3

import sys
import time
import win32gui as w32g
import win32con as w32c
import pyautogui as pag

keys_list = [
    None,
    'aaaaassdwwssawdssaaaaa',
    'aaaawaswwaasdddssaaasawdwaaaaadwaa',
    'aaasaassawdwasawdwaasawwwwaaasss',
    'waaadssawawwssaawsddsswwaasaaaaw',
    'awawdddwwadwddsawddssdwaassawsawdssawdssaaaasdwaassdddsd',
    'aaawwaawasxdddssawdwaawaasdsddssaaddwwasdwwwaawassxsaaaa',
    'waaaasssaassaawwwwwdddsaawasssswwddsawddsssaaaxaaaaw',
    'waaawasddwwwwdddsaawassaaawaaasddwdsaaaawwwdssasdddddddassawdwaaadddsssddwasawdwaasawwwwxwwdwssaaaaassssdwwwawdddsdwwddwaxaaaw',
    'dwwwwwwaaaaawddddssawdsssssaaaawwssddddwwwaaaadwwasssswdsaxasssa',
    'wwwwwwwdddsaawassssssssxdwsdddwwawaawdddddwwaaaaaasssssasdwdsxawwwwwwwwaaaasdddwdssssssssdsaxwwwaaasawwdddddwasaaawwwdsasddddsssddddwwawwaassssasdxawwwwwssddddwaaaawwdddddsawassswdsaawassssdsaaaxaaaaa',
    'ssssawdwwwaassddwwwaaaaaassssddwddddwwwaassddwwwaassddwwaaaxdssadddwwasdsaaaddwwasdwwwaaassswwwaassdwwddsawdddsssaasaaaxaa',
    'sdddddsssaaaaaawdddsddddwwwwaaaawassswdddddsssaaaaaaawdsddddddssawdwaaadddwwasswwwaaaaassdddaaaassdwdddwasddddssawdwaaddwwasssdsaxaaa',
    'awwwwasaassdwawddwdsaaaaawddsddddssssaasaawwwwssssddwddwwwwaaaawasdddddssawdwaaaawaasdwdssssssdsaxaasdwdddwwddsaaaaassawxwwwaaaaa',
    'ddssasssddddwasaaawwawwwddddsaawasssssdsssawdwaxaaaaaawdddddsdwwwawwwwdssssssassddddxawwdddddssaaaaaaaawwasssxssssawaaawdddsdwwwwwawdddddddsdwwxddwwwwassssssdsaaawwaassssxssdddsddwaaasawwwwwdwwaaassawwwwawwwddsaaaxaaaawwdsasdddddwdsssssssssasddwdssddsaxaaa',
    'assaaasdwwaawdwwassddsdddsawwddwasawsssaawdssaaaaaaaaaaawaaasdddddddddddddsdwwwddwaaaaaxddssasdddddwwwwwwasssswwwwwaaaaaaaaaaaawaaasddddddddddddwdsssssddsaaaaaaxddwwdwddssssdsssawwwdwaaaaaaaaaxaaaaaddwwaasaa',
    'aasasssaaswaassdawwasddddwwwdsaawwaaaassaasawawaawwwa',
    'dddddssssassddwwwwwwdddwwddssaaadddwwaassddwwaasaassssswwwwwddwddssdsssaawaawwwwddwddssdsssaasawaaadwwwwaassssswaassdsddwaaaaxaaa',
    'sawawwwdddssawdssaasssaswdwwwaasdwaassasddsddwdssaasss',
    'dddddddxassdssswwwawwdddssssxsddssaawwwsaaawwwwssssasaawwddawwddsssasdwdsxawwwdsssddddssaawsddwwaawwaaawwawdddwdssssssssxsswwwwwwaaasaaasaawwddawwwddsawddddssssaawwwssaawwwddddddwdsssssssssssssxwwaawwwwddwwwaaasassaaassdwsssaaawwdassdwawddassddwwawddddaaaawwwdwddddwddsssaasssssswwddsssaaxwwwwwaaaaasaawwwwdwwassssssdssaawdsdwawddassddwwawddddaaaawwwdwddddwddsssaasssssswwddsssaaaaaaxaaa',
    'sssxwwaasdwaawadssssaassasdxwwaaawwwwddsawddssdsssssddddwwwwwwaawaaassdwssssssddddwwwwwwaasadwddssssssaaaawwwwwawwdddswaasssssaaawwwwddsdssssassdddddwwwwwwaawawassssswwwwddssdwaasssasaaadddwdwwwwaaaaassssxddssdwawaawwwwdddddssssasaaadddwdwwwwaaaaasssssxwddddwdwwadssaawssssddddwwwaaadwwwwaaassdssdsaaaddwwwawwaasdwaassssssxwwdddssddwdsdwwssaaaawwwddwwwddsawddssdsaaaadddwwwaawaaassdssdsaaaddwwwawwaasdwaasssssssxwwwddddwdddwwwaasaaswawwdswddsddwaaawassssswwwwddddssssaaasaaadddwdwwwwaaaaasdwaassssssssxssaaaa',
]

def prepare(hwnd):
    w32g.SetWindowPos(hwnd, w32c.HWND_TOPMOST, 0, 0, 0, 0,
                      w32c.SWP_NOMOVE | w32c.SWP_NOSIZE)
    l, t, r, b = w32g.GetWindowRect(hwnd)
    pag.moveTo(l+60, t+10)
    pag.click()

def proc(stage, info=True):
    keys = ['enter'] * 15 + list(keys_list[stage])
    if info:
        print(f'ステージ{stage}を処理中...', file=sys.stderr)
    for k in keys:
        time.sleep(0.05)
        pag.press(k)

def proc_all(info=True):
    for s in range(20):
        time.sleep(1)
        proc(s+1, info)

def finish(hwnd):
    w32g.SetWindowPos(hwnd, w32c.HWND_NOTOPMOST, 0, 0, 0, 0,
                      w32c.SWP_NOMOVE | w32c.SWP_NOSIZE)

def help(msg='引数に0から20までの整数を指定して実行してください。'):
    print(msg, file=sys.stderr)
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    if not sys.argv[1].isdigit():
        help()
    stage = int(sys.argv[1])
    if stage < 0 or stage > 20:
        help()
    hwnd = w32g.FindWindow(None, '真・女神転生Ⅲ NOCTURNE HD REMASTER')
    if hwnd == 0:
        help('真・女神転生Ⅲ NOCTURNE HD REMASTERが起動されていません')

    prepare(hwnd)

    if stage == 0:
        proc_all()
    else:
        proc(stage)

    finish(hwnd)

    sys.exit(0)
