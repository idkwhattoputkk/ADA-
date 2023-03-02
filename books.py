def can_assign_books(pages, k, max_pages_per_scriber):
    num_scribers = 1
    pages_assigned = 0
    for p in pages:
        if p > max_pages_per_scriber:
            return False
        if pages_assigned + p <= max_pages_per_scriber:
            pages_assigned += p
        else:
            num_scribers += 1
            pages_assigned = p
            if num_scribers > k:
                return False
    return True

def assign_books(pages, k):
    left, right = max(pages), sum(pages)
    while left <= right:
        mid = (left + right) // 2
        if can_assign_books(pages, k, mid):
            right = mid - 1
        else:
            left = mid + 1
    result = []
    pages_assigned = 0
    num_scribers = 1
    for p in pages:
        if len(result) < k - 1 and pages_assigned + p > left:
            result.append('/')
            pages_assigned = p
            num_scribers += 1
        else:
            pages_assigned += p
        result.append(str(p))
    while len(result) < len(pages) + k - 1:
        result.append('/')
        result.append(str(pages[-1]))
    return ' '.join(result)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        m, k = map(int, input().split())
        pages = list(map(int, input().split()))
        print(assign_books(pages, k))
