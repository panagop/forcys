import streamlit as st
import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
# from mpl_toolkits.basemap import Basemap

from forcys.time_funcs import timestring
from forcys.wavedata import WaveDataFile, WaveVariable

st.title('Forcys - Wave')

# folder_path = '../data'
folder_path = 'data'

# Get a list of all files in the folder
files = os.listdir(folder_path)

selected_file = st.sidebar.selectbox('Select a file', files)

wdf = WaveDataFile.from_file(folder_path + '/' + selected_file)

st.sidebar.divider()

radio_selection = st.sidebar.radio('Select a plot', ('Contour plot', 'Time series'), index=0)

st.sidebar.divider()

selected_variable = st.sidebar.selectbox('Select a variable', wdf.variables)
myvar = WaveVariable(wdf, selected_variable)

st.sidebar.write(f'{selected_variable}: {myvar.long_name}')

st.sidebar.divider()

var_array = myvar.values  # Reads the netCDF variable MT, array of one element

st.sidebar.write('Start Time:', timestring(wdf.time[0]))
st.sidebar.write('End Time:', timestring(wdf.time[-1]))

selected_date = st.sidebar.date_input('Select a date', datetime.fromtimestamp(
    wdf.time[0]), min_value=datetime.fromtimestamp(wdf.time[0]),
    max_value=datetime.fromtimestamp(wdf.time[-1]))
selected_hour = st.sidebar.slider(
    'Select a time', min_value=0, max_value=23, value=0)
selected_datetime = datetime(
    selected_date.year, selected_date.month,
    selected_date.day, selected_hour, 0)
if selected_datetime > datetime.fromtimestamp(wdf.time[-1]):
    selected_datetime = datetime.fromtimestamp(wdf.time[-1])
if selected_datetime < datetime.fromtimestamp(wdf.time[0]):
    selected_datetime = datetime.fromtimestamp(wdf.time[0])

timestamp = datetime.timestamp(selected_datetime)

# time_index = 500
time_index = np.where(wdf.time == timestamp)[0][0]

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(8, 5))

# Add label and title to the plot
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_title(
    f"{myvar.long_name} ({selected_variable}) - \
        {timestring(wdf.time[time_index])}")

# Create a contour plot
contourf = ax.contourf(np.array(wdf.lon), np.array(
    wdf.lat), var_array[time_index], cmap='jet',
    levels=np.linspace(myvar.min_value, myvar.max_value, num=50))
cbar = fig.colorbar(contourf, ax=ax, extend='both', ticks=np.linspace(
    myvar.min_value, myvar.max_value, num=11))

# Show the plot
st.pyplot(fig)

with st.expander('Dataset info', expanded=True):
    st.write(wdf.dataset)

checkbox = st.sidebar.checkbox('Show expander', value=False)
if checkbox:
    with st.expander('Save csv', expanded=True):
        selected_lat = st.select_slider('Select latitude', wdf.lat)
        selected_lon = st.select_slider('Select longitude', wdf.lon)
        multivariables = st.multiselect('Select variables', wdf.variables)

        # selected_wvs = [WaveVariable(wdf, var) for var in multivariables]

        mydict = {'time': wdf.time}
        for mv in multivariables:
            temp_var = WaveVariable(wdf, mv)
            mydict[mv] = temp_var.get_time_history_at_coords(
                selected_lat, selected_lon)

        df = pd.DataFrame(mydict)

        st.write(df)

        st.download_button('Download CSV', df.to_csv(index=False), 'data.csv', 'text/csv')
        # df.to_csv('data.csv', index=False)










