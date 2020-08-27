import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title='Please Drink Water',
            message=" Drink eight 8-ounce glasses of water a day. That's easy to remember, and it's a reasonable goal.",
            app_icon="icon.ico",
            timeout=2,
        )
        time.sleep(6)