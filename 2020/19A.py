f = open('Input/19.txt')

raw_rules, raw_messages = f.read().split('\n\n')

rules = {}
for raw_rule in raw_rules.splitlines():
    parts = raw_rule.split(' ')
    if '"' in parts[1]:
        rule = ([parts[1].strip('"')],)
    elif '|' in parts[1:]:
        pipe_location = parts.index('|')
        rule = (parts[1:pipe_location], parts[pipe_location + 1:])
    else:
        rule = (parts[1:],)
    rules[parts[0][:-1]] = rule

cache = {}

def cache_matches(message, rule, depth = 0):
    in_cache = message in cache
    if in_cache:
        if rule in cache[message][True]:
            return True
        elif rule in cache[message][False]:
            return False
    result = matches(message, rule, depth)
    if in_cache:
        cache[message][result].append(rule)
    else:
        cache[message] = {result: [rule], (not result): []}
    return result

def matches(message, rule, depth = 0):
    # print('  ' * depth, message, rule)
    depth += 1
    # lowest level, has to match totally
    if type(rule) == str:
        if rule in 'ab':
            return message == rule
        else:
            return cache_matches(message, rules[rule], depth)
    # mid level, has to match both parts put together
    elif type(rule) == list:
        if len(rule) == 1:
            return cache_matches(message, rule[0], depth)
        elif len(rule) == 2:
            for split_point in range(1, len(message)):
                if cache_matches(message[:split_point], rule[0], depth) and cache_matches(message[split_point:], rule[1], depth):
                    return True
            return False
        else:
            for split_point_1 in range(1, len(message) - 1):
                for split_point_2 in range(split_point_1, len(message)):
                    if cache_matches(message[:split_point], rule[0], depth) and cache_matches(message[split_point:], rule[1], depth):
                        return True
            return False
    # highest level, has to match either part
    else:
        for sub_rule in rule:
            if cache_matches(message, sub_rule, depth):
                return True
        return False

total_matches = 0

for message in raw_messages.splitlines():
    print("\n" + message, end = ": ")
    is_a_match = cache_matches(message, '0')
    total_matches += is_a_match
    print(is_a_match)

# for rule, values in cache.items():
#     print(rule, values)

print("answer:", total_matches)
