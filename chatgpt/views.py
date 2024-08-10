

# 환경 변수에서 API 키 가져오기

from django.shortcuts import render 
from django.http import JsonResponse 
import openai
import os
from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')


# API 키 불러오기
openai.api_key = os.getenv('OPENAI_API_KEY')
def get_completion(prompt):
    # 프롬프트를 출력하여 디버깅에 도움을 줍니다.
    print(f"Prompt: {prompt}")

    try:
        # OpenAI Chat API 호출
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # 사용할 모델 이름
            messages=[
                {'role': 'user', 'content': prompt}  # 사용자 메시지 설정
            ],
            max_tokens=1024,  # 최대 토큰 수
            n=1,  # 생성할 응답 수
            temperature=0.5,  # 생성된 응답의 창의성 조정
        )

        # API 응답에서 내용 추출
        message = response['choices'][0]['message']['content']
        print(f"Response: {message}")

        return message

    except Exception as e:
        # 예외 발생 시 오류 메시지 반환
        print(f"Error: {e}")
        return str(e)


def query_view(request): 
	if request.method == 'POST': 
		prompt = request.POST.get('prompt') 
		prompt=str(prompt)
		response = get_completion(prompt)
		return JsonResponse({'response': response}) 
	return render(request, 'index.html') 
