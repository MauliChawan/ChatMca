from django.shortcuts import render
import openai

openai.api_key = os.getenv('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')  # Replace with your OpenAI API key

def chat_view(request):
    response_text = ''
    user_input = ''
    
    if request.method == 'POST':
        user_input = request.POST.get('message')
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=500
            )
            response_text = response['choices'][0]['message']['content']
        except Exception as e:
            response_text = f"Error: {str(e)}"

    return render(request, 'chatbot/chat.html', {
        'response': response_text,
        'user_input': user_input
    })
