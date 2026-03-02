class Solution(object):
    def destCity(self, paths):
        cities = set()

        # Thu thập tất cả các thành phố xuất phát (điểm đi)
        for path in paths:
            cities.add(path[0])

        # Tìm thành phố đích không có đường đi tiếp (không nằm trong tập điểm đi)
        for path in paths:
            dest = path[1]
            if dest not in cities:
                return dest

        return ""