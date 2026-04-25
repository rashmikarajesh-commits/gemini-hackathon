import google.generativeai as genai

# 1. Setup with your key
genai.configure(api_key="PASTE_YOUR_API_KEY_HERE")

# 2. Using the model we found in your list earlier
model = genai.GenerativeModel('gemini-3-flash-preview')

print("✨ GEN-Z STUDY SLAY IS ONLINE ✨")

# 3. Input section
user_text = input("\nPaste boring text: ")

# 4. The prompt logic
prompt = f"Explain this like a Gen-Z influencer with slang and emojis. 3 bullet points: {user_text}"

print("\n⏳ Slaying... please wait...")

try:
    # 5. Running the AI
    response = model.generate_content(prompt)
    print("\n🔥 THE SLAY-MARY:")
    print(response.text)
except Exception as e:
    print(f"\n❌ Error: {e}")