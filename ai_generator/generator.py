import openai
import os
from .seo_fetcher import fetch_seo_metrics

def generate_blog_post(keyword):
    seo_data = fetch_seo_metrics(keyword)
    prompt = f"""
You are a seasoned content strategist and subject matter expert. Your task is to create an in-depth, research-backed blog post about: **{keyword}**.

## CRITICAL: First, analyze the keyword type and intent:
- **Product/Tool**: Focus on practical applications, comparisons, real-world use cases
- **Concept/Topic**: Provide educational depth, context, industry insights
- **Person/Brand**: Offer biographical context, achievements, impact, current relevance
- **Problem/Solution**: Address pain points, methodologies, step-by-step guidance

## SEO Context (use strategically, don't force):
- Search Volume: {seo_data['search_volume']} monthly searches
- Keyword Difficulty: {seo_data['keyword_difficulty']}/100
- Average CPC: ${seo_data['avg_cpc']}

## Content Requirements:

### 1. Strategic Structure (Dynamic Based on Keyword)
Create 4-6 main sections that are SPECIFIC to your keyword. Avoid generic headings like "What is X?" or "Benefits of X". Instead, craft sections that reflect:
- Current industry trends or recent developments
- Specific challenges or opportunities in this space
- Advanced techniques or lesser-known insights
- Real-world applications or case studies

### 2. Research Depth & Authority
- Include specific statistics, studies, or data points (you may reference general industry knowledge)
- Mention relevant industry experts, companies, or authoritative sources
- Provide historical context or evolution of the topic where relevant
- Address common misconceptions or advanced considerations

### 3. Audience-Centric Value
- Target readers who already have basic familiarity with the topic
- Provide actionable insights they can't easily find elsewhere
- Include practical tips, frameworks, or methodologies
- Address intermediate to advanced questions, not just beginner FAQs

### 4. Content Formatting
- Use Markdown with strategic heading hierarchy (# ## ###)
- Include bullet points for complex information
- Add relevant examples, scenarios, or mini case studies
- Use **bold** for key concepts and *italics* for emphasis
- **IMPORTANT**: Include 2-3 affiliate link placeholders naturally within the content using the format `{{{{AFF_LINK_1}}}}`, `{{{{AFF_LINK_2}}}}`, etc. Place these where you would naturally recommend tools, products, or resources related to the topic.

### 5. Tone & Style
- Expert but accessible writing style
- Confident assertions backed by reasoning
- Avoid fluff words and generic statements
- Write for professionals or serious enthusiasts in this space

## Content Structure Template:

```markdown
# [Compelling, Specific Title - Not Generic]

## Introduction
[2-3 sentences that immediately establish your expertise and the specific angle you're taking. Avoid basic definitions.]

## [Section 1: Current Landscape/Trends/Recent Developments]
[Industry-specific insights, recent changes, market dynamics]

## [Section 2: Advanced Strategies/Methodologies/Deep Dive]
[Technical depth, professional techniques, insider knowledge]
[When mentioning tools or resources, use: {{{{AFF_LINK_1}}}}]

## [Section 3: Practical Implementation/Case Studies/Real-World Applications]
[Specific examples, actionable frameworks, proven approaches]
[When recommending products or services, use: {{{{AFF_LINK_2}}}}]

## [Section 4: Common Challenges/Solutions/Advanced Considerations]
[Address pain points, troubleshooting, advanced considerations]

## [Section 5: Future Outlook/Emerging Opportunities/Next Steps]
[Forward-looking insights, emerging trends, strategic recommendations]

## Conclusion
[Synthesize key insights and provide clear next steps for readers]
```

**REMEMBER**: Naturally integrate {{{{AFF_LINK_1}}}}, {{{{AFF_LINK_2}}}}, and {{{{AFF_LINK_3}}}} when discussing tools, products, or resources that would be helpful to readers.
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
        markdown_content = response.choices[0].message.content
        for i in range(1, 6):
            markdown_content = markdown_content.replace(f"{{{{AFF_LINK_{i}}}}}", f"https://example.com/affiliate-link-{i}")
        aff_count = 1
        while '[Affiliate Link Here]' in markdown_content:
            markdown_content = markdown_content.replace('[Affiliate Link Here]', f'https://example.com/affiliate-link-{aff_count}', 1)
            aff_count += 1
        return markdown_content
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return "Error generating blog post." 