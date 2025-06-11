class CommonRegex:
    """
    A class containing common regular expressions used in the application.
    """

    # Regular expression to match a valid email address
    EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # Regular expression to match a valid URL
    URL_REGEX = r"^(https?|ftp)://[^\s/$.?#].[^\s]*$"

    # Regular expression to match a valid phone number (US format)
    PHONE_REGEX = r"^\+?1?\d{10,15}$"

    # Regex for time and description in schedule
    SCHEDULE_REGEX = r"([0-9]{2}:[0-9]{2})\s-\s(.*)"
