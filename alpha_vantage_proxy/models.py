
import enum

class TimeSeriesFunction(enum.Enum):
   
    INTRADAY = "TIME_SERIES_INTRADAY"
    INTRADAY_EXTENDED = "TIME_SERIES_INTRADAY_EXTENDED"
    DAILY = "TIME_SERIES_DAILY"
    DAILY_ADJUSTED = "TIME_SERIES_DAILY_ADJUSTED"
    WEEKLY = "TIME_SERIES_WEEKLY"
    WEEKLY_ADJUSTED = "TIME_SERIES_WEEKLY_ADJUSTED"
    MONTHLY = "TIME_SERIES_MONTHLY"
    MONTHLY_ADJUSTED = "TIME_SERIES_MONTHLY_ADJUSTED"

class TimeSeriesOutputSize(enum.Enum):

    COMPACT = "compact"
    FULL = "full"

class TimeSeriesDataType(enum.Enum):

    JSON = "json"
    CSV = "csv"