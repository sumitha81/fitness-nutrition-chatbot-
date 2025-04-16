# 📦 Step 1: Install required packages (uncomment and run this once)
# !pip install openai pinecone requests

# 📂 Step 2: Imports and API Keys
import openai
from pinecone import Pinecone
import requests

# 🔑 Set your API keys here
openai.api_key = "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"
pinecone_api_key = "pcsk_USPhh_Wx4i4Pt3gx5UUXd28NLBkeGabENmqrPP5ekEWbzJV96Yci7m3iQZfCCEhzBfoR"
news_api_key = "ac24fdf8a3164c1e9f2e8b19277a9109"

# 🧠 Step 3: Initialize Pinecone
pc = Pinecone(api_key=pinecone_api_key)
index_name = "interview-prep"

# Create index if not exists
if index_name not in pc.list_indexes().names():
    pc.create_index(name=index_name, dimension=1536, metric="cosine")

# Connect to the index
index = pc.Index(index_name)

# 🗃️ Step 4: User memory functions using Pinecone
def store_user_context(user_id, context_dict):
    vector_id = f"user-{user_id}"
    metadata = {k: str(v) for k, v in context_dict.items()}
    index.upsert(vectors=[{"id": vector_id, "values": [0.0] * 1536, "metadata": metadata}])

def get_user_context(user_id):
    vector_id = f"user-{user_id}"
    result = index.fetch(ids=[vector_id])
    return result["vectors"][vector_id]["metadata"] if vector_id in result["vectors"] else {}

# 🌐 Step 5: Real-time company news using News API
def get_company_news(company_name):
    url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey={news_api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        return ["Error fetching news."]
    articles = response.json().get("articles", [])[:3]
    return [f"{a['title']} - {a['source']['name']}" for a in articles]

# 🧠 Step 6: Generate interview coaching response using OpenAI
def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert AI interview coach helping job seekers with personalized advice."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# 🤖 Step 7: Main chatbot function
def handle_user_query(user_id, user_input):
    context = get_user_context(user_id)

    if "update profile" in user_input.lower():
        # Example static context for now; in practice, extract this from user_input
        new_context = {
            "career_background": "Data Analyst, 3 years",
            "target_roles": "Data Scientist",
            "skills": "Python, SQL, Machine Learning",
            "companies": "Google, Microsoft",
            "interview_experience": "2 FAANG interviews",
        }
        store_user_context(user_id, new_context)
        return "✅ Your profile has been updated."

    elif "news about" in user_input.lower():
        company = user_input.split("about")[-1].strip()
        news = get_company_news(company)
        return f"📰 Latest on {company}:\n\n" + "\n".join(news)

    else:
        prompt = f"""Here is the user's context: {context}
Now respond to their question with personalized interview coaching:
Question: {user_input}"""
        return generate_response(prompt)

# 🧪 Step 8: Test the chatbot
user_id = "user123"

# 🛠️ Update profile example
print(handle_user_query(user_id, "Update profile: I'm a backend engineer applying to fintech startups."))

# 🔍 Company news example
print(handle_user_query(user_id, "What are the latest news about Stripe?"))

# 🎤 Interview question example
print(handle_user_query(user_id, "How should I answer leadership questions for a Stripe interview?"))

# 📦 Step 1: Install required packages (uncomment and run this once)
# !pip install openai pinecone requests

# 📂 Step 2: Imports and API Keys
import openai
from pinecone import Pinecone
import requests

# 🔑 Set your API keys here
openai.api_key = "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"
pinecone_api_key = "pcsk_USPhh_Wx4i4Pt3gx5UUXd28NLBkeGabENmqrPP5ekEWbzJV96Yci7m3iQZfCCEhzBfoR"
news_api_key = "ac24fdf8a3164c1e9f2e8b19277a9109"

# 🧠 Step 3: Initialize Pinecone
pc = Pinecone(api_key=pinecone_api_key)
index_name = "interview-prep"

# Create index if not exists
if index_name not in pc.list_indexes().names():
    pc.create_index(name=index_name, dimension=1536, metric="cosine")

# Connect to the index
index = pc.Index(index_name)

# 🗃️ Step 4: User memory functions using Pinecone
def store_user_context(user_id, context_dict):
    vector_id = f"user-{user_id}"
    metadata = {k: str(v) for k, v in context_dict.items()}
    index.upsert(vectors=[{"id": vector_id, "values": [0.0] * 1536, "metadata": metadata}])

def get_user_context(user_id):
    vector_id = f"user-{user_id}"
    result = index.fetch(ids=[vector_id])
    return result["vectors"][vector_id]["metadata"] if vector_id in result["vectors"] else {}

# 🌐 Step 5: Real-time company news using News API
def get_company_news(company_name):
    url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey={news_api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        return ["Error fetching news."]
    articles = response.json().get("articles", [])[:3]
    return [f"{a['title']} - {a['source']['name']}" for a in articles]

# 🧠 Step 6: Generate interview coaching response using OpenAI
def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert AI interview coach helping job seekers with personalized advice."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# 🤖 Step 7: Main chatbot function
def handle_user_query(user_id, user_input):
    context = get_user_context(user_id)

    if "update profile" in user_input.lower():
        # Example static context for now; in practice, extract this from user_input
        new_context = {
            "career_background": "Data Analyst, 3 years",
            "target_roles": "Data Scientist",
            "skills": "Python, SQL, Machine Learning",
            "companies": "Google, Microsoft",
            "interview_experience": "2 FAANG interviews",
        }
        store_user_context(user_id, new_context)
        return "✅ Your profile has been updated."

    elif "news about" in user_input.lower():
        company = user_input.split("about")[-1].strip()
        news = get_company_news(company)
        return f"📰 Latest on {company}:\n\n" + "\n".join(news)

    else:
        prompt = f"""Here is the user's context: {context}
Now respond to their question with personalized interview coaching:
Question: {user_input}"""
        return generate_response(prompt)

# 🧪 Step 8: Test the chatbot
user_id = "user123"

# 🛠️ Update profile example
print(handle_user_query(user_id, "Update profile: I'm a backend engineer applying to fintech startups."))

# 🔍 Company news example
print(handle_user_query(user_id, "What are the latest news about Stripe?"))

# 🎤 Interview question example
print(handle_user_query(user_id, "How should I answer leadership questions for a Stripe interview?"))
