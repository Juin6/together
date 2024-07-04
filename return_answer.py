
class Answer:
    # 1, 2, 3, 4 각 지표 결과
    inno1 = ''
    inno2 = ''
    inno3 = ''
    inno4 = ''

    def __init__(self, type_score):
        if type_score['R'] >= type_score['T']:
            self.inno1 = 'R'
        else:
            self.inno1 = 'T'

        if type_score['C'] >= type_score['F']:
            self.inno2 = 'C'
        else:
            self.inno2 = 'F'

        if type_score['J'] >= type_score['M']:
            self.inno3 = 'J'
        else:
            self.inno3 = 'M'

        if type_score['A'] >= type_score['N']:
            self.inno4 = 'A'
        else:
            self.inno4 = 'N'
        
    def get_answer(self):
        return self.inno1 + self.inno2 + self.inno3 + self.inno4

# 테스트용 예시

test_score = {
    'R': 1,
    'T': 2,
    'C': 3,
    'F': 4,
    'J': 100,
    'M': 10,
    'A': 7,
    'N': 7,
}

# 결과 출력

answer = Answer(test_score)
print(answer.get_answer())