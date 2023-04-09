def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:  # check for expected format
        if '-' in s:
            raise ValueError

        if not ' to ' in s.lower():
            raise ValueError

        # split time to start and end
        s = s.upper().split('TO')
        times = [elem.strip() for elem in s]
        hours = []

        for period in times:
            if ':' in period:  # check time format with or without minutes
                h, m = period.split(':')
                if int(h) > 12:  # check valid hours
                    raise ValueError
                else:
                    if m.endswith(' PM'):  # convert to 24 format
                        if h == '12':  # esp case for 12PM
                            h = int(h)
                        else:
                            h = int(h) + 12
                        m = m.strip(' PM')

                    else:
                        if h == '12':  # esp case for 12AM
                            h = 00
                        else:
                            h = int(h)  # leave time as it was
                        m = m.strip(' AM')
                    if int(m) >= 60:  # check valid minutes
                        raise ValueError
            else:
                if ' PM' in period:
                    h = period.strip(' PM')  # convert to 24 hours format
                    if int(h) > 12:  # check valid hours
                        raise ValueError
                    else:
                        if h == '12':  # esp case for 12PM
                            h = 12
                        else:
                            h = int(h) + 12
                else:
                    h = period.strip(' AM')
                    if h == '12':  # esp case for 12AM
                        h = 00
                    else:
                        h = int(h)
                m = '00'  # add minutes anyway

            a = f'{int(h):02d}:{m}'  # format to the expected format
            hours.append(a)

        return f'{hours[0]} to {hours[1]}'

    except ValueError:
        raise ValueError



if __name__ == "__main__":
    main()