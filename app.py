
import gradio as gr

from rag_chain import create_rag_chain
from vector_store import create_vector_store

print("Initializing Eleven Madison Park Assistant...")

vector_store = create_vector_store()
rag_chain = create_rag_chain(vector_store)

print("Assistant is ready!")

def ask_elevenmadison_assistant(question):

    try:
        #Sending the question to RAG chain
        result = rag_chain.invoke({"question": question})
        answer = result["answer"]
        source_documents = result["source_documents"]
        unique_sources = {}

        for doc in source_documents:
            source = doc.metadata.get("source", "Unknown source")
            title = doc.metadata.get("title", "Untitled page")

            unique_sources[source] = title

      
        sources = "\n".join(
            f"{title}: {url}"
            for url, title in unique_sources.items()
        )

        return answer, sources

    except Exception as e:
        print(f"Error: {e}")
        return (
            "Sorry, something went wrong while processing your question.",
            ""
        )



with gr.Blocks(
    theme=gr.themes.Soft(),
    title="EMP Q&A Assistant"
) as demo:

    # Title and description
    gr.Markdown(
        """
        # Eleven Madison Park - AI Q&A Assistant 💬

        Ask questions about the restaurant based on its website data.

        The AI provides answers and cites the source documents.

        *(Examples: What are the menu prices? Who is the chef?
        Is it plant-based?)*
        """
    )

    # Input component
    question_input = gr.Textbox(
        label="Your Question:",
        placeholder="e.g., What are the opening hours on Saturday?",
        lines=2
    )

    # Output components
    with gr.Row():

        answer_output = gr.Textbox(
            label="Answer:",
            interactive=False,
            lines=6
        )

        sources_output = gr.Textbox(
            label="Sources:",
            interactive=False,
            lines=6
        )

    # Buttons
    with gr.Row():

        submit_button = gr.Button(
            "Ask Eleven Madison Park AI 🤖",
            variant="primary"
        )

        clear_button = gr.ClearButton(
            components=[
                question_input,
                answer_output,
                sources_output
            ],
            value="Clear All"
        )

    # Example questions
    gr.Examples(
        examples=[
            "What are the different menu options and prices?",
            "Who is the head chef?",
            "What is Magic Farms?",
            "Do I need a reservation for the bar?",
            "What is the dress code?",
            "Can I buy gift cards?"
        ],
        inputs=question_input,
        cache_examples=False
    )

    # Connect the button to our RAG function
    submit_button.click(
        fn=ask_elevenmadison_assistant,
        inputs=question_input,
        outputs=[
            answer_output,
            sources_output
        ]
    )


print("Gradio interface defined.")

if __name__ == "__main__":

    print("\nLaunching Gradio app...")

    demo.launch()
