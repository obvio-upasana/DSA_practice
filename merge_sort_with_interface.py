import streamlit as st

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def run_merge_sort_app():
    # Set the page to use a dark theme
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
    st.markdown("""
        <style>
        .stApp {
            background-color: #0E1117;
            color: #FAFAFA;
        }
        .css-1d391kg {
            background-color: #262730;
            color: #FAFAFA;
        }
        </style>
        """, unsafe_allow_html=True)

    st.title('Merge Sort Visualization App')
    st.markdown('Enter a list of numbers, and I\'ll sort them for you using the Merge Sort algorithm! 💻')

    # Input for the array
    user_input = st.text_input('Enter numbers separated by commas (e.g., 12, 11, 13, 5, 6, 7)', '12, 11, 13, 5, 6, 7')

    # Button to trigger the sorting process
    if st.button('Sort'):
        try:
            # Convert the input string to a list of integers
            arr = [int(item.strip()) for item in user_input.split(',')]
            
            # Make a copy of the original array to display later
            original_arr = list(arr)
            
            # Perform merge sort on the array
            mergeSort(arr)
            
            st.success('Sorting complete! 🎉')
            
            # Display the results in a formatted box
            st.subheader('Results:')
            
            st.write(f"**Original Array:** {original_arr}")
            st.write(f"**Sorted Array:** {arr}")
            
        except ValueError:
            st.error("Invalid input. Please enter numbers separated by commas.")

if __name__ == '__main__':
    run_merge_sort_app()
    