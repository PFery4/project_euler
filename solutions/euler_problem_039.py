"""
https://projecteuler.net/problem=39
"""


def get_triangles(p):
    """
    generates the list of valid triangles for perimeter of length p
    """
    triangles = []
    c = p // 2
    while c > 1:
        ab = p - c
        for a in range(1, ab//2):
            b = ab - a
            if a * a + b * b == c * c:
                triangles.append((a, b, c))
        c -= 1
    return triangles


def solution():
    best_p = 120
    num_p = 3

    for p in range(1, 1001):
        num_trial = len(get_triangles(p))
        if num_trial > num_p:
            num_p = num_trial
            best_p = p
    return best_p


if __name__ == "__main__":
    print(solution())
