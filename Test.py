class Test:
    def __init__(self):
        pass
        # self.date = UIData()
        # self.date.set_btn_back_state(True).set_btn_cancel_match_state(True).set_light_state(True)
        # print(self.date.btn_cancel_match_state)

    def combin_lst(self, lst_a, lst_b):
        len_b = len(lst_b)
        min_a = lst_a[0]
        max_b = lst_b[len_b - 1]
        if min_a >= max_b:
            lst_b.extend(lst_a)
            return lst_b

        len_a = len(lst_a)
        min_b = lst_b[0]
        max_a = lst_a[len_a - 1]
        if min_b >= max_a:
            lst_a.extend(lst_b)
            return lst_a

        result = []
        index_a, index_b = 0, 0
        while len(result) < len_a + len_b:

            if index_a >= len_a:
                result.append(lst_b[index_b])
                break

            if index_b >= len_b:
                result.append(lst_a[index_a])
                break

            if lst_a[index_a] > lst_b[index_b]:
                result.append(lst_b[index_b])
                index_b += 1
            else:
                result.append(lst_a[index_a])
                index_a += 1

            print("result len {0}  index a {1}  index b {2}".format(len(result), index_a, index_b))

        return result
