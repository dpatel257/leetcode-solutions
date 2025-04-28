class Solution:
    mem = {}
    def climbStairs(self, n: int) -> int:

        if n in self.mem:
            return self.mem.get(n)
        if n == 0 or n == 1 or n == 2:
            self.mem[n] = n
            return n
        val =  self.climbStairs(n-1) + self.climbStairs(n-2)
        self.mem[n] = val
        return val
