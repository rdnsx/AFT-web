# AFT-web

This is a Python code that uses the Streamlit library to create a simple web application for tracking aquarium fertilizer.

The st.set_page_config() function sets the configuration of the web page, including the title, icon, and layout.

The @st.cache_data decorator is used to cache the result of the load_data() function, which reads a CSV file containing fertilizer data for an aquarium. Caching the data ensures that the file is only read once, even if the web page is refreshed multiple times.

The main() function is the main logic of the web application. It first sets the title of the page using st.title(), then loads the data using the load_data() function and displays it in a DataFrame using st.dataframe().

Finally, the if __name__ == '__main__': statement ensures that the main() function is only executed if the script is run directly (as opposed to being imported as a module).
