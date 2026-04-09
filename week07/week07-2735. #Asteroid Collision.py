735. Asteroid Collision
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for ast in asteroids:
            if ast > 0: #正的往右 不跟左相撞
                ans.append(ast) #直接塞入
            else:
                while ans and ans[-1] > 0 and abs(ast) > ans[-1]: #目前有存 且最右邊正的 向右 會相撞 ans中數值比ast小
                    ans.pop() #被消滅了 吐掉
                if ans and ans[-1] > 0 and abs(ast) == ans[-1]: #目前有存 且最右邊正的 向右 會相撞 兩個行星數值一樣
                    ans.pop() #被消滅了 吐掉
                    continue #因為數值一樣所以也被消滅 所以直接下一個

                if ans and ans[-1] > 0 and abs(ast) < ans[-1]: #目前有存 且最右邊正的 向右 會相撞 ans中數值比ast大
                    continue #因為ast比ans小 所以被消滅 直接下一個
                ans.append(ast)

        return ans