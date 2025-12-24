from langchain_core.prompts import ChatPromptTemplate
from langchain_oci.chat_models import ChatOCIGenAI
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("""Translate the following text into French. 
If the text is a question, first translate the question 
and then answer the question in French.: {text}""")

llm = ChatOCIGenAI(
    model_id="openai.gpt-oss-20b",
    service_endpoint="https://inference.generativeai.us-chicago-1.oci.oraclecloud.com",
    compartment_id="ocid1.tenancy.oc1..aaaaaaaaxie5xno3zeoxdwobc4n4yfusalie4n7hvwtq7qlfmo2wyh764j3q",
    model_kwargs={"temperature": 0, "max_completion_tokens": 500},
    auth_type="SECURITY_TOKEN",
    auth_profile="DEFAULT",
    auth_file_location="/Users/amitchawla/.oci/config",
    # provider="cohere"

)


# OCI_COMPARTMENT_ID = os.environ.get("OCI_COMPARTMENT_ID")
# OCI_ENDPOINT = os.environ.get("OCI_SERVICE_ENDPOINT")
# OCI_CHAT_MODEL = os.environ.get("OCI_CHAT_MODEL", "cohere.command-r-08-2024")
# OCI_EMBED_MODEL = os.environ.get("OCI_EMBED_MODEL", "cohere.embed-english-v3.0")
#
# llm = ChatOCIGenAI(model_id=OCI_CHAT_MODEL, service_endpoint=OCI_ENDPOINT, compartment_id=OCI_COMPARTMENT_ID, model_kwargs={"temperature": 0.1, "max_tokens": 2500})

output_parser = StrOutputParser()

chain = prompt | llm | output_parser
input_data = {"text": "What are the four seasons in a year?"}

result = chain.invoke(input_data)
print(result)