class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_id = {s: i for i, s in enumerate(req_skills)}
        dp = {0: []}

        for i, person in enumerate(people):
            mask = 0
            for skill in person:
                if skill in skill_id:
                    mask |= 1 << skill_id[skill]

            new_dp = dp.copy()

            for state, team in dp.items():
                new_state = state | mask

                if (new_state not in new_dp or
                    len(new_dp[new_state]) > len(team) + 1):
                    new_dp[new_state] = team + [i]

            dp = new_dp

        return dp[(1 << len(req_skills)) - 1]