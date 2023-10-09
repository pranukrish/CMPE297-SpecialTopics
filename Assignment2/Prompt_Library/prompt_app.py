import gradio as gr

import openai

# Make sure to set up your API key
openai.api_key = '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'

def get_gpt4_feedback(query):
    # Use the OpenAI API to get a response from the model
    response = openai.Completion.create(
        engine="gpt-4",  # You may need to adjust this for GPT-4 if it's different
        prompt=query,
        max_tokens=150  # Limit the response to 150 tokens
    )

    return response.choices[0].text.strip()  # Extracting the text from the API's response

# This function will be linked to the Gradio UI
def prompt_generator(user_query):
    feedback = get_gpt4_feedback(user_query)
    return feedback

# Define Gradio interface
iface = gr.Interface(
    fn=prompt_generator,  # function to call
    inputs="text",  # input type
    outputs="text",  # output type
    live=True,  # update output while typing (set to False if using actual GPT-4 to save on API calls)
    title="Prompt Generator with GPT-4 Assistance",
    description="Enter your initial query or requirement to get feedback from GPT-4.",
)

iface.launch()
