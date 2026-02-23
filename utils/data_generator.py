from datetime import datetime


def generate_Email_Time_Stamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace("-", "").replace(":", "").replace(" ", "")