from collections import deque
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter_map = {}
        start_r, start_c = -1, -1
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_map[(r, c)] = len(litter_map)
                    
        num_litter = len(litter_map)
        target_mask = (1 << num_litter) - 1
        max_energy_at_state = {}
        queue = deque([(start_r, start_c, 0, energy, 0)])
        max_energy_at_state[(start_r, start_c, 0)] = energy
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c, mask, curr_energy, moves = queue.popleft()
            if mask == target_mask:
                return moves
            
            if curr_energy == 0 and classroom[r][c] != 'R':
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_energy = curr_energy - 1
                    next_mask = mask
                    
                    if classroom[nr][nc] == 'R':
                        next_energy = energy
                    elif classroom[nr][nc] == 'L':
                        next_energy = max(next_energy, 0)
                        next_mask |= (1 << litter_map[(nr, nc)])
                    else:
                        next_energy = max(next_energy, 0)
                    
                    state_key = (nr, nc, next_mask)
                    if next_energy > max_energy_at_state.get(state_key, -1):
                        max_energy_at_state[state_key] = next_energy
                        queue.append((nr, nc, next_mask, next_energy, moves + 1))
                        
        return -1
