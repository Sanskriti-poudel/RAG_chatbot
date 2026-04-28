from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

def build_rag_chain(vectorstore):

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    pipe = pipeline(
        "text-generation",
        model="google/flan-t5-base",
        max_length=256
    )

    llm = HuggingFacePipeline(pipeline=pipe)

    prompt_template = """
    You are an AI assistant.
    Answer the question clearly and concisely in 1-2 sentences.
    Use only the given context.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )

    return qa_chain