"""
백준
1,2,3 더하기 4
https://www.acmicpc.net/problem/15989

어려웠다. DP 형태의 식을 세워서 접근을 하였는데 순서가 다른
합은 같은걸로 친다는 조건을 만족하는 방법을 찾지 못 했다.
이 조건의 뜻은 순서만 다른 숫자들의 조합은 중복으로 간주해
하나만 세어 주어야한다.

처음 식은 f(n) = f(n-1) + f(n-2) + f(n-3)
이렇게 작성해보았다. 즉 n 은 n-1 의 조합에 1을 더 한 결과
더하기 n-2 의 조합에 2를 더 한 결과 더하기 n-3 의 조합에 3을
더 한 결과들의 합이다.

하지만 이건 중복되는 조합을 잡아내지 못한다.
풀이 방법을 참고했다. 결론은 임의의 숫자 n 에 대하여 1,2,3 을
사용한 결과 값을 따로 저장해주고 해당 숫자로 조합을 만들 때 그 숫자보다
큰 수의 경우는 고려하지 않는 방법이다. 이렇게 하면 덧셈 식의 숫자 조합이 
오름차순이 되는 경우를 (예: 1 + 1 + 2 + 3) 유지하며 경우를 셀 수 있다.

f(n) = f(n-1) + f(n-2) + f(n-3) 식을 어느정도 사용 할 수 있지만 정확히 
표현하자면 f(n-1) 을 만드는 조합 중 1 만 사용한 조합의 수 더하기
f(n-2) 을 만드는 조합 중 1 과 2 만 사용한 조합의 수 더하기
f(n-3) 을 만드는 조합 중 1, 2, 3 모두 사용한 조합의 수를 합산한 값이 된다.

가장 직관적으로는 2D 배열을 만들어서 행은 1에서 n 까지의 숫자, 열은 1, 2, 3 으로
만들어 각각 해당하는 값을 저장한다. 예를 들어 배열[4][2] 은 4 를 만드는 경우 중 2
를 사용해서 만들수 있는 경우의 수, 더 정확히는 합산식이 2로 끝나는 경우.
4를 2를 써서 만든다는 것은 2 (즉 4-2) 를 만드는 경우 중 1하고 2만 사용해서 만드는 경우의 수가 된다.
즉 배열[2][1] + 배열[2][2] 가 된다.

좀 더 메모리 사용 효율을 높이고 싶다면 1차원 배열로도 가능하다. 각 숫자 i 에 대한
경우의 수는 배열[i] 가 된다고 할 때, 1 만 사용하여 만들 수 있는 경우의 수를 세고
그 다음 2 그리고 마지막으로 3 을 사용하여 만들 수 있는 경우의 수를 차례로 합산하면
중복을 없애는 효과를 그대로 낼 수 있다.
"""
import sys

def solution(n):
    if n < 4:
        return n
    memo = [1 for _ in range(n + 1)]
    for i in range(2, n+1):
        memo[i] += memo[i-2]
    for i in range(3, n+1):
        memo[i] += memo[i-3]
    return memo[n]

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        n = int(sys.stdin.readline().strip())
        print(solution(n))
