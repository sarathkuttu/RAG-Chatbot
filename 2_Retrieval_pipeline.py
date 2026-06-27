from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

persist_directory = "db/chroma_db"

# Load embeddings and vector store
embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")

db = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding_model,
    collection_metadata={"hnsw:space": "cosine"}
)

# Search for relevant documents
query = "How many monthly active users does Facebook have?"

retriever = db.as_retriever(search_kwargs={"k": 3})

# Alternative retriever configuration
# retriever = db.as_retriever(
#     search_type="similarity_score_threshold",
#     search_kwargs={
#         "k": 5,
#         "score_threshold": 0.3  # Only return chunks with cosine similarity >= 0.3
#     }
# )

relevant_docs = retriever.invoke(query)

print(f"User Query: {query}")

print(f"\nRetrieved {len(relevant_docs)} documents\n")


# Combine the query and the relevant document contents
combined_input = f"""Based on the following documents, please answer this question: {query}

Documents:
{chr(10).join([f"- {doc.page_content}" for doc in relevant_docs])}

Please provide a clear, helpful answer using only the information from these documents. If you can't find the answer in the documents, say no data in the document provided.
"""

# # Create a ChatOpenAI model
# model = ChatOpenAI(model="gpt-4o")

# # Define the messages for the model
# messages = [
#     SystemMessage(content="You are a helpful assistant."),
#     HumanMessage(content=combined_input),
# ]

# # Invoke the model with the combined input
# result = model.invoke(messages)

# # Display the full result and content only
# print("\n--- Generated Response ---")
# # print("Full result:")
# # print(result)
# print("Content only:")
# print(result.content)

# for i, doc in enumerate(relevant_docs, start=1):
#     print(f"----- Document {i} -----")
#     print(f"Source: {doc.metadata['source']}")
#     print()
#     print(doc.page_content)
#     print("-" * 80)

# Store our conversation as messages
chat_history = []


def ask_question(user_question):

    print(f"\n--- You asked: {user_question} ---")

    # Step 1: Make the question clear using conversation history
    if chat_history:

        # Ask AI to make the question standalone
        messages = [
            SystemMessage(
                content="Given the chat history, rewrite the new question as a standalone question."
            )
        ] + chat_history + [
            HumanMessage(content=f"New question: {user_question}")
        ]

        result = model.invoke(messages)
        search_question = result.content.strip()

        print(f"Searching for: {search_question}")

    else:
        search_question = user_question

    # Step 2: Find relevant documents
    retriever = db.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(search_question)

    print(f"Found {len(docs)} relevant documents:")

    for i, doc in enumerate(docs, 1):

        # Show first 2 lines of each document
        lines = doc.page_content.split("\n")[:2]
        preview = "\n".join(lines)

        print(f"Doc {i}: {preview}...")

    # Step 3: Create final prompt
    combined_input = f"""
Based on the following documents, please answer this question: {user_question}

Documents:
{"\n".join([f"- {doc.page_content}" for doc in docs])}

Please provide a clear, helpful answer using only the information from these documents.
If you can't find the answer in the documents, say you don't know.
"""

    # Step 4: Get the answer
    messages = [
        SystemMessage(
            content="You are a helpful assistant that answers questions based on provided documents and conversation history."
        )
    ] + chat_history + [
        HumanMessage(content=combined_input)
    ]

    result = model.invoke(messages)
    answer = result.content

    # Step 5: Remember this conversation
    chat_history.append(HumanMessage(content=user_question))
    chat_history.append(AIMessage(content=answer))

    print(f"Answer: {answer}")

    return answer

# Simple chat loop

def ask_question(query):

    # Retrieve relevant documents
    retriever = db.as_retriever(search_kwargs={"k": 3})
    relevant_docs = retriever.invoke(query)

    # Combine retrieved documents
    combined_input = f"""
Based on the following documents, please answer this question:

Question: {query}

Documents:
{chr(10).join([doc.page_content for doc in relevant_docs])}

Please answer using only the information provided above.
"""

    # Create GPT model
    model = ChatOpenAI(model="gpt-4o")

    # Create messages
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content=combined_input)
    ]

    # Get response
    result = model.invoke(messages)

    # Print answer
    print("\nAnswer:")
    print(result.content)
    
def start_chat():
    print("Ask me questions! Type 'quit' to exit.")

    while True:
        question = input("\nYour question: ")

        if question.lower() == "quit":
            print("Goodbye!")
            break

        ask_question(question)


if __name__ == "__main__":
    start_chat()