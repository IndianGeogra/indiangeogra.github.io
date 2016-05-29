#!/usr/bin/python
# -*- coding: utf-8 -*-

class Comic():
    def __init__(self, comic_number, comic_name, comic_data, comic_orientation, is_last=False, is_first=False):
        self.nr = comic_number
        self.prev_nr = self.nr - 1
        self.next_nr = self.nr + 1
        self.name = comic_name
        self.data = comic_data
        if comic_orientation in ['v','h']:
            self.orientation = comic_orientation
        else:
            raise TypeError('Comic orientation must be either' + \
                            "'h' (horizontal) or 'v' (vertical). Given: " + \
                            comic_orientation + '.')
        self.is_first = is_first
        self.is_last = is_last


info_data = [\
             Comic(1,  u'Daria 2016', '160107', 'h', False, True),
             Comic(2,  u'Окололетнее' , '160212', 'h'),
             Comic(3,  u'Ходячий замок Хаула', '160129', 'v'),
             Comic(4,  u'А.', '160215', 'h'),
             Comic(5,  u'Случай в Мадриде', '160218', 'v'),
                       
             Comic(6,  u'По дороге', '160216', 'v'),
             Comic(7,  u'Ведьма', '150817', 'v'),
             Comic(8,  u'Фонари зажигаются', '150813', 'v'),
             Comic(9,  u'Март', '150301', 'h'),
             Comic(10, u'Часы', '******', 'v'),
                       
             Comic(11, u'Городская геодезия', '150303', 'v'),
             Comic(12, u'На работу', '150303', 'h'),
             Comic(13, u'Друзья', '150302', 'v'),
             Comic(14, u'Рынок', '**07**', 'v'),
             Comic(15, u'The Jerk', '160304', 'h'),
                       
             Comic(16, u'В городе моем', '160304', 'h'),
             Comic(17, u'Ботинки, мечтающие о чашке чая', '******', 'v'),
             Comic(18, u'Мумий Тролль', '160305', 'h'),
             Comic(19, u'Москва-река', '160306', 'h'),
             Comic(20, u'Зима уходит', '160315', 'v'),
                       
             Comic(21, u'Meryl', '160311', 'v'),
             Comic(22, u'Флейтистка', '160319', 'v'),
             Comic(23, u'Китайская фантазия', '14****', 'v'),
             Comic(24, u'Размытый город', '1511**', 'h'),
             Comic(25, u'Качели', '150324', 'h'),
                       
             Comic(26, u'Средиземноморье', '151220', 'h'),
             Comic(27, u'Конец марта', '160320', 'v'),
             Comic(28, u'Depeche Mode', '151129', 'h'),
             Comic(29, u'До Драмтеатра', '160325', 'v'),
             Comic(30, u'Мост', '160325', 'h'),

             Comic(31, u'В подворотне', '130416', 'h'),
             Comic(32, u'Даль', '****13', 'h'),
             Comic(33, u'Конец апреля', '150416', 'v'),
             Comic(34, u'Караоке', '200416', 'h'),
			 Comic(35, u'Улитка на склоне Фудзи', '150516', 'h', True)
]

number_of_comics = len(info_data)
# Adjust previous and next numbers for the first and for the last comic
info_data[0].prev_nr = 1
info_data[-1].next_nr = info_data[-1].nr








