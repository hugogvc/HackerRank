if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    
    scores = [s for s in arr] 
    
    scores = sorted(list(set(scores)))
    
    score_vice = scores[(len(scores) -2)]
    
    print(score_vice)