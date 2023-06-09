from Face_and_Landmark_Detection.ExtractionUtil import ExtractionUtil
import cv2
import numpy as np
#import Emotion_Classification.Classification_Prediction as c
import Analyser.Suggestion as s

vid = cv2.VideoCapture(0)

extractionUtil = ExtractionUtil()


while True:
    ret, image = vid.read()

    imageBW = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret, rect = extractionUtil.getFaceRect(imageBW)

    if (ret == 0):
        cv2.rectangle(image, extractionUtil.getFlattenedRectangleFromDLibRectangle(rect), (255, 0, 0), 10)
    else:
        print("no face detected")
    
    cv2.resize(image, (640, 480))
    cv2.imshow("window", image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    #print("running program")
  
vid.release()
cv2.destroyAllWindows()
"""

image = cv2.imread("example.jpg")
print("starting")

imageBW = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#faceDetection = FaceDetection()
detectionUtil = DetectionUtil()

ret, rect = detectionUtil.getFaceRect(imageBW)

if ret == -1:
    print("No face detected")
else:
    print("face detected")

cv2.rectangle(image, detectionUtil.getFlattenedRectangleFromDLibRectangle(rect), (0, 0, 255), 10)

landmarks = detectionUtil.get_landmarks(imageBW, rect)

print("landmark shape is : ")
print(np.shape(landmarks))

detectionUtil.draw_shape_points(image, landmarks)

print("normalizing landmarks")
landmarks_norm = detectionUtil.normalizelandmarks(image, landmarks)
landmarks_norm = np.reshape(landmarks_norm, (136))

# Get Emotion
Emotion =  c.predict_emotions(landmarks_norm)

# Suggestion By Analyser
suggest = s.get_suggestion(Emotion)
print(suggest)


print(landmarks_norm)

image = cv2.resize(image, (600, 600))
cv2.imshow("window", image)

cv2.waitKey(0)
    
cv2.destroyAllWindows()"""