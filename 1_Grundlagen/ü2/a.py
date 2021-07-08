import cv2
import numpy as np

''' Öffnen einer Kamera und Initialisierung von Variablen '''
file = 'C:\\Users\\Fabian\\Desktop\\miku.mp4'
cap = cv2.VideoCapture(file)
mode = "LUMINANZ"  # CHROMINANZ, LUMINANZ
window_name = "Ergebnis mit %s" % mode

''' Auslesen, Modifizieren und Ausgeben von Bildern'''
while True:
    ret, frame = cap.read()
    if not ret:
        cap.release()
        cap = cv2.VideoCapture(file)
        ret, frame = cap.read()

    if mode == "CHROMINANZ":
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
        frame[:, :, 0] = 255 / 2
        frame = cv2.cvtColor(frame, cv2.COLOR_YCrCb2BGR)
    elif mode == "LUMINANZ":
        frame_0, frame_1 = frame.copy(), frame.copy()
        # weighted
        frame_0[:, :, :] = frame @ np.array([[0.114, 0.587, 0.299]]).T

        # average
        frame_1[:, :, :] = np.mean(frame, axis=-1, keepdims=True)

        w = frame.shape[1] // 2
        c = 300
        frame = np.concatenate([frame_0[:, w - c:w + c], frame_1[:, w - c:w + c]], axis=1)
    else:
        raise Exception("FALSCHER MODE!!!")

    cv2.imshow(window_name, frame)
    # cv2.waitKey(0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

''' Fenster schließen, nachdem q gedrückt wurde '''
cap.release()
cv2.destroyAllWindows()
