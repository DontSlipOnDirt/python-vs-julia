import streamlit as st
# from julia import Julia
# jl = Julia(compiled_modules=False)
# from julia import Main as jl
# import numpy as np
import benchmarks as bench

test = 0

# sidebar
with st.sidebar:

    if st.button("Test 1"):
        test = 1

    if st.button("Test 2"):
        test = 2

    if st.button("Test 3"):
        test = 3
    
st.title("Python vs. Julia")

if test == 1:
    jl_time, py_time = bench.test_matrix_mult_benchmark()
    st.write("Julia Time:", jl_time)
    st.write("Python Time:", py_time)

elif test == 2:
    # jl_time, py_time = bench.test_elementwise_exp_benchmark()
    # st.write("Julia Time:", jl_time)
    # st.write("Python Time:", py_time)

    st.write("Test 2")

elif test == 3:
    # jl_time, py_time = bench.test_gradient_benchmark()
    # st.write("Julia Time:", jl_time)
    # st.write("Python Time:", py_time)

    st.write("Test 3")

else:
    st.write("Please select a test to run")