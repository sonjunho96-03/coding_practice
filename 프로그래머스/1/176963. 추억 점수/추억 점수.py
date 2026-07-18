def solution(name, yearning, photo):
    answer = []

    for one_photo in photo:
        photo_score = 0

        for person in one_photo:
            if person in name:
                pos = name.index(person)
                photo_score += yearning[pos]

        answer.append(photo_score)

    return answer