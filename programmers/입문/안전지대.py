dr = [0, 0, 1, 1, 1, -1, -1, -1]
dc = [1, -1, 0, 1, -1, 0, 1, -1]

def solution(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for d in range(8):
                    nr, nc = i + dr[d], j + dc[d] 
                    if 0 <= nr < n and 0 <= nc < n:
                        if board[nr][nc] == 0:
                            board[nr][nc] = 2
                            
    answer = 0
    for i in range(n):
        answer += board[i].count(0)
    return answer