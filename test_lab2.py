import lab_2

def test_find_min_max():
    expected_results = [1, 6]
    test_list = [1, 6, 4, 3, 5, 2]
    result = lab_2.find_min_max(test_list)
    assert (result == expected_results)

def test_calc_average():
    test_list = [1, 6, 4.245, 3, 5, 2]
    expected_list = 3.540833333
    result = lab_2.calc_average(test_list)
    assert (round(result, 4) == round(expected_list, 4))

def test_median_temp():
    test_list = [1, 6, 4, 3, 5, 2]
    expected_result = 3.5
    result = lab_2.calc_median_temp(test_list)
    assert (result == expected_result)