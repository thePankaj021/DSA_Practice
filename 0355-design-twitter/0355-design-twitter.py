from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)      # userId -> [(time, tweetId)]
        self.following = defaultdict(set)    # userId -> set(followeeId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int):
        heap = []

        self.following[userId].add(userId)

        for followee in self.following[userId]:
            tweets = self.tweets[followee]

            if tweets:
                idx = len(tweets) - 1
                time, tweetId = tweets[idx]
                heapq.heappush(heap, (-time, tweetId, followee, idx - 1))

        res = []

        while heap and len(res) < 10:
            neg_time, tweetId, followee, idx = heapq.heappop(heap)
            res.append(tweetId)

            if idx >= 0:
                time, nextTweet = self.tweets[followee][idx]
                heapq.heappush(heap, (-time, nextTweet, followee, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.following[followerId].discard(followeeId)