def solution(board):
    safe = 0
    n = len(board)
    dirs = [(-1, -1), (-1, 0), (-1, 1), 
           (0, -1), (0, 1), 
           (1, -1), (1, 0), (1, 1)]
    
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                continue
            is_safe = True
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if 0 <= nr < n and 0 <= nc < n:
                    if board[nr][nc] == 1:
                        is_safe = False
                        break
                        
            if is_safe:
                safe += 1
    return safe