from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta


def calc_end_time(values, data):
    pass
    # try:
    #     data_value = values.get(data)
    #     if data_value is None:
    #         return values
    #     start_time = values.get("start_time")
    #     if data == "hours":
    #         values["end_time"] = start_time + timedelta(hours=data_value)
    #     if data == "days":
    #         values["end_time"] = start_time + timedelta(days=data_value)
    #     if data == "minutes":
    #         values["end_time"] = start_time + timedelta(minutes=data_value)
    #     if data == "months":
    #         values["end_time"] = start_time + relativedelta(months=+data_value)
    #     if data == "years":
    #         values["end_time"] = start_time.replace(year=start_time.year + data_value)
    # except Exception as e:
    #     raise e
    # finally:
    #     end_time = str(values.get("end_time"))
    #     values["end_time"] = str(datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S"))
    #     return values

        # if data is None:
        #     return values
        # start_time = values.start_time
        # if data == "hours":
        #     values.end_time = start_time + timedelta(hours=)
        # if data == "days":
        #     values["end_time"] = start_time + timedelta(days=data_value)
        # if data == "minutes":
        #     values["end_time"] = start_time + timedelta(minutes=data_value)
        # if data == "months":
        #     values["end_time"] = start_time + relativedelta(months=+data_value)
        # if data == "years":
        #     values["end_time"] = start_time.replace(year=start_time.year + data_value)

        # end_time = str(values.get("end_time"))
        # values["end_time"] = str(datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S"))
        # return values