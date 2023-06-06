import os
import PyPDF2
import openai

# Function to read a PDF file
def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(reader.getNumPages()):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text

# Function to read a text file
def read_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

# Function to interact with OpenAI API
def interact_with_openai(text, query):
    openai.api_key = 'YOUR API KEY'
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": query},
            {"role": "assistant", "content": text}
        ]
    )
    return response['choices'][0]['message']['content']

# Determine the type of the file (PDF or text)
def determine_file_type(file_path):
    _, ext = os.path.splitext(file_path)
    if ext.lower() == '.pdf':
        return 'pdf'
    elif ext.lower() == '.txt':
        return 'text'
    else:
        return None

# Main part of the script
def process_file():
    file_path = input("Please enter the filename: ")
    query = input("Please enter your query: ")
    file_type = determine_file_type(file_path)
    if file_type == 'pdf':
        text = read_pdf(file_path)
    elif file_type == 'text':
        text = read_text(file_path)
    else:
        print(f'Unsupported file type: {file_path}')
        return

    response = interact_with_openai(text, query)
    print(response)

# Usage
process_file()