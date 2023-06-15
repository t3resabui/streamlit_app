import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

web_apps = st.sidebar.selectbox("Select Web Apps", ("Exploratory Data Analysis", "Distributions"))

df = None

if web_apps == "Exploratory Data Analysis":
    uploaded_file = st.sidebar.file_uploader("Choose a file")

    if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:
        df = pd.read_csv(uploaded_file)
        show_df = st.checkbox("Show Data Frame", key="disabled")

        if show_df:
            st.write(df)

        num_rows = df.shape[0]
        num_columns = df.shape[1]
        num_categorical = len(df.select_dtypes(include=['object']).columns)
        num_numerical = len(df.select_dtypes(include=['int64', 'float64']).columns)
        num_date = len(df.select_dtypes(include=['int64']).columns)

        st.subheader("Dataset Statistic")
        st.write("Number of rows:", num_rows)
        st.write("Number of columns:", num_columns)
        st.write("Number of categorical variables:", num_categorical)
        st.write("Number of numerical variables:", num_numerical)
        st.write("Number of date variables:", num_date)

        selected_column = st.sidebar.selectbox("Select a Column", df.columns)

        column_type = st.sidebar.selectbox('Select Data Type', ("Numerical", "Categorical", "Date"))

        if column_type == "Numerical":
            numerical_column = st.sidebar.selectbox('Select a Column', df.select_dtypes(include=['int64', 'float64']).columns)

            # histogram
            choose_color = st.color_picker('Pick a Color', "#69b3a2")
            choose_opacity = st.slider('Color Opacity', min_value=0.0, max_value=1.0, step=0.05)

            hist_bins = st.slider('Number of bins', min_value=5, max_value=150, value=30)
            hist_title = st.text_input('Set Title', 'Histogram')
            hist_xtitle = st.text_input('Set x-axis Title', numerical_column)

            fig, ax = plt.subplots()
            ax.hist(df[numerical_column], bins=hist_bins, edgecolor="black", color=choose_color, alpha=choose_opacity)
            ax.set_title(hist_title)
            ax.set_xlabel(hist_xtitle)
            ax.set_ylabel('Count')

            st.pyplot(fig)
            filename = "plot.png"
            fig.savefig(filename, dpi=300)

             # Display the download button
            with open("plot.png", "rb") as file:
              btn = st.download_button(
                  label="Download image",
                  data=file,
                  file_name="flower.png",
                  mime="image/png"
              )
            
        elif column_type == "Categorical":
          categorical_column = st.sidebar.selectbox('Select a Column', df.select_dtypes(include=['object']).columns)

          choose_color = st.color_picker('Pick a Color', "#69b3a2")

          category_count = df[categorical_column].value_counts()
          category_proportions = df[categorical_column].value_counts(normalize=True)

          bar_title = st.text_input('Set Title', 'Bar Plot')
          bar_xtitle = st.text_input('Set x-axis Title', categorical_column)

          st.write("Category Counts:")
          st.write(category_count)

          st.write("Category Proportions:")
          st.write(category_proportions)

          fig, ax = plt.subplots()
          sns.countplot(data=df, x=categorical_column, color = choose_color)
          ax.set_title(f"Bar Plot: {categorical_column}")
          ax.set_xlabel(categorical_column)
          ax.set_ylabel("Count")

          st.pyplot(fig)
          filename = "barplot.png"
          fig.savefig(filename, dpi=300)

          # Display the download button
          with open("plot.png", "rb") as file:
            btn = st.download_button(
                label="Download image",
                data=file,
                file_name="flower.png",
                mime="image/png"
            )

        elif column_type == "Date":
          date_column = st.sidebar.selectbox('Select a Column', df.select_dtypes(include=['int64']).columns)

          # Bar plot
          choose_color = st.color_picker('Pick a Color', "#69b3a2")

          year_counts = df[date_column].value_counts().sort_index()
          year_proportions = df[date_column].value_counts(normalize=True).sort_index()

          st.write("Year Counts:")
          st.write(year_counts)

          st.write("Year Proportions:")
          st.write(year_proportions)

          fig, ax = plt.subplots()
          ax.bar(year_counts.index, year_counts.values, color=choose_color)
          ax.set_title(f"Bar Plot: {date_column}")
          ax.set_xlabel(date_column)
          ax.set_ylabel("Count")

          st.pyplot(fig)
          filename = "barplot_yr.png"
          fig.savefig(filename, dpi=300)

          # Display the download button
          with open("plot.png", "rb") as file:
            btn = st.download_button(
                label="Download image",
                data=file,
                file_name="flower.png",
                mime="image/png"
            )

elif web_apps == "Distributions":
    uploaded_file = st.sidebar.file_uploader("Choose a file")

    if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:
        df = pd.read_csv(uploaded_file)
        show_df = st.checkbox("Show Data Frame", key="disabled")

        if show_df:
            st.write(df)

        num_rows = df.shape[0]
        num_columns = df.shape[1]
        num_categorical = len(df.select_dtypes(include=['object']).columns)
        num_numerical = len(df.select_dtypes(include=['int64', 'float64']).columns)
        num_date = len(df.select_dtypes(include=['int64']).columns)

        st.subheader("Dataset Statistic")
        st.write("Number of rows:", num_rows)
        st.write("Number of columns:", num_columns)
        st.write("Number of categorical variables:", num_categorical)
        st.write("Number of numerical variables:", num_numerical)
        st.write("Number of date variables:", num_date)

        selected_column = st.sidebar.selectbox("Select a Column", df.columns)

        column_type = st.sidebar.selectbox('Select Data Type', ("Numerical", "Categorical", "Date"))

        if column_type == "Numerical":
          numerical_column = st.sidebar.selectbox('Select a Column', df.select_dtypes(include=['int64', 'float64']).columns)

          # Density plot
          choose_color = st.color_picker('Pick a Color', "#69b3a2")
          choose_opacity = st.slider('Color Opacity', min_value=0.0, max_value=1.0, step=0.05)

          kde_title = st.text_input('Set Title', 'Density Plot')
          kde_xtitle = st.text_input('Set x-axis Title', numerical_column)
          kde_bandwidth = st.slider('Bandwidth', min_value=0.1, max_value=10.0, step=0.1, value=1.0)

          fig, ax = plt.subplots()
          sns.kdeplot(data=df[numerical_column], fill=True, color=choose_color, alpha=choose_opacity, bw_adjust=kde_bandwidth)
          ax.set_title(kde_title)
          ax.set_xlabel(kde_xtitle)
          ax.set_ylabel('Density')

          st.pyplot(fig)
          filename = "densityplot.png"
          fig.savefig(filename, dpi=300)

          # Display the download button
          with open("plot.png", "rb") as file:
            btn = st.download_button(
                label="Download image",
                data=file,
                file_name="densityplot.png",
                mime="image/png"
            )

        elif column_type == "Categorical":
          categorical_column = st.sidebar.selectbox('Select a Column', df.select_dtypes(include=['object']).columns)
          numerical_column = st.sidebar.selectbox('Select a Column', df.select_dtypes(include=['int64', 'float64']).columns)

          # Box plot
          boxplot_title = st.text_input('Set Title', 'Box Plot')
          boxplot_ytitle = st.text_input('Set y-axis Title', categorical_column)
          boxplot_color = st.color_picker('Set Box Color', '#1f77b4')
          boxplot_outlier_color = st.color_picker('Set Outlier Color', '#ff7f0e')
          boxplot_whisker_linestyle = st.selectbox('Set Whisker Line Style', ['-', '--', '-.', ':'])

          fig, ax = plt.subplots()
          sns.boxplot(data=df, x=categorical_column, y=numerical_column, color=boxplot_color, flierprops={'marker': 'o', 'markerfacecolor': boxplot_outlier_color, 'markeredgecolor': boxplot_outlier_color})
          ax.set_title(boxplot_title)
          ax.set_xlabel(categorical_column)
          ax.set_ylabel(boxplot_ytitle)

          # Customize whisker lines
          for whisker in ax.lines[4:8]:
              whisker.set_linestyle(boxplot_whisker_linestyle)

          st.pyplot(fig)
          filename = "plot.png"
          fig.savefig(filename, dpi=300)

        # Display the download button
          with open("plot.png", "rb") as file:
            btn = st.download_button(
                label="Download image",
                data=file,
                file_name="boxplot.png",
                mime="image/png"
            )

