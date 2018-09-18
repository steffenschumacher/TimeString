import re
import datetime

class TimeString(object):
    string_time_re = re.compile(r'(((?P<years>\d+)y)|((?P<weeks>\d+)w)|((?P<days>\d+)d)|((?P<hours>\d+)h)){1,2}')

    @staticmethod
    def convert(value):
        """
        Converts either timestring (1y2w etc) to timedelta, or timedelta(or hours as int) to timestring
        :param value:
        :return:
        """
        if isinstance(value, str):
            return TimeString._to_time_delta(value)
        elif isinstance(value, datetime.timedelta):
            return TimeString._to_time_string(value)
        elif isinstance(value, int):
            return TimeString._to_time_string(value)
        else:
            raise ValueError('cannot convert {}, as it is an unsupported type'.format(value))

    @staticmethod
    def to_hours(value):
        """
        Converts timedelta or timestring to hours
        :param value: either timedelta or string - eg. 1y34w
        :return: number of hours
        :rtype: int
        """
        if isinstance(value, str):
            value = TimeString._to_time_delta(value)

        if isinstance(value, datetime.timedelta):
            return value.days*24+value.seconds/3600
        raise ValueError('The value {} was of an unexpected type?'.format(value))

    @staticmethod
    def _to_time_delta(item):
        """
        Parse a time string - eg. 1w2d
        :param item:
        :return:
        """
        string_time_match = TimeString.string_time_re.match(item)
        delta_parts = None
        if string_time_match:
            delta_parts = {x: int(v) for x, v in string_time_match.groupdict().items() if v}
        return datetime.timedelta(**delta_parts)

    @staticmethod
    def _to_time_string(item):
        """
        :param item: timedelta or int (hours)
        :type item: datetime.timedelta | int
        :return: str
        """
        hours = item
        if isinstance(item, datetime.timedelta):
            hours = TimeString.to_hours(item)

        val = ''
        years = int(hours/8760)
        weeks = int(hours/168)
        days = int(hours/24)

        if (years) > 0:
            val = '{}y'.format(years)
            remainder_days = int(hours%8760/24)
            if remainder_days == 0:
                pass  # do nothing further
            elif remainder_days%7 == 0:
                val += '{}w'.format(int(remainder_days/7))
            else:
                val += '{}d'.format(remainder_days)
        elif (weeks) > 0:
            val = '{}w'.format(weeks)
            remainder = (hours % 168)
            if remainder == 0:
                pass  # do nothing further
            elif remainder % 24 == 0:
                val += '{}d'.format(int(remainder/24))
            else:
                val += '{}h'.format(remainder)
        elif (days) > 0:
            val = '{}d'.format(days)
            remainder = (hours % 24)
            if remainder > 0:
                val += '{}h'.format(remainder)
        else:
            val += '{}h'.format(hours)
        return val

    @staticmethod
    def to_hours(value):
        """
        :param value: either timedelta or string - eg. 1y34w
        :return: number of hours
        :rtype: int
        """
        if isinstance(value, str):
            value = TimeString._to_time_delta(value)

        if isinstance(value, datetime.timedelta):
            return value.days*24+value.seconds/3600
        raise ValueError('The value {} was of an unexpected type?'.format(value))