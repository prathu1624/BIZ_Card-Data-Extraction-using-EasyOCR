

#pip install easyocr

#!pip install psycopg2

#pip install streamlit

import easyocr
import pandas as pd
import psycopg2
import streamlit as st
import cv2
from matplotlib import pyplot as plt
from io import StringIO 


# conn = psycopg2.connect(user = "postgres", password = "pr@thu123", host = "localhost", port = "5432", database = "prathamesh")
# conn.autocommit = True
# pk = conn.cursor()

reader = easyocr.Reader(['en'],gpu=False)

def img_upload(imgx):
  result = reader.readtext(imgx,paragraph=False)
  ext_data=[]
  for i in result:
    ext_data.append(i[1])
 

  
  temp = ext_data
  dict1 = {}
  for i in range(len(ext_data)):
    temp_st = ext_data[i]
    
    if i == 0:
      dict1['Name'] = temp_st
      
      continue
    if i == 1:
      dict1["designation"] = temp_st
      
      continue
    if '-' in temp_st:
      dict1["phone number"] = temp_st
      
      continue
    if '@' in temp_st:
      dict1["email"] = temp_st
      
      continue
    if 'www'  in temp_st:
      dict1["website"] = temp_st
      
      continue
    if 'WWW' in temp_st:
      dict1['website'] = temp_st
      continue
    df = pd.DataFrame.from_dict([dict1])
  return df



def detect(imgx):
  result_1 = reader.readtext(imgx,paragraph=False)
  top_left = tuple(result_1[0][0][0])
  bottom_right = tuple(result_1[0][0][2])
  text = result_1[0][1]
  font = cv2.FONT_HERSHEY_SIMPLEX
  det_data=[]

  data=[]
  img = cv2.imread(imgx)
  spacer = 100
  for detection in result_1: 
      top_left = tuple(detection[0][0])
      bottom_right = tuple(detection[0][2])
      text = detection[1]
      img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)
      img = cv2.putText(img,text,(20,spacer), font, 0.5,(0,255,0),2,cv2.LINE_AA)
      spacer+=15
      data.append(detection)
  plt.figure(figsize=(10,10))
  plt.imshow(img)
  plt.show()
  for i in data:
    det_data.append(i[1])
  df1 = pd.DataFrame(det_data)

  return df1


#Streamlit block
def streamlit():
  st.title('BIZ_Card Data Extraction Using EasyOCR')
  st.header('Welcome to Business card data extraction by Prathamesh')
  file = st.file_uploader("Please choose a file")

  if file is not None:

    #To read file as bytes:

      bytes_data = file.getvalue()

      data = img_upload(bytes_data)
      st.write(data)
      


maincall = streamlit()
