import re
import urllib.parse
import pandas as pd

regex_log_dict = {
    'user': re.compile(r' user=(?P<user>.*)\n'),
    'ip_list': re.compile(r' rhost=([0-9]+\.[0-9]+\.[0-9]+\.[0-9])(?P<ip_string>.*)\n'),
}




def _parse_line(lines):
    """
    Do a regex search against all defined regexes and
    return the key and match result of the first matching regex

    """
    auth_log_dict = {}
    auth_log_list = []
    new_list = []
    date_wise_dict = {}
    count = 1
    for line in lines:
        d = {}
        date = line[0:6]
        new_line = str(line).strip()
        if " user=" in new_line and " rhost=" in new_line:
            if " user=" in new_line and regex_log_dict.get('user'):
                match_ = regex_log_dict.get('user').search(str(line))
                match = match_.group(1).strip().split(' ')[-1].split('=')[-1]
            if " rhost=" in new_line and regex_log_dict.get('ip_list'):
                match_ = regex_log_dict.get('ip_list').search(str(line))
                if match_:
                    match1 = match_.group(1).strip().split(' ')[0]

            if match and match1:
                if len(auth_log_list) == 0:
                    d.setdefault(date, {}).setdefault(match, {})['IPLIST'] = match1
                    d.setdefault(date, {}).setdefault(match, {})['total_count'] = count
                    if d:
                        auth_log_list.append(d)
                else:
                    for auth_rec in auth_log_list:
                        if date in auth_rec:
                            if match in auth_rec.get(date):
                                if auth_rec.get(date).get(match).get('IPLIST') == match1:
                                    count += 1
                                    auth_rec.get(date).get(match)['total_count'] = count

                                else:
                                    count = 1
                                    auth_rec.get(date).get(match)['IPLIST'] = match1
                                    auth_rec.get(date).get(match)['total_count'] = count
                        else:
                            d.setdefault(date, {}).setdefault(match, {})['IPLIST'] = match1
                            d.setdefault(date, {}).setdefault(match, {})['total_count'] = count
                            if d:
                                auth_log_list.append(d)

    return auth_log_list


def parse_file(filepath):
    final_list = []
    with open(filepath, 'r') as file_object:
        lines = file_object.readlines()
    file_object.close()
    if lines:
        lines = [ln for ln in lines]
        # date = ln[0:6]
        final_list = _parse_line(lines[1:6])
    print(final_list)
    return final_list


if __name__ == '__main__':
    filepath = 'auth.log'
    data = parse_file(filepath)
