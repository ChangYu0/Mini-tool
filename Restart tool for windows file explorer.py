import os
import sys

def restart_explorer():
    # 關閉 Windows 檔案總管
    os.system("taskkill /f /im explorer.exe")

    # 重新啟動 Windows 檔案總管
    os.system("start explorer.exe")

def main():
    # 重新啟動 Windows 檔案總管
    restart_explorer()

    # 顯示選項
    print("重新啟動 Windows 檔案總管成功 Restarting Windows File Explorer successfully。")
    print("請選擇 Please select：")
    print("1. 再次執行 Execute again")
    print("2. 退出 Exit")

    # 讀取使用者輸入
    choice = input()

    # 根據使用者輸入執行動作
    if choice == "1":
        main()
    elif choice == "2":
        sys.exit()
    else:
        print("請輸入有效的選項。")

if __name__ == "__main__":
    main()
