import streamlit as st

def app(car_data):
    st.header("Car Price Dataset")
    with st.expander("Car Price Data"):
        st.dataframe(car_data)

    st.subheader("Columns Description:")
        
    if st.checkbox("Show summary"):
        st.table(car_data.describe())

    beta_col1, beta_col2, beta_col3 = st.columns(3)

    # Add a checkbox in the first column. Display the column names of 'car_df' on the click of checkbox.
    with beta_col1:
        if st.checkbox("Show all column names"):
            st.table(list(car_data.columns))

    # Add a checkbox in the second column. Display the column data-types of 'car_df' on the click of checkbox.
    with beta_col2:
        if st.checkbox("View column data-type"):
            dtypes_list = list(car_data.dtypes)
            dtypes = {
            list(car_data.columns)[0] : dtypes_list[0],
            list(car_data.columns)[1] : dtypes_list[1],
            list(car_data.columns)[2] : dtypes_list[2],
            list(car_data.columns)[3] : dtypes_list[3],
            list(car_data.columns)[4] : dtypes_list[4]
            }
            st.write(dtypes)

    # Add a checkbox in the third column followed by a selectbox which accepts the column name whose data needs to be displayed.
    with beta_col3:
        if st.checkbox("View column data"):
            column_data = st.selectbox('Select column', tuple(car_data.columns))
            st.write(car_data[column_data])

