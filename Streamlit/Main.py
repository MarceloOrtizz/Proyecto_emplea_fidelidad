import streamlit as st
import numpy as np
from streamlit_folium import st_folium
from st_on_hover_tabs import on_hover_tabs
import pandas as pd
import pickle

st.set_page_config(
    layout="wide",
    page_title="Emplea Fidelidad",
    page_icon="👋",
    initial_sidebar_state="expanded"
)


# def KNN_model_predict(params, slider_count):
    
#     key_file_path = './GCP_service_account/key_storage_ML.json'
#     bucket_name= 'data_clear_ml'
#     file_name = 'modelo1_knn.pkl'

#     # Set up authentication with service account key file

#     storage_client = storage.Client.from_service_account_json(key_file_path)

#      # Download the file from the bucket
#     try:
#         bucket = storage_client.bucket(bucket_name)
#         blob = bucket.blob(file_name)
#         model_data  = blob.download_as_bytes()
#         knn_model_file = pickle.loads(model_data)
#         indexes = knn_model_file.kneighbors([params],slider_count)[1][0]

#     except Exception as e:
#         print(f"Error downloading file: {e}")

#     return indexes


st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

with st.sidebar:
    tabs = on_hover_tabs(tabName=['Home', 'Dashboard'], 
                         iconName=['home', 'dashboard'], default_choice=0)

if tabs=="Home":
        with st.container(border=True):
            st.header("Emplea Fidelidad/:blue[grupo 63]:rocket:", divider='rainbow',anchor=False)


            st.subheader('Contexto y Problematica')

            contextoProblematica = '''Hoy en día, la retención de empleados se ha convertido en una de las principales preocupaciones para las empresas. <br>
            La alta rotación de personal no solo representa costos significativos en términos de reclutamiento y capacitación, sino que también afecta negativamente la moral del equipo y la productividad general. <br>
            Las organizaciones que no logran retener a sus empleados ierden talento valioso y enfrentan desafíos adicionales para mantener la continuidad en sus operaciones.'''
              
            st.markdown(contextoProblematica)

            st.subheader('Impacto de la Problemática')

            impactoProblematica = '''La incapacidad de retener a los empleados puede llevar a una serie de problemas, incluyendo:<br>
            **Aumento de Costos:** Gastos en reclutamiento, formación de nuevos empleados y pérdida de productividad durante el período de adaptación.<br>       
            **Pérdida de Conocimiento:** Los empleados que se marchan llevan consigo el conocimiento adquirido sobre los procesos y la cultura de la empresa.<br>
            **Desmoralización del Equipo:** La salida frecuente de colegas puede afectar la moral y la motivación del equipo restante.'''

            st.markdown(impactoProblematica)

            st.subheader('Objetivo del Proyecto')

            objetivoProyecto = '''El objetivo principal de este proyecto es analizar los datos de recursos humanos para identificar los factores que influyen en la retención de empleados y desarrollar estrategias efectivas para mejorar la retención
            '''
            st.markdown(objetivoProyecto)

            st.subheader('Conclusion')

            conclusion = '''El análisis de retención de empleados proporciona una oportunidad invaluable para que las empresas comprendan mejor las razones detrás de la rotación de personal y tomen medidas proactivas para mejorar la satisfacción y retención de sus empleados. <br> 
            Con un enfoque basado en datos y el uso de modelos de machine learning, se pueden desarrollar estrategias efectivas que no solo mejoren la retención, sino que también contribuyan al crecimiento y éxito a largo plazo de la empresa.
            '''
            st.markdown(conclusion)
            
            st.subheader('Autores:')
            authors = '''   **Matias Ponce** - PM / Data Engineer <br>
                            **Francisco Vela** - Data Analyst <br>
                            **Marcelo Ortiz** - Data Analyst <br>  
                            **Dayana Vega** - Data Scientist <br>
                            **Gerardo Toso** - Data Scientist <br> 
                            **David Ramirez** - ML Engineer <br>
                            **Daniel Ceballos** - ML Engineer <br>
            '''
            st.markdown(authors)

elif tabs=="Dashboard":
        # st.header("Dashboard DPT05/:blue[grupo 3]:rocket:", divider='rainbow')
        embed_url = "https://app.powerbi.com/view?r=eyJrIjoiZjM5ZDVkODUtYWFmZi00NTk2LTkyNWEtYmE4YjhhZGEyMmYwIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9"
        st.components.v1.iframe(src=embed_url, height=800, width=1100)

# elif tabs=="ML":
        
#         st.header("Machine Learning Acceso al modelo entrenado", divider='rainbow',anchor=False)
        
#         st.header("Parametros", anchor=False)
#         col1, col2, col3= st.columns([1,1,2])
#         with st.form("Trained_model"):
            
                
#             with col1:           

#                     slider_count  = st.slider("Cant a devolver", min_value=3, max_value=10)
#                     toggle_takeout = st.toggle('Takeout')
#                     toggle_delivery = st.toggle('Delivery')
#                     toggle_kids = st.toggle('Entretenimientos de ninos')
#                     toggle_creditcard = st.toggle('Acepta Tarjeta de Credito')
#                     toggle_reservation = st.toggle('Se hacen reservas')
#                     toggle_wifi = st.toggle('Wifi disponible')
            
#             with col2:
                    
#                     toggle_dogs = st.toggle('Pet friendly')
#                     toggle_alcohol = st.toggle('Venta de Alcohol')
#                     toggle_hamburger= st.toggle('Hacen hamburguesas')
#                     toggle_sandwich = st.toggle('Hacen sandwiches')
#                     toggle_breakfast = st.toggle('Tienen desayuno')
#                     toggle_ice = st.toggle('Tienen helados')
#                     toggle_chiken = st.toggle('Tienen pollo')
#                     toggle_mexican = st.toggle('Comida mexicana')
#                     toggle_american = st.toggle('Comida yankee')     
#                     print("pollo", toggle_chiken) 
#                     print("mex", toggle_mexican)
            
#             with col3:                
        
#                 m = folium.Map(location=[38, -97], zoom_start=4)
#                 folium.Marker([37, -97], popup="Ubicacion Seleccionada", tooltip='Ubicacion Seleccionada').add_to(m)
#                 st_data = st_folium(m, width=800, height=350)
                
                
#                 try :
#                     lc_lat = float(st_data['last_clicked']['lat'])
#                     lc_long = float(st_data['last_clicked']['lng'])

#                     print(lc_lat, lc_long)
#                     folium.Marker([lc_lat, lc_long], popup="Ubicacion Seleccionada", tooltip='Ubicacion Seleccionada').add_to(m)

#                 except:
#                     print('fisrt time passed')

#             submitted = st.form_submit_button(label="Enviar",
#                                                                     help=None,
#                                                                     on_click=None,
#                                                                     args=None,
#                                                                     kwargs=None,
#                                                                     type="primary",
#                                                                     disabled=False,
#                                                                     use_container_width=True)
                            
#             if submitted:
                        
#                         if 'lc_lat' not in globals() or 'lc_lat' not in locals():
#                                 st.warning('Especifique un punto de interes en el plano', icon="⚠️")
                       
#                         else:
                        
#                             params = [lc_lat,
#                                     lc_long,
#                                     toggle_takeout,
#                                     toggle_delivery,
#                                     toggle_kids,
#                                     toggle_creditcard,
#                                     toggle_reservation,
#                                     toggle_wifi,
#                                     toggle_dogs,
#                                     toggle_alcohol,
#                                     toggle_hamburger,
#                                     toggle_sandwich,
#                                     toggle_breakfast,
#                                     toggle_ice,
#                                     toggle_chiken,
#                                     toggle_mexican,
#                                     toggle_american
#                                 ]
#                             indexes = tuple(KNN_model_predict(params, slider_count))
                        
#                             locations_df = get_business_locations(indexes)
                            
# # calculate locations bounds

#                             sw = [np.min(locations_df['latitude']), np.max(locations_df['longitude'])]
#                             ne = [np.max(locations_df['latitude']), np.min(locations_df['longitude'])]
        
                    
#                             c1, c2 = st.columns([1,1])
#                             with c1:
#                                 print(locations_df)          
                                        
#                                 lc_lat = float(st_data['last_clicked']['lat'])
#                                 lc_long = float(st_data['last_clicked']['lng'])
                                
                                
#                                 m1 = folium.Map(location=[(np.mean(locations_df['latitude'])+lc_lat)/2, (np.mean(locations_df['longitude'])+lc_long)], zoom_start=4)      
                                                      
                                
#                                 folium.Marker([lc_lat, lc_long], popup="Ubicacion Seleccionada", tooltip='Ubicacion Seleccionada',icon=folium.Icon(color='red')).add_to(m1)
                                
                                                             
#                                 for index, row in locations_df.iterrows():
                                                        
#                                         folium.Marker(
#                                             location=[row['latitude'], row['longitude']],
#                                             popup=row['name']
#                                             ).add_to(m1)
                                        

                                        
#  # pass bunds to the map from returned data
                                
#                                 m1.fit_bounds([sw, ne])
#                                 st_folium(m1, height=400, width=700)
                                
#                             with c2:
#                                 st.dataframe(locations_df)
