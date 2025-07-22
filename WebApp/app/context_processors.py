from datetime import datetime
import pytz


def common_context(request):
    if request.user.is_authenticated:
        timezone = pytz.timezone("Asia/Tehran")
        now = datetime.now(timezone)
        context = {'current_time': now, }
    else:
        context = {'current_time': 0, }

    return context
