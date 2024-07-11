from PyQt5.QtWidgets import QApplication, QLabel
import pyaimp
import time

app = QApplication([])
label = QLabel('olas')
label.show()

try:
    app.exec()
    client = pyaimp.Client()

    while True:
        state = client.get_playback_state()

        if state == pyaimp.PlayBackState.Stopped:
            print('Detenido')
        elif state == pyaimp.PlayBackState.Paused:
            print('Pausado')
        elif state == pyaimp.PlayBackState.Playing:
            print('Reproduciendo')
            print(client.get_current_track_info()["title"])
            # label.text = client.get_current_track_info()["title"]
        time.sleep(1)
    print("terminado")

except RuntimeError as re: # AIMP instance not found
    print(re)
except Exception as e:
    print(e)