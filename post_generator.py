from  llm_helper import llm

def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"


def generate_post(length, language, tag):
    length_str = get_length_str(length)

    prompt = f'''
    Generate a Linkedin post using the below information. No preamble.
    
    1) Topic: {tag}
    2) Length: {length}
    3) Language: {language}
    The script for the generated post should always be English.
    '''

    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    post = generate_post("Short", "English", "Job Search")
    print(post)