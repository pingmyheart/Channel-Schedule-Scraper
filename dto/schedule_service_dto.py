from typing import List

from pydantic import BaseModel

from dto.service_response import ServiceResponse


class ChannelPairDTO(BaseModel):
    channel_name: str
    channel_href: str


class RetrieveScheduleChannelsServiceResponse(ServiceResponse):
    channels: List[ChannelPairDTO]


class ScheduleDTO(BaseModel):
    time: str
    description: str


class RetrieveChannelScheduleServiceResponse(ServiceResponse):
    schedules: List[ScheduleDTO]
