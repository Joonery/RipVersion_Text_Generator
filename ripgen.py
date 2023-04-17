
# 기본 알고리즘

# 전체 텍스트를 하나의 문자열 변수로 합친다.
# 거기로부터 n size의 window로 랜덤 추출해서 concat. (이걸 언제까지 반복하냐면, 총 길이가 line * perlinelen 이 넘기 전까지.)
# 이때, 그 가져온 window를 특정 확률로 랜덤한 어절을 삭제한다.
# 랜덤한 확률로 뒤에 타겟 텍스트를 삽입한다.
# 생성된 하나의 긴 문장을 라인 단위로 나눈다.

import random as rd

class RIPVERSION_TEXT_GENERATOR :

    def __init__(self, original_text_path, target_text_path, output_text_path, min_corpus_size=5, delete_rate=0.1, target_rate=0.1, per_line_size=100, total_line=8) -> None:

        # 내부 파라미터들
        self.paths = {
            "ORIGINAL_TEXT" : original_text_path,
            "TARGET_TEXT" : target_text_path,
            "OUTPUT_TEXT" : output_text_path,
        }
        self.min_corpus_size = min_corpus_size
        self.delete_rate = delete_rate
        self.target_rate = target_rate
        self.per_line_size = per_line_size
        self.total_line = total_line


        self.enough_size = 1

        # 아웃풋
        self.original_text = ""
        self.target_text = ""
        self.final_text = ""

        # 에러 타입
        self.errors = {
            "SHORT_ORIGINAL_TEXT" : "Original text length is not enough for generating output text.",
            "NOT_VALID_PARAMETERS" : "Parameters are not valid.",
            "NOT_EXISTING_FILE" : "File not exist.",
        }

    # 가장 빠른 concat
    def _fast_concat(self, target_list) :
        return "".join([ele.strip() for ele in target_list])

    # original_text를 불러온다.
    def _load_data(self) :
        
        try :
            with open(self.paths["ORIGINAL_TEXT"], "r", encoding="UTF8") as f :
                
                # 불러온다.
                self.original_text = self._fast_concat(f.readlines())
                self.enough_size += self.delete_rate / (len(self.original_text) - self.delete_rate)  # 계산해봤더니 1개씩 삭제할 경우 삭제율에 따라 1 + p/(N-p) 배보다 더 여유가 필요함.

                # 이때, 총 사이즈가 생성하려는 문장의 enough배가 넘지 않으면
                if (len(self.original_text) <  self.per_line_size * self.total_line * self.enough_size ) :
                    self._print_log(self.errors["SHORT_ORIGINAL_TEXT"])
                    return 0
                
                self.original_text = self.original_text.split()

            with open(self.paths["TARGET_TEXT"], "r", encoding="UTF8") as f :
                self.target_text = f.readline() # todo : 여기가 항상 단문이라는 보장이 있는지?

        except FileNotFoundError :
            self._print_log(self.errors["NOT_EXISTING_FILE"])
            return 0


        return 1

    # todo : 파라미터 보여주기
    def __repr__(self) -> str:
        return "RIP VERSION TEXT GENERATOR OBJECT\n\
            "

    # 출력
    def _print_log(self, log) :
        print(log)


    # min_corpus_size 어절의 문장 생성 
    def _parse_line(self, corpus_size) -> str :
        
        true_corpus_size = rd.randint(corpus_size, corpus_size*2)
        entry_idx = rd.randint(0, len(self.original_text) - true_corpus_size) # todo : 여기 위험. 뽑으려는 위치의 엔트리 포인트가 -가 될 수 도 있음. 일단 오리지널 텍스트 사이즈를 크게 해서 이 문제를 해결해놨는데 미봉책이긴 함. 삭제율을 너무 크게 올릴 경우에는 작동 안할수도 있음. 삭제율과 관계를 보고 결정해야 함.
        result = []

        # 빼서 concat
        for i in range(true_corpus_size) :
            result.append(self.original_text.pop(entry_idx)) 

        return result

    def _export_data(self) :

        all_lines = []
        startidx = endidx = 0

        # 라인 횟수만큼
        for i in range(self.total_line) :            
            endidx += self.per_line_size
            if (i+1 == self.total_line) : all_lines.append(self.final_text[startidx:])
            else : all_lines.append(self.final_text[startidx:endidx])
            startidx = endidx

        with open(self.paths["OUTPUT_TEXT"], "w", encoding="UTF8") as f :
            for line in all_lines :
                f.write(line + "\n\n")

    def _is_valid_params(self) :

        if (self.delete_rate < 0 or self.delete_rate > 0.5) :
            self._print_log(self.errors["NOT_VALID_PARAMETERS"])
            return 0
        
        if (self.target_rate < 0 or self.target_rate >= 1) :
            self._print_log(self.errors["NOT_VALID_PARAMETERS"])
            return 0

        return 1

    def run(self) :
        
        # 파라미터 체크
        if not self._is_valid_params() :
            return

        # 전체 텍스트를 불러와 하나의 문자열 변수로 합친다.
        if not self._load_data() :
            return
        
        # 총 길이가 line * perlinelen 이 넘기 전까지
        while (len(self.final_text) < self.per_line_size * self.total_line) :
            
            # 거기로부터 n size의 window로 랜덤 추출
            parsed_line = self._parse_line(self.min_corpus_size)

            
            # target_rate 확률만큼 뒤에 타겟 텍스트를 삽입.
            if ( rd.random() < self.target_rate ) :
                parsed_line.append(self.target_text)


            # 특정 확률로 가져온 window에서 랜덤한 어절을 하나 삭제한다.
            if ( rd.random() < self.delete_rate ) :
                parsed_line.pop(rd.randint(0, len(parsed_line)-1))

            # concat.
            self.final_text += " ".join(parsed_line)


        # 생성된 하나의 긴 문장을 라인 단위로 나누어 출력한다.
        self._export_data()
        
        self._print_log("Done!")

    






if __name__ == "__main__" :
    
    PATH_ORIGINAL_TEXT = "data/original.txt"
    PATH_TARGET_TEXT = "data/target.txt"
    PATH_OUTPUT = "data/output.txt"
    MIN_CORPUS_SIZE = 5
    DELETE_RATE = 0.5
    TARGET_RATE = 0.5
    PER_LINE_SIZE = 100
    TOTAL_LINE = 8

    # txtt = method6()
    # print(txtt)

    generator = RIPVERSION_TEXT_GENERATOR(PATH_ORIGINAL_TEXT, PATH_TARGET_TEXT, PATH_OUTPUT, MIN_CORPUS_SIZE, DELETE_RATE, TARGET_RATE, PER_LINE_SIZE, TOTAL_LINE)
    generator.run()
    # print(generator.original_text)