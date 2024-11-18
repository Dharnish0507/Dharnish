import random
import streamlit as st


def give_hint(user_guess, machine_number):
    if user_guess < machine_number:
        return "higher"
    elif user_guess > machine_number:
        return "lower"
    else:
        return "correct"


st.title("Guess the Machine's Number Game")


st.write("I have selected a number between 1 and 100. Your task is to guess it.")
st.write("I will give you hints after each guess: 'higher' if your guess is too low, and 'lower' if your guess is too high.")


if 'machine_number' not in st.session_state:
    st.session_state.machine_number = random.randint(1, 100)  # Machine randomly selects a number between 1 and 100
    st.session_state.attempts = 0  # Count number of attempts


user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)


if st.button("Submit Guess"):
    if user_guess == 0:  # If the user submits a 0 (a signal for invalid guess), do nothing
        st.warning("Please enter a valid number.")
    else:
        
        st.session_state.attempts += 1

        
        hint = give_hint(user_guess, st.session_state.machine_number)

        if hint == "correct":
            st.write(f"Congratulations! You guessed the number {st.session_state.machine_number} correctly in {st.session_state.attempts} attempts!")
            if st.button("reset "):
                st.session_state.machine_number = random.randint(1, 100)  # Pick a new random number
                st.session_state.attempts = 0
        else:
            st.write(f"Guess  {hint}. Try again!")
