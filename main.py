import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import ctransformers

# Comms with LLama 2

def getLLamaResponse(input_text, number_of_words, blog_style):
    llm = ctransformers.CTransformers(model="models/llama-2-7b-chat.ggmlv3.q8_0.bin", model_type="llama")

    template = """
    write a blog for {{blog_style}} on topic of {{input_text}} with words length of {{number_of_words}}
    """

    Prompt = PromptTemplate(input_variables=['blog_style', 'input_text', 'number_of_words'], template=template)

    response = llm.invoke((Prompt.format(blog_style=blog_style, input_text=input_text, number_of_words=number_of_words)))
    print(response)
    return response

st.set_page_config(page_title="Generate Content",
                    page_icon='🚩',
                    layout='centered',
                    initial_sidebar_state='collapsed'
                    )
st.header("Generate Content To Replace ContentWriters 🚩")

input_text = st.text_input("Enter The Topic")

col1, col2 = st.columns([5, 5])

with col1:
    number_of_words = st.text_input("Blog Length")
with col2:
    blog_style = st.selectbox('writing the blog for ', ('Researchers', 'Engineers', 'common people'), index=0)

submit = st.button("Generate")

if submit:
    st.write(getLLamaResponse(input_text, number_of_words, blog_style))

