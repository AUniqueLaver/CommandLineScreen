
from User import UserApplication as UserApplication
import User.UserApplication as UserApplication

if __name__ == "__main__":
    userApplicationSettings = UserApplication.ApplicationSettings()
    # userApplicationSettings.start(240, 120)
    userApplicationSettings.start(240, 60)
    userApplication = UserApplication.UserApplication()
    userApplication.start(userApplicationSettings)
    userApplication.run()
    userApplication.onDestroy()





