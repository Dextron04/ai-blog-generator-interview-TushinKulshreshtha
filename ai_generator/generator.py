import openai
import os
from .seo_fetcher import fetch_seo_metrics

def generate_blog_post(keyword):
    seo_data = fetch_seo_metrics(keyword)
    prompt = f"""
You are an expert blog writer and SEO content strategist. Your task is to generate a high-quality, SEO-optimized blog post in **Markdown** format for the keyword: **{keyword}**.

Use the following SEO data:
- **Search Volume**: {seo_data['search_volume']} monthly searches
- **Keyword Difficulty**: {seo_data['keyword_difficulty']} (scale 0–100)
- **Average CPC**: ${seo_data['avg_cpc']}

### Requirements:

1. **Output Format**: Return the blog post in valid **Markdown**.
2. **Title**: Start with a strong, catchy blog post title (use `# Title` format).
3. **Introduction**:
   - Brief overview (2–3 sentences).
   - Mention the keyword naturally.
   - Make it engaging and informative.
4. **Headings & Structure**:
   - Use `##` and `###` Markdown headings.
   - Include at least 3 sections with relevant subheadings.
   - Naturally include answers to questions like:
     - What is {keyword}?
     - Why is it important?
     - How to choose or use it effectively?
5. **Use of the Keyword**:
   - Mention the keyword multiple times (3–6x) naturally.
   - Include related keywords or phrases (synonyms, variations).

6. **Affiliate Links**:
   - Insert **two** clearly marked `[Affiliate Link Here]` placeholders.
   - Example: `👉 [Buy the top-rated product here](Affiliate Link Here)`

7. **Conclusion**:
   - Brief summary and final thoughts.
   - Encourage action or further reading.

8. **Markdown Best Practices**:
   - Use bullet points or numbered lists where helpful.
   - Use bold (`**text**`) or italic (`*text*`) formatting for emphasis.
   - Avoid raw HTML.
   - Keep paragraphs short and scannable.

9. **Tone & Readability**:
   - Friendly, helpful, expert tone.
   - Target audience: curious readers, online shoppers, or blog subscribers.
   - Avoid jargon unless explained.

Return **only** the markdown content—no extra explanation or chat.

Begin now.
"""
    api_key = os.getenv("OPENAI_API_KEY")
    client = openai.OpenAI(api_key=api_key)
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return "Error generating blog post." 