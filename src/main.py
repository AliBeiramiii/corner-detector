import cv2 
import numpy as np
import pandas as pd

image = cv2.imread('../data/test2.png')

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray_image,maxCorners=30, qualityLevel=0.01, minDistance=20)
corners = sorted(np.int0(corners), key=lambda x:x[0][0])


for i in range(len(corners)):
    x, y = corners[i].ravel()
    cv2.circle(image,(x,y), 5, (0, 0, 255), -1)
    cv2.putText(image, str(i+1), (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
    
for i in range(len(corners)):
    x, y = corners[i].ravel()
    print(f"Corner {i}: x={x}, y={y}")


data = [[int(lst2[0][1] > lst1[0][1]) for _, lst2 in enumerate(corners)] for _, lst1 in enumerate(corners)]


df = pd.DataFrame(data)
print(df)

file_name = "boolean_matrix.xlsx"
df.to_excel(file_name, index=False)

print("Boolean matrix saved to", file_name)

cv2.imshow('Detected Corners', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
