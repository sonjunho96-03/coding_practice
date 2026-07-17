def solution(players, callings):
    positions = {}

    # 각 선수가 현재 몇 번 위치에 있는지 저장
    for i in range(len(players)):
        positions[players[i]] = i

    # 불린 선수를 바로 앞 선수와 교환
    for called_player in callings:
        called_index = positions[called_player]
        front_index = called_index - 1

        front_player = players[front_index]

        players[front_index] = called_player
        players[called_index] = front_player

        positions[called_player] = front_index
        positions[front_player] = called_index

    answer = players
    return answer