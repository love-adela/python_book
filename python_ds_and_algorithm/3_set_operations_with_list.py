def remove_duplicate(lst):
    ''' 리스트의 중복된 항목을 제거한 후 리스트 형태로 반환한다.'''
    return list(set(lst))


def intersection(lst1, lst2):
    ''' 교집합 결과를 리스트 형태로 반환한다.'''
    return list(set(lst1) & set(lst2))


def union(lst1, lst2):
    ''' 합집합 결과를 리스트 형태로 반환한다.'''
    return list(set(lst1) | set(lst2))


def test_sets_operations_with_lists():
    lst1 = [1, 2, 3, 4, 5, 5, 9, 11, 15]
    lst2 = [4, 5, 6, 7, 8]
    lst3 = []
    assert remove_duplicate(lst1) == [1, 2, 3, 4, 5, 9, 11, 15]
    assert intersection(lst1, lst2) == [4, 5]
    assert union(lst1, lst2) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 15]
    assert remove_duplicate(lst3) == []
    assert intersection(lst3, lst2) == lst3
    assert sorted(union(lst3, lst2)) == sorted(lst2)
    print('Test 통과')


if __name__ == '__main__':
    test_sets_operations_with_lists()

