def solution(survey, choices):
    answer = ''

    type_score = {'R': 0,
    "T": 0,
    "C" :0,
    "F" :0,
    "J" :0,
    "M" :0,
    "A" :0,
    "N" :0,
    }

    def testman(x ,num):
        if num == 1:
            type_score[x[0]] += 3
        elif num == 2:
            type_score[x[0]] += 2
        elif num == 3:
            type_score[x[0]] += 1
        elif num == 5:
            type_score[x[1]] += 1
        elif num == 6:
            type_score[x[1]] += 2
        elif num == 7:
            type_score[x[1]] += 3
    
    for i in range(len(survey)):
        testman(survey[i], choices[i])
    
    class Answer:
         # 1, 2, 3, 4 각 지표 결과
        inno1 = ''
        inno2 = ''
        inno3 = ''
        inno4 = ''

        # 생성자(type_score) => 지표별 결과 산정
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

    a1 = Answer(type_score)
    answer = a1.get_answer()
    
    return answer