import warnings
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def app(df):
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title("Visualise Hydraulic Systems")

    if st.checkbox("Show the correlation heatmap"):
        st.subheader("Correlation Heatmap")
        plt.figure(figsize=(10, 6))
        ax = sns.heatmap(df.iloc[:, 1:].corr(),
                         annot=True)  # Creating an object of seaborn axis and storing it in 'ax' variable
        bottom, top = ax.get_ylim()  # Getting the top and bottom margin limits.
        ax.set_ylim(bottom + 0.5, top - 0.5)  # Increasing the bottom and decreasing the top margins respectively.
        st.pyplot()

        st.markdown("""<p style = 'color:grey'>
        The heatmap above shows the correlation between features and output variables(CO and NOx). 
        It is easy to see that some features are negatively correlated each other. For example, 
        the correlation between TIT and CO is -0.71, and it means that when the Turbine Inlet Temperature 
        (TIT) decreases, the gas-turbine engine will produce more CO because a low TIT reduces the efficiency 
        of the gas-turbine engine(look at the figure below).
        """, unsafe_allow_html=True)
        img = Image.open("tit graph.png")
        st.image(img, caption='Graph')

    with st.expander("View Histograms"):
        cols = df.columns
        hist_col = st.selectbox("Select the column to view its histogram",cols)
        df[hist_col].hist()
        plt.show()
        st.pyplot()
        st.markdown("""<p style = 'color:Grey'>
        The dataset is clean and has not had any null values. 
        From the "describe" function can be seen that almost all variable holds a low SD, so the data is more concentrated to the mean. 
        It is also true because the sensory data is already averaged by the author( look at the paper). 
        Not all the features are normally distributed, I'm going to normalize the data before training a model.
        """,  unsafe_allow_html=True)
    with st.expander("View Boxplots"):
        df.boxplot(figsize = (10, 10), widths = 1)
        plt.show()
        st.pyplot()
        st.markdown("""<p style = 'color:grey'>
        The boxplot shows that more input variables are outliers, 
        so I'll use mean absolute error (MAE) to evaluate the model in modeling. 
        The MAE is not sensitive to the outliers
        """, unsafe_allow_html=True)




