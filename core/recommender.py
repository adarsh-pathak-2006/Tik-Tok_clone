from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)

def get_recommended_videos(user_interests, videos):
    """
    user_interests: string like "funny cats"
    videos: list of Video objects
    """
    prompt = f"User likes: {user_interests}\nChoose top 3 videos from the list: {[v.title for v in videos]}"
    response = llm(prompt)
    # Parse the response to match Video objects
    recommended_titles = [t.strip() for t in response.split(',')]
    return [v for v in videos if v.title in recommended_titles]