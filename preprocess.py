import json
# import re
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm



def process_posts(raw_file_path,processsed_file_path="data/processed_posts.json"):
    enriched_posts = []
    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)

        for post in posts:
            metadata = extract_metadata(post['text'])
            post_with_metadata = post | metadata
            enriched_posts.append(post_with_metadata)

    for epost in enriched_posts:
        print(epost)

#
# def clean_text(text):
#     # Remove invalid surrogates
#     return text.encode("utf-8", "ignore").decode("utf-8", "ignore")


def extract_metadata(post):
    post = clean_text(post)  # sanitize before using in template
    template = '''
    You are given a Linkedin post. You need to extract number of lines,language of the post and tags.
    1.Return a valid JSON. No preamble.
    2.Json object should have exactly three keys: line_count, language and tags.
    3.tags is an array of text tags. Extract maximum two tags.
    4.Language should be English or hinglish (Hinglish means hindi + english)
    
    Here is the actual post on which you need to perform this task:
    {post}
    '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input ={'post':post})

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")
    return res


if __name__ == "__main__":
    process_posts("data/raw_posts.json","data/processed_posts.json")