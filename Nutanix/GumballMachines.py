# https://leetcode.com/discuss/interview-question/416158/Nutanix-or-OA-2020-or-Grumpy-Bookstore-Owner-and-Gumball-Machines

def gum_ball(n, colors):
	d = {}
	cost = 0
	for color in colors:
		if len(d) == 3 and color not in d:
			min_key = get_min_key(d)
			cost += d[min_key]
			del d[min_key]
		d[color] = 1000
		for key in d:
			d[key] -= 10
	return cost/100

def get_min_key(d):
	return min(d, key = lambda k: d[k])

n1 = 5
colors1 = ['red', 'green', 'blue', 'red', 'white']
n2 = 2
colors2 = ['red', 'red']

print(gum_ball(n1, colors1))
print(gum_ball(n2, colors2))