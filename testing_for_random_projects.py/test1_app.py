import streamlit as st

def solve_math_problem(problem):
    """
    Solves simple math problems given as strings, e.g., "2 + 3", "10 / 2".
    Supports +, -, *, / operators.
    """
    try:
        # Only allow safe characters
        allowed_chars = "0123456789+-*/.() "
        if not all(c in allowed_chars for c in problem):
            return "Invalid characters in problem."
        result = eval(problem)
        return result
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("viraaj made this ik it seems weird but its only a beta version")

user_input = st.text_input("Enter a simple math problem (e.g., 2 + 2):")

if st.button("Solve"):
    output = solve_math_problem(user_input)
    st.write(f"**Result:** {output}")
    if isinstance(output, (int, float)):
        formatted_output = f"{output:,}"
        st.write(f"**Formatted Result:** {formatted_output}")