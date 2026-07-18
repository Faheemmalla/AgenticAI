import os
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
from langchain_groq import ChatGroq
model = ChatGroq(model="qwen/qwen3.6-27b")

st.header('Reasearch Tool')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

current_dir = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(current_dir, 'template.json')
template = load_prompt(template_path)



if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result.content)