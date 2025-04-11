DEBUG = True
SECRET_KEY = (
    "django-insecure-zy=41263$a3vdnq9_#o1m3p8t+pb%t38cuxw)ig)yh6=(m6*-7"
)

LOGGING["formatters"]["colored"] = {  # type: ignore
    "()": "colorlog.ColoredFormatter",
    "format": "%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s",
}
LOGGING["loggers"]["bitcoin_core"]["level"] = "DEBUG"  # type: ignore
LOGGING["handlers"]["console"]["level"] = "DEBUG"  # type: ignore
LOGGING["handlers"]["console"]["formatter"] = "colored"  # type: ignore
