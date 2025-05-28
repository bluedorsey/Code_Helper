from google import genai
from google.genai.types import GenerateContentConfig
import streamlit as st 
import os 
from dotenv import load_dotenv # Load environment variables from a .env file    
load_dotenv()


client=genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))#add your api key in .env file



#for debugging the code 
def debugging (question):
    System_instrunction="""you are the best software engineer .can debug any code in any language with point wise explaination and without step by step breakdown """
    response=client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=question,
         config=GenerateContentConfig(
        system_instruction=System_instrunction,
        temperature=0.2,),
        
    )
    st.write(response.text)

#for explaination of code
def explaination (question):
    System_instrunction="""you are great programer who has a very good knowledge to explain the code of any language """
    response=client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=question,
         config=GenerateContentConfig(
        system_instruction=System_instrunction,
        temperature=0.2,),
        
    )
    st.write(response.text)

#for enhancemnet of code 
def enhancement (question):
    System_instrunction="""enhance the code with shortening the length and commneting line that help to understand the code """
    response=client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=question,
         config=GenerateContentConfig(
         system_instruction=System_instrunction,
         temperature=0.2,
         top_p=0.95,
         candidate_count=2),
        
    )
    st.write(response.text)


#page setup 
st.set_page_config(page_title="code helper")
st.header("🧠 Code Helper")
st.markdown("""this is a sample to :rainbow[debug],:rainbow[explain] or :rainbow[enhance] your code .....can check [linkdin profile](www.linkedin.com/in/ashutosh-sahu-979459326)""")

input=st.text_area("paste your code here",height=250)




mode = st.sidebar.radio("Choose an action", ["🔍 Debug", "📖 Explain", "⚙️ Enhance"])#add on





if input and mode=="🔍 Debug":
    with st.spinner("Analyzing your code..."):
     debugging(input)
    st.balloons()
elif input  and mode=="📖 Explain":
    with st.spinner("Analyzing your code..."):
     explaination(input)
     st.snow()
elif input  and mode=="⚙️ Enhance":
    with st.spinner("Analyzing your code..."):
     enhancement(input)
    st.balloons()



#streamlit run extension.py
