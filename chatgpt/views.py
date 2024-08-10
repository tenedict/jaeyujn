# 환경 변수에서 API 키 가져오기

from django.shortcuts import render 
from django.http import JsonResponse 
import openai
import os

openai.api_key = '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'
#앞서 자신이 부여받은 API key를 넣으면 된다. 절대 외부에 공개해서는 안된다.

def get_completion(prompt): 
	print(prompt) 
	query = openai.ChatCompletion.create( 
		model="gpt-3.5-turbo",
		messages=[
        	{'role':'user','content': prompt}
    	], 
		max_tokens=1024, 
		n=1, 
		stop=None, 
		temperature=0.5, 
	) 
	response = query.choices[0].message["content"]
	print(response) 
	return response 


def query_view(request): 
	if request.method == 'POST': 
		prompt = request.POST.get('prompt') 
		prompt=str(prompt)
		response = get_completion(prompt)
		return JsonResponse({'response': response}) 
	return render(request, 'index.html') 
