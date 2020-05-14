try:
    from crawler.settings.local import *
except Exception as e:
    from crawler.settings.prod import *