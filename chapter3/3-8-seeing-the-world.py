visit = ['ireland', 'new zealand', 'france', 'germany', 'hawaii']

print(visit)

## Alphabetical Sort
print(sorted(visit))

print(visit)

## Reverse Alphabetical Sort
print(sorted(visit, reverse=True))

print(visit)

## Reverse

visit.reverse()
print(visit)

## Reverse again to revert to original
visit.reverse()
print(visit)

## Permanently Sort
visit.sort()
print(visit)

## Permanently Reverse Sort
visit.sort(reverse=True)
print(visit)
