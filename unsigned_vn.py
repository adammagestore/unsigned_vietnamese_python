#!/usr/bin/env python
# Reference: https://sangnd.wordpress.com/2014/01/03/python-chuyen-tieng-viet-co-dau-thanh-khong-dau/

import re
import sys

patterns = {
    '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
    '[đ]': 'd',
    '[èéẻẽẹêềếểễệ]': 'e',
    '[ìíỉĩị]': 'i',
    '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
    '[ùúủũụưừứửữự]': 'u',
    '[ỳýỷỹỵ]': 'y'
}


def convert(vn_text):
    """
    Convert from 'Tieng Viet co dau' thanh 'Tieng Viet khong dau'
    text: input string to be converted
    Return: string converted
    """
    output = vn_text
    for regex, replace in patterns.items():
        print(regex);
        print(replace);
        
        output = re.sub(regex, replace, output)
        # deal with upper case
        output = re.sub(regex.upper(), replace.upper(), output)
    return output

if __name__ == '__main__':
    print(convert("Xin Chào Việt Nam"))