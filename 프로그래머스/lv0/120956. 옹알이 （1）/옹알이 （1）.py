def solution(babbling):
    answer = 0

    for string in babbling:
        while is_pronounceable(string):
            string = string[len(is_pronounceable(string)):]

        if len(string) == 0:
            answer += 1

    return answer


def is_pronounceable(string):
    baby = ['aya', 'ye', 'woo', 'ma']

    for word in baby:
        if string.find(word) == 0:
            return word

    return False