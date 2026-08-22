class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = str(n)
        z = 0
        pro = 1
        for i in a:
            val = int(i)
            z=z+val
            pro = pro*val

        total = z + pro

        if n%total == 0 :
            return True
        else :
            return False
        