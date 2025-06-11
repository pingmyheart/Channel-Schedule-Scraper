import re

from bs4 import BeautifulSoup
from requests import request

from dto.schedule_service_dto import RetrieveScheduleChannelsServiceResponse, ChannelPairDTO, \
    RetrieveChannelScheduleServiceResponse, ScheduleDTO
from util.common_regex import CommonRegex


class ScheduleService:
    def get_available_channels(self) -> RetrieveScheduleChannelsServiceResponse:
        """
        Retrieves the list of available channels for scheduling.

        :return: List of available channels.
        """
        # Build Response
        service_response = RetrieveScheduleChannelsServiceResponse(channels=[])
        # Retrieve page
        response = self.__retrieve_html_or_default()
        soup = BeautifulSoup(response, 'html.parser')
        channels = soup.find_all(class_='chbuttonsbox')
        for element in channels:
            for a in element.find_all('a'):
                (service_response.channels
                 .append(ChannelPairDTO(channel_name=a.text,
                                        channel_href=a.get('href'))))
        return service_response

    def get_schedule_by_channel(self, channel_href: str) -> str:
        """
        Retrieves the schedule for a specific channel.

        :param channel_href: The URL or path of the channel to retrieve the schedule for.
        :return: HTML content of the channel's schedule.
        """
        # Build Response
        service_response = RetrieveChannelScheduleServiceResponse(schedules=[])
        # Retrieve page
        response = self.__retrieve_html_or_default(path=channel_href)
        soup = BeautifulSoup(response, 'html.parser')
        box = soup.find_all(class_='listingbox')
        for element in box:
            for line in element.find('h4').text.split("\n"):
                matches = re.findall(CommonRegex.SCHEDULE_REGEX, line.strip())
                for time, description in matches:
                    (service_response.schedules
                     .append(ScheduleDTO(time=time.strip(),
                                         description=description.strip())))
        return service_response

    def __retrieve_html_or_default(self, path: str = None) -> str:
        """
        Retrieves the HTML content from a given path or returns a default message if the path is invalid.

        :param path: The URL or file path to retrieve HTML from.
        :return: HTML content as a string or a default message.
        """
        return request('GET', f"https://www.staseraintv.com{path if path else ''}").text


if __name__ == '__main__':
    service = ScheduleService()
    print(service.get_available_channels())
    print(service.get_schedule_by_channel('/programmi_stasera_iris.html#pal'))
