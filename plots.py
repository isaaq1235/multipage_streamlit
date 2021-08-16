import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def app(car_data):
    st.sidebar.subheader("Plots")

# Choosing x-axis values for the scatter plot.
# Add a multiselect in the sidebar with the 'Select the x-axis values:' label
    st.set_option('deprecation.showPyplotGlobalUse', False)

    feat_list = st.sidebar.multiselect('Select the x-axis values', ('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick'))


    st.sidebar.subheader("Visualistaion Selector")
# Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
    plot_types = st.sidebar.multiselect('Select the Charts/Plots:', ('Scatter Plot','Histogram', 'Box Plot', 'Correlation Heatmap', 'Pair Plot'))

    if 'Scatter Plot' in plot_types:
        for i in feat_list:
            st.subheader(f"Scatter Plot between {i} and Price of Car")
            plt.figure(figsize = (16,9))
            sns.scatterplot(x = i, y = "price", data = car_data)
            st.pyplot()

    if 'Histogram' in plot_types:
        for i in feat_list:
            st.subheader(f"Histogram between {i} and Price of Car")
            plt.figure(figsize = (16,9))
            plt.hist(x = car_data[i])
            st.pyplot()

    if 'Box Plot' in plot_types:
        for i in feat_list:
            st.subheader(f"Boxplot between {i} and Price of Car")
            plt.figure(figsize = (16,9))
            sns.boxplot(x = car_data[i])
            st.pyplot()

    if 'Correlation Heatmap' in plot_types:
        st.subheader(f"Heatmap of Car Prices")
        plt.figure(figsize = (16,9))
        ax = sns.heatmap(car_data.corr(), annot = True)
        bottom,top = ax.get_ylim()
        ax.set_ylim(bottom + 0.5, top - 0.5)
        st.pyplot()

    if 'Pair Plot' in plot_types:
  # plot pair plot
        st.subheader(f"Pair Plot of Car Prices")
        plt.figure(figsize = (16,9))
        sns.pairplot(car_data)
        st.pyplot()

