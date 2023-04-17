# RipVersion_Text_Generator
```
프트 립버전 1.16 다운과 결혼하게 되었고 본인이 노리던 대로 시우의 첫 스타크래프트 립버전 1.16다운이둘과 관계를 가진 덕분인지 공식적으로 아이겸 첫 아들도찾아갔을땐 얼마 지나지도 않았는데 점성술

물품엔 비싼게문제까지 겹쳐서 귀여운 여동생같은 느낌으로만 인식되는 중. 그래도 시우와 스타크래프트 립버전 1.16 다운굶주리고 있었다(...). 결국 시우에게 다시 식사를 대접받

은 뒤 상행에감우와 서로 언쟁으로 물어뜯었고 그래도 자신이 낳는데 성공했다. 정치적 입지를자신또한 자신의 마음을 왜 남들 배려하느라 포기해야비우는데, 어디까지나 자신처럼 마음의 정

리라도 시켜주려있는 근거를 찾았다며 이 당시 시우의모나와 종종 대립하긴 했지만 본인의 중2병 기질에 시우의입찰 경쟁이 끝난 후, 응광의 호출로 그녀와의 대화를 통해루미네와

결탁해 복귀, 이전보다 더 적극적으로 시우에게 다가간다.이후리월 상행을 떠나고자 할때 호위로지인이라고 생각했던 '헤일리'라는 여성에게 배신당해 목숨을 위협받을때 스타크래프트 립버

전 1.16 다운이야기를 나누자 한발 물러서는 태도를 보였었다. 스타크래프트 립버전 1.16 다운있으며, 자신과 시우 사이에 오해가 있었다는 것을 전해 듣는다. 스타크래프트 립버전

1.16 다운것과 티바트 대륙쪽으로 기울여지던 그의관계를 망설이고 있었기 때문에 피슬과 루미네가 이 일에 대해 서로 스타크래프트 립버전 1.16 다운얘기하면서 과거의 묵

은 감정을 해소하고,자기 자신을 제대로 봐줄려는 그의 스타크래프트 립버전 1.16 다운반해버렸다. 이때문에 개인적인 입맞춤을 하는등 여러 가지로 진도를 빼고시우를 그냥 평범한 고용인으로 여겼으나 다른
```

### 사용법
1. 소스 텍스트를 충분히 준비하여 data 폴더의 original.txt에 넣습니다.
2. 넣을 문구를 data 폴더의 target.txt에 넣습니다.
3. main.py를 실행합니다.
4. data 폴더에 output.txt에 결과물이 출력됩니다.


### 파라미터 설명

```
PATH_ORIGINAL_TEXT = "data/original.txt"    // 원본 문장 파일 경로
PATH_TARGET_TEXT = "data/target.txt"        // 타겟 문장 파일 경로
PATH_OUTPUT = "data/output.txt"             // 출력 문장 파일 경로
MIN_CORPUS_SIZE = 5                         // 최소 문장 단위
DELETE_RATE = 0.1                           // 랜덤 단어 삭제 빈도 [0 ~ 0.5]
TARGET_RATE = 0.3                           // 타겟 문장 포함 빈도 [0, 1)
PER_LINE_SIZE = 100                         // 출력 줄당 글자 개수
TOTAL_LINE = 8                              // 출력 줄 개수
```



### TroubleShooting
- **"Original text length is not enough for generating output text."**
> 원본 텍스트를 충분히 넣어주세요. 최소 PER_LINE_SIZE*TOTAL_LINE 개 이상의 글자를 넣어야 합니다.

> ex. PER_LINE_SIZE (줄당 글자 개수) = 100이고, TOTAL_LINE (줄 수) = 8 이면, 100 * 8 = 800자 이상 필요

- **"Parameters are not valid."**
> 파라미터가 유효하지 않습니다.

- **"File not exist."**
> 파일이 존재하지 않습니다.경로를 다시 확인해주세요.



### TODO
- 값 유효성 체크
- target text 여러 줄에도 대응
- web으로 실행 가능하도록
