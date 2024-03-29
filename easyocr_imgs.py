

#pip install easyocr

#!pip install psycopg2

#pip install streamlit

import easyocr
import pandas as pd
import streamlit as st




# conn = psycopg2.connect(user = "postgres", password = "pr@thu123", host = "localhost", port = "5432", database = "prathamesh")
# conn.autocommit = True
# pk = conn.cursor()

reader = easyocr.Reader(['en'],gpu=False)

def img_upload(imgx):
  result = reader.readtext(imgx,paragraph=False)
  ext_data=[]
  for i in result:
    ext_data.append(i[1])
 

  addr = ''
  c_name = ''
  p_num = ''
  dict1 = {}
  for i in range(len(ext_data)):
    
    
    if i == 0:
      dict1['Name'] = ext_data[i]
      
      continue
    if i == 1:
      dict1["designation"] = ext_data[i]
      
      continue
    if '-' in ext_data[i]:
      p_num = ','.join([p_num,ext_data[i]])
      dict1["phone_number"] = p_num[2:]
      
      continue
    if '@' in ext_data[i]:
      dict1["email"] = ext_data[i]
      
      continue
    if 'www'  in ext_data[i]:
      dict1["website"] = ext_data[i]
      
      continue
    if 'WWW' in ext_data[i]:
      dict1['website'] = ext_data[i]
      continue
    if '-' not in ext_data[i] and "@" not in ext_data[i] and "www" not in ext_data[i] and "WWW" not in ext_data[i]:
      
      if any(char.isdigit() for char in ext_data[i]) or "," in ext_data[i] or ";" in ext_data[i]:
        addr = addr + ext_data[i]
        dict1["Address"] = addr
        continue
      else:
        c_name = ' '.join([c_name, ext_data[i]])
        dict1["Company_Name"] = c_name[0:]
      
    df = pd.DataFrame.from_dict([dict1])
  return df


#Streamlit block
def streamlit():
  st.title('BIZ_Card Data Extraction Using EasyOCR')
  st.header('Welcome to Business card data extraction by Prathamesh')
  file = st.file_uploader("Please choose an image")

  if file is not None:

    #To read file as bytes:

      bytes_data = file.getvalue()

      data = img_upload(bytes_data)
      st.write(data)
      st.image(file)
      
 
maincall = streamlit()
