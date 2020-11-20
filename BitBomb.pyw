from tkinter import *
import tkinter.messagebox as tmsg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import keyboard
import time

# launching browser and opening whatsapp web
driver = webdriver.Chrome('./chromedriver')
driver.get("http://web.whatsapp.com")
driver.maximize_window()
driver.find_element_by_name('rememberMe').click()

#launching UI
root = Tk()

#window background color
root.configure(bg='white')

root.title("BitBomb")

root.minsize(300, 300) 
root.maxsize(300, 300)

photo = PhotoImage(file = "win_icon.png")
root.iconphoto(False, photo)

# Launch button function
def launch():
    try:
        launch_button["state"] = DISABLED
        launch_button.update()

        target = target_val.get()
        msg = msg_val.get()
        count = count_val.get()
        
        #confirmation prompt
        MsgBox = tmsg.askquestion ('Confirmation prompt', f'confirm {count} shots to the target: {target.upper()}.', icon = 'warning')
        if MsgBox == 'yes':
            pass
        else:
            launch_button.update()
            launch_button["state"] = NORMAL
            return None

        search = driver.find_element_by_xpath("//*[@data-tab='3']")
        search.click()
        search.send_keys(target)
        time.sleep(2)
        search.send_keys(Keys.ENTER)
    
        text_msg = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

        for i in range(count):
            text_msg.send_keys(msg)
            driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button/span").click()

            if keyboard.is_pressed('q'):
                break

        # output window
        tmsg.showinfo("Messages sent", "Task completed successfully.")
        launch_button.update()
        launch_button["state"] = NORMAL

    except:
        pass

# destroy button function
def destroy():
    driver.quit()
    root.destroy()


# UI lebels
head = Label(root, text="BitBomb" , bg='#00BFA5', fg='white', padx=90, pady=0, font=("cosmicsansms", 20 , 'bold'))
head.grid(row=0, column=0, columnspan=2)

# insttuction label
msg_label = Label(text="Please scan and login first.", bg='#00BFA5', fg='white', padx=40, pady=2, font=("cosmicsansms", 10, 'bold'))
msg_label.grid(row=1, column=0, columnspan=2, padx=0, pady=5)

# entries label
target_label = Label(text="Target",bg='white', padx=10, pady=10, font=("cosmicsansms", 10))
target_label.grid(row=2, column=0)

msg_label = Label(text="Message", bg='white', padx=10, pady=10, font=("cosmicsansms", 10))
msg_label.grid(row=3, column=0)

count_label = Label(text="Count", bg='white', padx=10, pady=10, font=("cosmicsansms", 10))
count_label.grid(row=4, column=0)

# UI Entries
target_val = StringVar()
msg_val = StringVar()
count_val = IntVar()

target_entry = Entry(root, textvariable = target_val)
target_entry.grid(row=2, column=1, padx=0, pady=5)

msg_entry = Entry(root, textvariable = msg_val)
msg_entry.grid(row=3, column=1, padx=0, pady=5)

count_entry = Entry(root, textvariable = count_val)
count_entry.grid(row=4, column=1, padx=0, pady=5)

# Termination lebel
msg_label = Label(text="press 'Q' to Terminate.", bg='#00BFA5', fg='white', padx=60, pady=2, font=("cosmicsansms", 10, 'bold'))
msg_label.grid(row=5, column=0, columnspan=2)


# Launch button
launch_button = Button(text="LAUNCH", command=launch, borderwidth=3, padx=30, pady=0)
launch_button.grid(row=6, column=1, padx=10, pady=10)

# Destroy button
destroy_button = Button(text="DESTROY", command=destroy, borderwidth=3, padx=20, pady=0)
destroy_button.grid(row=6, column=0, padx=10, pady=10)
# About logo
msg_label = Label(text="Copyright, XtremaX 2020.\n Coded by- RAJAT (rajatkumar2312001@gmail.com)",bg='white', fg='black', padx=0, pady=2, font=("cosmicsansms", 8))
msg_label.grid(row=7, column=0, columnspan=2)

# UI main loop
root.mainloop()