from django.shortcuts import render

# Create your views here.
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

openai.api_key = 'my key'

@csrf_exempt
def generate_strategy(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        description = data.get('description', '')
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは教育戦略立案の専門家です。"},
                {"role": "user", "content": f"以下の詳細を基に教育機関向けの戦略プランを作成してください: {description}"}
            ],
            max_tokens=4000
        )
        strategy_text = response.choices[0].message['content'].strip()
        return JsonResponse({'strategy': strategy_text})
    return JsonResponse({'error': 'Invalid request method'}, status=400)