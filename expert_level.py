def exp_max_level(N, M, Ai, Bi):
	rivals = [(Ai[i], Bi[i]) for i in range(N)]
	rivals.sort()
	expert_lev = M

	for a, b in rivals:
		if expert_lev >= a:
			expert_lev += b

		else:
			break

	return expert_lev


N = 5
M = 9
Ai = [2, 3, 6, 7, 8]
Bi = [3, 4, 2, 2, 3]

print(exp_max_level(N, M, Ai, Bi))
