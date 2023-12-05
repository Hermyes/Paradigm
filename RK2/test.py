import unittest
from RK1 import streets, houses, houses_on_streets, main


class TestRK1Functions(unittest.TestCase):
    def test_task_E1(self):
        expected_result = [
            ('Улица Луговая, 3', 2000, 'Улица Луговая'),
            ('Улица Луговая, 10', 1905, 'Улица Луговая')
        ]
        one_to_many = [(h.address, h.houseCreatingYear, s.name)
                       for s in streets
                       for h in houses
                       if h.street_id == s.id]
        filtered_result = list(filter(lambda i: i[2].find('Луговая') != -1, one_to_many))
        self.assertEqual(filtered_result, expected_result)


    def test_task_E2(self):
        expected_result = [
            ('Улица Кринжовая', 2123.0),
            ('Улица Герасимовская', 2005.0),
            ('Улица Маслянная', 2023.0)
        ]
        one_to_many = [(h.address, h.houseCreatingYear, s.name)
                       for s in streets
                       for h in houses
                       if h.street_id == s.id]
        res_12_unsorted = []
        for s in streets:
            street_house = list(filter(lambda i: i[2] == s.name, one_to_many))
            if len(street_house) > 0:
                s_year = [houseCreatingYear for _, houseCreatingYear, _ in street_house]
                s_year_sum = round(sum(s_year) / len(street_house), 2)
                res_12_unsorted.append((s.name, s_year_sum))

        res_12 = sorted(res_12_unsorted, key=lambda x: x[1], reverse=True)
        self.assertEqual(res_12, expected_result)


    def test_task_E3(self):
        expected_result = [
            ('Улица Гениальная, 45', 2005, 'Улица Гениальная'),
            ('Улица Герасимова, 205', 1998, 'Улица Герасимовская'),
            ('Улица Герасимова 303', 2017, 'Улица Герасимовская'),
            ('Улица Маслянная 76', 2023, 'Улица Маслянная')
        ]
        many_to_many_temp = [(s.name, hos.street_id, hos.house_id)
                             for s in streets
                             for hos in houses_on_streets
                             if s.id == hos.street_id]
        many_to_many = [(h.address, h.houseCreatingYear, street_name)
                        for street_name, street_id, house_id in many_to_many_temp
                        for h in houses if h.id == house_id]
        filtered_result = list(filter(lambda i: i[0].find('Г') != -1, many_to_many))
        self.assertEqual(filtered_result, expected_result)


if __name__ == '__main__':
    unittest.main()
