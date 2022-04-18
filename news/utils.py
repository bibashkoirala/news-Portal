from datetime import datetime
from pyBSDate import convert_AD_to_BS, bsdate


def TodayBS():
    today = datetime.now()
    # date = today.strftime("%Y/%m/%d")
    date = convert_AD_to_BS(today.year, today.month, today.day)
    ne_date = bsdate(date[0], date[1], date[2])
    return ne_date.strftime("%B %d %Y,%A", lang='ne')
