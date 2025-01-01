class Solution:
  def rev_bubble(self, num, ele):
    pass_count = 0
    for i in range(num):
      for j in range(1, num-i-1):
        if ele[j] < ele[j+1]:
          ele[j] = ele[j+1]
          ele[j+1] = ele[j]
          pass_count += 1
    return pass_count + 1

if __name__ == '__main__':
  sol = Solution()
  num = int(input().strip())
  ele = list(map(int, input().strip().split()))
  print(sol.rev_bubble(num, ele))
  