import keyboard
import pygame
import sys
import json

#wav,mp3を再生するだけ
class PlaySE:
    #引数の型はすべてstr
    def __init__(self, key, path, volume):
        self.se = pygame.mixer.Sound(path)
        if volume == None:
            volume = "1.0"
        self.se.set_volume(float(volume))
        self.key = key

    def play(self):
        self.se.stop()
        self.se.play()

#ファイル名を指定してjsonを読み込む
#辞書型を返す
def loadJsonFile():
    print("\n読み込むファイル名(json形式)を入力してください。")
    print("未入力の場合、default.jsonが読み込まれます")
    path = input("")
    if path == "":
        path = "default.json"
    print("読み込みファイル:"+path+"\n")
    with open(path) as f:
        playSEMap = json.load(f)
    return playSEMap


#hotkeyから呼び出される関数
def playSEHandle(seList, no):
    seList[no].play()
    

if __name__ == "__main__":
    #se再生のための初期化
    pygame.mixer.init()
    playSEMap = loadJsonFile()
    seList = []
    #jsonからplayseオブジェクトを生成
    for key in playSEMap:
        path = playSEMap[key].get("path")
        volume = playSEMap[key].get("volume")
        print("hotkey:"+key+" 再生ファイル:"+path)
        seList.append(PlaySE(key, path, volume))

    #hotkey登録
    for i in range(len(seList)):
        keyboard.add_hotkey(seList[i].key, lambda no = i: playSEHandle(seList, no))

    print("\nshihf + escでプログラムを終了します")
    keyboard.wait("shift + esc")
    #終了処理
    keyboard.unhook_all_hotkeys()
    print("プログラムを終了します。")
    sys.exit()
