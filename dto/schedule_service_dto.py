from typing import List

from pydantic import BaseModel


class ChannelPairDTO(BaseModel):
    channel_name: str
    channel_href: str


class RetrieveScheduleChannelsServiceResponse(BaseModel):
    channels: List[ChannelPairDTO]


class ScheduleDTO(BaseModel):
    time: str
    description: str


class RetrieveChannelScheduleServiceResponse(BaseModel):
    schedules: List[ScheduleDTO]
