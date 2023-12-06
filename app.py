import streamlit as st 
import streamlit.components as stc
import plotly.express as px
# Utils
import base64 
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
import pandas as pd 

df = pd.read_csv('iris.csv')

# Display the Iris dataset
st.markdown('<h1 style="color:orange;">Iris Dataset </h1>', unsafe_allow_html=True)
st.write('**This is iris dataset**')
st.write(df)

st.markdown('<h1 style="color:green;">Charts View </h1>', unsafe_allow_html=True)
st.write('**This a multiple charts use function. It is very simple. you select chart and visualize data in liked chart.**')
# # Select chart type
chart_type = st.selectbox('Select Chart Type', ['Bar Chart', 'Line Chart', 'Scatter Plot'])


if chart_type == 'Bar Chart':
    fig = px.bar(df, x='sepal_length', y='sepal_width', title='Bar Chart')
elif chart_type == 'Line Chart':
    fig = px.line(df, x='sepal_length', y='sepal_width', title='Line Chart')
elif chart_type == 'Scatter Plot':
    fig = px.scatter(df, x='sepal_length', y='sepal_width', title='Scatter Plot')
st.plotly_chart(fig)



# Fxn
def text_downloader(raw_text):
	b64 = base64.b64encode(raw_text.encode()).decode()
	new_filename = "new_text_file_{}_.txt".format(timestr)
	st.markdown("#### Download File ###")
	href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click Here!!</a>'
	st.markdown(href,unsafe_allow_html=True)


def csv_downloader(data):
	csvfile = data.to_csv()
	b64 = base64.b64encode(csvfile.encode()).decode()
	new_filename = "new_text_file_{}_.csv".format(timestr)
	st.markdown("#### Download File ###")
	href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click Here!!</a>'
	st.markdown(href,unsafe_allow_html=True)

# Class
class FileDownloader(object):
	"""docstring for FileDownloader
	>>> download = FileDownloader(data,filename,file_ext).download()

	"""
	def __init__(self, data,filename='myfile',file_ext='txt'):
		super(FileDownloader, self).__init__()
		self.data = data
		self.filename = filename
		self.file_ext = file_ext

	def download(self):
		b64 = base64.b64encode(self.data.encode()).decode()
		new_filename = "{}_{}_.{}".format(self.filename,timestr,self.file_ext)
		st.markdown("#### Download File ###")
		href = f'<a href="data:file/{self.file_ext};base64,{b64}" download="{new_filename}">Click Here!!</a>'
		st.markdown(href,unsafe_allow_html=True)





def main():
	menu = ["Home","CSV","About"]

	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		my_text = st.text_area("Your Message")
		if st.button("Save"):
			st.write(my_text)
			# text_downloader(my_text)
			download = FileDownloader(my_text).download()


	elif choice == "CSV":
		df = pd.read_csv("iris.csv")
		st.dataframe(df)
		# csv_downloader(df)
		download = FileDownloader(df.to_csv(),file_ext='csv').download()


	else:
		st.subheader("About")



if __name__ == '__main__':
	main()
