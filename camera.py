import cv2
import  cvzone

cascade =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
overlays = [cv2.imread('HeadGear_01.png', cv2.IMREAD_UNCHANGED),cv2.imread('HeadGear_02.png', cv2.IMREAD_UNCHANGED),
            cv2.imread('HeadGear_03.png', cv2.IMREAD_UNCHANGED)]
position_of_headgears = [[10,90],[10,90],[20,90]]
# width, height relative scaling factors
size_of_headgears = [[1.1,1.1],[1.1,1.1],[1.3,1.1]]
choice = 0
total_headgears = len(overlays)

class Video(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
        global choice
        choice=0
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret,frame=self.video.read()
        gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray_scale)

        if (len(faces) > 0):
            for (x, y, w, h) in faces:
                if (x >= 25 and x <= 460 and y >= 110 and y <= 370):
                    # cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)
                    overlay_resize = cv2.resize(overlays[choice], (int(w * size_of_headgears[choice][0]), int(h * size_of_headgears[choice][1])))
                    frame = cvzone.overlayPNG(frame, overlay_resize, [x - position_of_headgears[choice][0],
                                                                      y - position_of_headgears[choice][1]])
        #if cv2.waitKey(15) == ord('n'):
        #self.choice = (self.choice + 1) % total_headgears
        #if cv2.waitKey(15) == ord('q'):
            #break

        ret,jpg=cv2.imencode('.jpg',frame)
        return jpg.tobytes()
