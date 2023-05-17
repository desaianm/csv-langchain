import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "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";




def main():
    st.set_page_config(page_title="Ask your Csv")
    st.header("Ask your CSV")

    user_csv =st.file_uploader("Upload  your Csv File",type="csv")
    user_question = st.text_input("Ask a Question abpit your Csv: ")
    
    if user_csv is not None: 
        
        llm = OpenAI(temperature=0)
        agent = create_csv_agent(llm, user_csv,verbose=True);

    if user_question is not None and user_question!= "":
        response = agent.run(user_question)
        st.write(response)



if __name__ == "__main__":
    main()    
