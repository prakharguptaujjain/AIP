"""
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.
"""
#! /usr/local/bin/python3

from dataclasses import dataclass

from models.base import Base
from constants.defaults import Defaults, FlowKeys


@dataclass
class Flow(Base):
    """
    dataclass used to describe flows
    """
    src_address: str
    events: float
    duration: float
    avg_duration: float
    bytes: float
    avg_bytes: float
    packets: float
    avg_packets: float
    first_event: float
    last_event: float
    avg_events: float
    aged_score: float

    __slots__ = [name for name in dir(FlowKeys) if not name.startswith('_')]


    def __init__(self):
        """
        Default constructor
        """
        self.src_address = "1.0.0.1"
        self.float = Defaults.ZERO.value
        self.duration = Defaults.ZERO.value
        self.avg_duration = Defaults.ZERO.value
        self.bytes = Defaults.ZERO.value
        self.avg_bytes = Defaults.ZERO.value
        self.packets = Defaults.ZERO.value
        self.avg_packets = Defaults.ZERO.value
        self.first_event = Defaults.ZERO.value
        self.last_event = Defaults.ZERO.value
        self.avg_events = Defaults.ZERO.value
        self.aged_score = Defaults.ZERO.value

    @classmethod
    def from_line(cls, line):
        """
        Flow constructor from CSV line
        """
        f = cls()
        f.src_address = str(line[0])
        f.events = float(line[1])
        f.duration = float(line[2])
        f.avg_duration = float(line[3])
        f.bytes = float(line[4])
        f.avg_bytes = float(line[5])
        f.packets = float(line[6])
        f.avg_packets = float(line[7])
        f.first_event = float(line[8])
        f.last_event = float(line[9])
        f.avg_events = float(line[10])

        return f

    @classmethod
    def from_dict(cls, config):
        """
        Flow constructor from config dict
        """
        f = cls()
        f.src_address = config.get(FlowKeys.SRC_ADDRESS.value)
        f.events = float(config.get(FlowKeys.EVENTS.value))
        f.duration = float(config.get(FlowKeys.DURATION.value))
        f.avg_duration = float(config.get(FlowKeys.AVG_DURATION.value))
        f.bytes = float(config.get(FlowKeys.BYTES.value))
        f.avg_bytes = float(config.get(FlowKeys.AVG_BYTES.value))
        f.packets = float(config.get(FlowKeys.PACKETS.value))
        f.avg_packets = float(config.get(FlowKeys.AVG_PACKETS.value))
        f.first_event = float(config.get(FlowKeys.FIRST_EVENT.value))
        f.last_event = float(config.get(FlowKeys.LAST_EVENT.value))
        f.avg_events = float(config.get(FlowKeys.AVG_EVENTS.value))

        return f
