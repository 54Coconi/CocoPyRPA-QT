"""
打包程序
"""
if __name__ == '__main__':
    from PyInstaller.__main__ import run

    x = input("是否继续打包程序[y/N]?")
    if x == "y" or x == "Y":
        # 不含 cmd 窗口
        opts = ['runMain.py', '-D', '-w', '--hidden-import=queue', '--icon=./logo.ico']
        run(opts)
    else:
        exit()
