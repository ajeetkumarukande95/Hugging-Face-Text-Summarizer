import gradio as gr
from transformers import pipeline
# model- google-t5/t5-small
# task - summarization

# Function to perform summarization
def summarize_text(text):
    try:
        summerizer = pipeline('summarization', model='google-t5/t5-small')
        summarized_text = summerizer(text)[0]['summary_text']
        return summarized_text
    except Exception as e:
        return str(e)

# Create Gradio interface
input_text = gr.Textbox(lines=10, label="Input Text", placeholder="Enter text to summarize...")
output_text = gr.Textbox(label="Summarized Text", placeholder="Summarized text will appear here...")

# Author information
author = "Ajeetkumar Ukande"

# Create Gradio interface
interface = gr.Interface(summarize_text, inputs=input_text, outputs=output_text, 
             title="<div style='color: #336699; font-size: 24px; font-weight: bold; border: 2px solid #336699; padding: 10px; border-radius: 10px;'>Text Summarizer</div>", 
             description=f"""<div style='color: #666666; font-family: Arial, sans-serif;'>
                             <p style='margin-top: 10px;'>Enter some text and get it summarized.</p>
                             <p>Developed by <span style='color: #336699; font-weight: bold;'>{author}</span>.</p>
                             </div>""", 
             theme="default" # Change theme to default
           
             )

# Deploy the interface to Hugging Face Spaces
interface.launch(share=True, debug=True)
