from typing import Dict, List


def dfs_recursive(G: Dict[int, List[int]], s: int) -> List[int]:
    visited = []

    def dfs_serach(G: Dict[int, List[int]], s: int, visited: List[int]):
        visited.append(s)
        if s in G.keys():
            for i in G[s]:
                if i not in visited:
                    dfs_serach(G, i, visited)
                else:
                    return False

    print(dfs_serach(G, s, visited))

    return visited
