def solution(survey, choices):
    answer = ''
    return answer

    type_score = {'A': 0,
    "T": 0,
    "C" :0,
    "F" :0,
    "J" :0,
    "M" :0,
    "A" :0,
    "N" :0,
    }
    my_survey = []
    for i in survey:
        tem_list = [[i[0], 3], [i[0], 2], [i[0], 1], 0, [i[1], 1], [i[0], 2], [i[0], 3]]

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
    

solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])