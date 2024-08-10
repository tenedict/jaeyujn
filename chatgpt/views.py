

from django.shortcuts import render 
from django.http import JsonResponse 
import openai
import os
# .env 파일에서 환경 변수 로드하기
load_dotenv()

# 환경 변수에서 API 키 가져오기
openai.api_key = os.getenv('OPENAI_API_KEY')
# OpenAI의 GPT-3.5 모델을 사용하여 프롬프트에 대한 응답을 생성하는 함수
def get_completion(prompt):
    print(prompt)  # 디버깅 용도로 프롬프트를 출력합니다.

    # OpenAI의 ChatCompletion API를 호출하여 응답을 생성합니다.
    query = openai.ChatCompletion.create(
        model="gpt-4o",  # 사용할 모델 지정
        messages=[
            {'role': 'user', 'content': prompt}  # 사용자의 프롬프트를 메시지로 전달
        ],
        max_tokens=1024,  # 응답에서 생성할 최대 토큰 수
        n=1,  # 생성할 응답의 개수
        stop=None,  # 응답 생성을 멈추기 위한 토큰 (없음)
        temperature=0.5,  # 응답의 창의성 조절 (0.0~1.0 사이의 값)
    )

    # API 응답에서 첫 번째 응답의 콘텐츠를 추출합니다.
    response = query.choices[0].message["content"]
    print(response)  # 디버깅 용도로 응답을 출력합니다.

    return response  # 생성된 응답을 반환합니다.

# POST 요청으로 들어오는 프롬프트를 처리하고 응답을 반환하는 Django 뷰
def query_view(request):
    if request.method == 'POST':  # 요청이 POST일 때만 처리
        # POST 요청에서 'prompt' 파라미터를 가져옵니다.
        prompt = request.POST.get('prompt')

        # 프롬프트를 문자열로 변환합니다. (불필요할 수 있음)
        prompt = str(prompt)

        # 프롬프트를 사용하여 응답을 생성합니다.
        response = get_completion(prompt)

        # 생성된 응답을 JSON 형태로 반환합니다.
        return JsonResponse({'response': response})

    # GET 요청이나 다른 HTTP 메소드일 때는 'index.html' 템플릿을 렌더링합니다.
    return render(request, 'index.html')