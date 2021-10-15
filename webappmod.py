import streamlit as st
import cv2
from PIL import Image
import numpy as np


disfraz = cv2.CascadeClassifier('dataSet\cascade.xml')

rec=cv2.face.LBPHFaceRecognizer_create()

def detect_faces(our_image):
    
    img = np.array(our_image.convert('RGB'))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    df1 = disfraz.detectMultiScale(gray, scaleFactor=7,minNeighbors=91,minSize=(70,78))
    # Draw rectangle around the faces
    name='Desconocido'
    for (x, y, w, h) in df1:
        # To draw a rectangle in a face
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, 'Marimonda', (x, y-10), 2, 0.7, (0, 255, 0),2, cv2.LINE_AA)
        cv2.imshow('img',img)
        print(id)

    return img

def main():
    """Disfraz Recognition App"""

    st.title("SENA BOOTCAMP 2021 EQUIPO 1 SALON 8")

    html_temp = """
    <body style="background-color:black;">
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">IA RECOGNIZER OPENCV WITH STREAMLITE</h2>
    <h4 style="color:white;text-aling:left;">Grupo conformado por: </h4>
    <h4 style="color:white;text-aling:left;">1. Benjamin Guardo - Ficha: 2340502</h4>
    <h4 style="color:white;text-aling:left;">2. Carlos Alvarez - Ficha: 2340502</h4>
    <h4 style="color:white;text-aling:left;">3. Daniel Almanza - Ficha: 2397136</h4>
    <h4 style="color:white;text-aling:left;">4. Isajar Mendoza - Ficha: 2397136</h4>
    <h4 style="color:white;text-aling:left;">5. Lilia Almanza - Instructora CEDAGRO</h4>
    <h4 style="color:white;text-aling:left;">6. Luis Perez - Ficha: 2348209</h4>
    <h4 style="color:white;text-aling:left;">7. Sebastian Castiblanco - Ficha: 2397137</h4>
    <h4 style="color:white;text-aling:left;">8. Johny Núñez - Ficha: 2397137 </h4>
    <h4 style="color:white;text-aling:left;">9. Roiman Herrera - Ficha: 2397137</h4>
    <h4 style="color:white;text-aling:left;">10. Reinaldo Valencia - Ficha: 2357645</h4>
    </div>
    </body>
    
    """
    st.markdown(html_temp, unsafe_allow_html=True)
  

    image_file = st.file_uploader("Subir imagen", type=['jpg', 'png', 'jpeg'])
    if image_file is not None:
        our_image = Image.open(image_file)
        st.text("Imagen original")
        st.image(our_image)

    if st.button("Ejecutar reconocimiento"):
        
        result_img= detect_faces(our_image)
        st.image(result_img)


if __name__ == '__main__':
    main()
