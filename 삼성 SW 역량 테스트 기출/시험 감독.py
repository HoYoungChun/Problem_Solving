N = int(input())
people_cnts = list(map(int, input().split()))
B,C = map(int, input().split())

ans = 0 
for people_cnt in people_cnts: # 1,000,000
  # 총감독관
  ans+=1
  people_cnt -= B
  
  # 부감독관
  if people_cnt > 0:
    quotient, remainder = divmod(people_cnt, C)
    ans += quotient
    if remainder: # 나머지가 0이 아니면
      ans+= 1

print(ans)
