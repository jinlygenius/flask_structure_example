from datetime import datetime, timezone
# import pytz
import time
import uuid


def parse_request_args_keys(request):
    '''
    In a GET request, return all query params keys
    '''
    query_args = request.args
    return [_ for _ in query_args]


def parse_request_json_keys(request):
    '''
    In a POST request, return all post params keys
    '''
    post_data = request.json
    return [_ for _ in post_data]


def generate_user_id():
    '''
    Generate a UUID for user_id
    '''
    user_id = uuid.uuid4().hex
    return user_id


def convert_string_2_timestamp(datetime_string):
    try:
        res = int(time.mktime(datetime.strptime(datetime_string, "%Y-%m-%dT%H:%M:%SZ").timetuple()))
        # res = int(time.mktime(datetime.strptime(datetime_string, "%Y-%m-%dT%H:%M:%SZ").timetuple()) * 1000000000)
    except:
        res = int(time.mktime(datetime.strptime(datetime_string, "%Y-%m-%dT%H:%M:%S").timetuple()))
    return res


def convert_timestamp_2_UTC8_datetimestring(timestamp):
    # local_tz = pytz.timezone('Asia/Shanghai')
    # dt = datetime.fromtimestamp(timestamp, tz=local_tz)

    # convert timestamp to UTC+8 timestamp
    utc8_timestamp = timestamp + 8 * 60 * 60
    dt = datetime.fromtimestamp(utc8_timestamp)
    dt_string = dt.strftime("%Y-%m-%dT%H:%M:%S")
    return dt_string


def convert_UTCstring_2_UTC8string(datetime_string):
    ts = convert_string_2_timestamp(datetime_string)
    dt_str = convert_timestamp_2_UTC8_datetimestring(ts)
    return dt_str
