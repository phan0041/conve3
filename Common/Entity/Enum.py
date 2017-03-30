# -*- coding: utf-8 -*-
from enum import Enum


class CITY(Enum):
    SGN = 1
    HCM = 2
    HAN = 3
    OTHER = 4

    def label(self):
        label_list = [
             "", "Singapore", u"Hồ Chí Minh", u"Hà Nội", u"Nơi khác"
        ]

        return label_list[self.value]


class CATEGORY(Enum):
    Dry = 1
    Wet = 2
    Other = 3

    def label(self):
        label_list = [
            "", u"Đồ khô", u"Đồ ướt", u"Không phải thực phẩm"
        ]

        return label_list[self.value]


class REQUEST_STATUS(Enum):
    Active = 1
    Closed = 2
    Expired = 3
    Deleted = 4

    def label(self):
        label_list = [
            "", u"Đang hoạt động", u"Đã đóng", u"Đã hết hạn", u"Đã xóa"
        ]
        return label_list[self.value]


class CURRENCY(Enum):
    SGD = 1
    VND = 2

    def label(self):
        return self.name

