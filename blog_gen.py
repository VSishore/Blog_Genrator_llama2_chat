import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

#Function to get responce from llama-2 model
def get_llama_response(input_text,no_words,blog_style,overview):
    llm=CTransformers(model='model/llama-2-7b-chat.ggmlv3.q8_0.bin',model_type="llama",config={'max_new_tokens':256,
                                                       'temperature':0.01})
    

    #prompt templete
    template="""
    write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words.give the topics overview{overview}to know about the intension."""

    prompt=PromptTemplate(input_variables=['blog_Style','input_text','n_words','overview'], template=template)


    # Generate the Response from llama 2 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words,overview=overview))
    print(response)
    return response


st.set_page_config(page_title="Blog Generator",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed'
)

st.header("Blog Generator 🤖")

input_text=st.text_input("Enter the BLog Topic")
## creating another two column for additional two fields

coll,coll2=st.columns([5,5])

with coll:
    no_words=st.text_input('No.of Words')
with coll2:
    blog_style=st.selectbox('Wiritng the blog for',('Teachers','Students','Common people','childrens'),index=0)
overview=st.text_input('overview about the topics')

submit=st.button('Generate')

#Final response
if submit:
    st.write(get_llama_response(input_text,no_words,blog_style,overview))


    