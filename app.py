import pickle
import streamlit as st
from streamlit_option_menu import option_menu

pce_model = pickle.load(open("pce.pkl",'rb'))
jsc_model = pickle.load(open("jsc.pkl",'rb'))
voc_model = pickle.load(open("voc.pkl",'rb'))
ff_model = pickle.load(open("ff.pkl",'rb'))

le_cell_arch = pickle.load(open("le_cell_arch.pkl", "rb"))
le_substrate_stack_sequence = pickle.load(open("le_substrate_stack_sequence.pkl", "rb"))

custom_css = """
    <style>
        body {
            background-color: #DDA0DD;
        }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
with st.sidebar:
    st.image("https://as2.ftcdn.net/v2/jpg/05/74/98/03/1000_F_574980328_1H6EOdcXUM5PUa3BDBC3Zu2lQbUipR9C.jpg")
    selected = option_menu('Flexible solar cell performance prediction',
                           ['Introduction page','PCE Prediction', 'JSC Prediction',
                            'VOC Prediction', 'FF Prediction'])

if selected == 'Introduction page':
    st.title("Welcome to My Introduction Page!")
    st.write("Hi there! I'm Sangratna Gaikwad, pursuing my M.Tech in IIT Kharagpur majoring in Renewable Energy Technologies.")
    st.write("I have automated my M.Tech project into an interactive web application that predicts the performance of flexible solar cells.")
    
    st.subheader("Connect with Me:")
    
    # Add your social media links here with icons and formatting
    st.markdown("📧 [Email](mailto:gsangratna21@gmail.com)")
    st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/sangratna-gaikwad-395376134)")
    st.markdown("📱 [WhatsApp](tel:+917350521650)")
    
    st.subheader("Lets Explore the predictions")

if selected == 'PCE Prediction':
    st.title('PCE Prediction Using ML')
    HOMO = st.number_input("HOMO", min_value=-0.62, max_value=1.2, step=.01, value=0.5)
    LUMO = st.number_input("LUMO", min_value=-0.54, max_value=1.35, step=0.01, value=0.5)
    cell_area_measured = st.number_input("Cell_area_measured", min_value=0.01, max_value=10.0, step=0.01, value=1.5)
    cell_architecture = st.selectbox("Cell Architecture", ['nip', 'pin'])
    substrate_stack_sequence = st.selectbox("Substrate Stack Sequence", ['PET | ITO', 'PET', 'SLG | ITO', 'PET | IZO', 'PEN | ITO', 'PET | Ag-grid', 'Ti'])
    perovskite_band_gap = st.number_input("Perovskite Band Gap", min_value=1.39, max_value=1.72, step=0.01, value=1.53)

    cell_architecture_encoded = le_cell_arch.transform([cell_architecture])[0]
    substrate_stack_sequence_encoded = le_substrate_stack_sequence.transform([substrate_stack_sequence])[0]

    # Create a dictionary with user input
    input_data = {
        'HOMO': HOMO,
        'LUMO': LUMO,
        'Cell_area_measured': cell_area_measured,
        'Cell_architecture': cell_architecture_encoded,
        'Substrate_stack_sequence': substrate_stack_sequence_encoded,
        'Perovskite_band_gap': perovskite_band_gap
    }

    # Perform prediction
    if st.button('Predict PCE'):
        # Perform prediction
        pce_prediction = pce_model.predict([list(input_data.values())])[0]

        # Display the prediction result
        st.subheader("Prediction Result:")
        st.write(f"PCE Prediction: {pce_prediction}%")

# Repeat the structure for other predictions (JSC, VOC, FF) with their respective models and input features.


if selected == 'JSC Prediction':
    st.title('JSC Prediction Using ML')
    HOMO = st.number_input("HOMO", min_value=-0.62, max_value=1.2, step=0.01, value=0.5)
    LUMO = st.number_input("LUMO", min_value=-0.54, max_value=1.35, step=0.01, value=0.5)
    cell_area_measured = st.number_input("Cell_area_measured", min_value=0.01, max_value=10.0, step=0.01, value=1.5)
    cell_architecture = st.selectbox("Cell Architecture", ['nip', 'pin'])
    substrate_stack_sequence = st.selectbox("Substrate Stack Sequence", ['PET | ITO', 'PET', 'SLG | ITO', 'PET | IZO', 'PEN | ITO','PET | Ag-grid','Ti'])
    perovskite_band_gap = st.number_input("Perovskite Band Gap", min_value=1.39, max_value=1.72, step=0.01, value=1.53)

    cell_architecture_encoded = le_cell_arch.transform([cell_architecture])[0]
    substrate_stack_sequence_encoded = le_substrate_stack_sequence.transform([substrate_stack_sequence])[0]

    
    # Create a dictionary with user input
    input_data = {
    'HOMO': HOMO,
    'LUMO': LUMO,
    'Cell_area_measured': cell_area_measured,
    'Cell_architecture':  cell_architecture_encoded,
    'Substrate_stack_sequence': substrate_stack_sequence_encoded,
    'Perovskite_band_gap': perovskite_band_gap
}

# Perform prediction
# Predict button
    if st.button('Predict jsc'):
        jsc_prediction = jsc_model.predict([list(input_data.values())])[0]

    # Display the prediction result
        st.subheader("Prediction Result:")
        st.write(f" Prediction: {jsc_prediction} mA/cm^2")

if selected == 'VOC Prediction':
    st.title('VOC Prediction Using ML')
    HOMO = st.number_input("HOMO", min_value=-0.62, max_value=1.2, step=0.01, value=0.5)
    LUMO = st.number_input("LUMO", min_value=-0.54, max_value=1.35, step=0.01, value=0.5)
    cell_area_measured = st.number_input("Cell_area_measured", min_value=0.01, max_value=10.0, step=0.01, value=1.5)
    cell_architecture = st.selectbox("Cell Architecture", ['nip', 'pin'])
    substrate_stack_sequence = st.selectbox("Substrate Stack Sequence", ['PET | ITO', 'PET', 'SLG | ITO', 'PET | IZO', 'PEN | ITO','PET | Ag-grid','Ti'])
    perovskite_band_gap = st.number_input("Perovskite Band Gap", min_value=1.39, max_value=1.72, step=0.01, value=1.53)

    cell_architecture_encoded = le_cell_arch.transform([cell_architecture])[0]
    substrate_stack_sequence_encoded = le_substrate_stack_sequence.transform([substrate_stack_sequence])[0]

    
    # Create a dictionary with user input
    input_data = {
    'HOMO': HOMO,
    'LUMO': LUMO,
    'Cell_area_measured': cell_area_measured,
    'Cell_architecture':  cell_architecture_encoded,
    'Substrate_stack_sequence': substrate_stack_sequence_encoded,
    'Perovskite_band_gap': perovskite_band_gap
}

# Perform prediction
# Predict button
    if st.button('Predict VOC'):
    # Perform prediction
        voc_prediction = voc_model.predict([list(input_data.values())])[0]

    # Display the prediction result
        st.subheader("Prediction Result:")
        st.write(f"voc Prediction: {voc_prediction} mV")

if selected == 'FF Prediction':
    st.title('FF Prediction Using ML')
    HOMO = st.number_input("HOMO", min_value=-0.62, max_value=1.2, step=0.01, value=0.5)
    LUMO = st.number_input("LUMO", min_value=-0.54, max_value=1.35, step=0.01, value=0.5)
    cell_area_measured = st.number_input("Cell_area_measured", min_value=0.01, max_value=10.0, step=0.01, value=1.5)
    cell_architecture = st.selectbox("Cell Architecture", ['nip', 'pin'])
    substrate_stack_sequence = st.selectbox("Substrate Stack Sequence", ['PET | ITO', 'PET', 'SLG | ITO', 'PET | IZO', 'PEN | ITO','PET | Ag-grid','Ti'])
    perovskite_band_gap = st.number_input("Perovskite Band Gap", min_value=1.39, max_value=1.72, step=0.01, value=1.53)

    cell_architecture_encoded = le_cell_arch.transform([cell_architecture])[0]
    substrate_stack_sequence_encoded = le_substrate_stack_sequence.transform([substrate_stack_sequence])[0]

    
    # Create a dictionary with user input
    input_data = {
    'HOMO': HOMO,
    'LUMO': LUMO,
    'Cell_area_measured': cell_area_measured,
    'Cell_architecture':  cell_architecture_encoded,
    'Substrate_stack_sequence': substrate_stack_sequence_encoded,
    'Perovskite_band_gap': perovskite_band_gap
}

# Perform prediction
# Predict button
    if st.button('Predict FF'):
    # Perform prediction
        ff_prediction = ff_model.predict([list(input_data.values())])[0]

    # Display the prediction result
        st.subheader("Prediction Result:")
        st.write(f"voc Prediction: {ff_prediction*100} %")
