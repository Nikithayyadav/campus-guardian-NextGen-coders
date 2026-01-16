from openai import OpenAI
import os

client = OpenAI(api_key="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")

def analyze(emergency, lat, lng):
    prompt = f"""
A student sent an emergency SOS.

Type: {emergency}
Latitude: {lat}
Longitude: {lng}

Give:
1) Risk level (Low, Medium, High)
2) One-line danger message for the campus security team
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a campus safety AI."},
                {"role": "user", "content": prompt}
            ],
            timeout=15,
        )
        return response.choices[0].message.content
    except Exception:
        # Fallback so your app never crashes
        return f"Risk: High\nMessage: {emergency} reported at ({lat}, {lng}). Immediate security response recommended."
