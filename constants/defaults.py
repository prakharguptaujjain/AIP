"""
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.
"""
#! /usr/local/bin/python3

from enum import Enum

from models.metric_weights import MetricWeights


IP_SAFELIST = {
    '1.0.0.1',
    '1.1.1.1',
    '8.8.4.4',
    '8.8.8.8',
    '17.57.146.20',
    '18.221.56.27',
    '34.233.66.117',
    '35.186.224.25',
    '46.101.250.135',
    '46.137.190.132',
    '52.113.194.132',
    '52.60.129.180',
    '54.64.67.106',
    '54.67.10.127',
    '54.79.28.129',
    '54.94.142.218',
    '63.143.42.242',
    '63.143.42.243',
    '63.143.42.244',
    '63.143.42.245',
    '63.143.42.246',
    '63.143.42.247',
    '63.143.42.248',
    '63.143.42.249',
    '63.143.42.250',
    '63.143.42.251',
    '63.143.42.252',
    '63.143.42.253',
    '69.162.124.226',
    '69.162.124.227',
    '69.162.124.228',
    '69.162.124.229',
    '69.162.124.230',
    '69.162.124.231',
    '69.162.124.232',
    '69.162.124.233',
    '69.162.124.234',
    '69.162.124.235',
    '69.162.124.236',
    '69.162.124.237',
    '74.125.34.46',
    '89.221.214.130',
    '104.131.107.63',
    '122.248.234.23',
    '128.199.195.156',
    '138.197.150.151',
    '139.59.173.249',
    '142.250.102.188',
    '142.250.27.188',
    '146.185.143.14',
    '147.231.100.5',
    '159.203.30.41',
    '159.89.8.111',
    '165.227.83.148',
    '178.62.52.237',
    '188.226.183.141',
    '195.113.20.2',
    '198.49.23.145',
    '216.144.250.150',
    '216.245.221.82',
    '216.245.221.83',
    '216.245.221.84',
    '216.245.221.85',
    '216.245.221.86',
    '216.245.221.87',
    '216.245.221.88',
    '216.245.221.89',
    '216.245.221.90',
    '216.245.221.91',
    '216.245.221.92',
    '216.245.221.93',
    '2607:ff68:107::3',
    '2607:ff68:107::4',
    '2607:ff68:107::5',
    '2607:ff68:107::6',
    '2607:ff68:107::7',
    '2607:ff68:107::8',
    '2607:ff68:107::9',
    '2607:ff68:107::10',
    '2607:ff68:107::11',
    '2607:ff68:107::12',
    '2607:ff68:107::13',
    '2607:ff68:107::14',
    '2607:ff68:107::15',
    '2607:ff68:107::16',
    '2607:ff68:107::17',
    '2607:ff68:107::18',
    '2607:ff68:107::19',
    '2607:ff68:107::20',
    '2607:ff68:107::21',
    '2607:ff68:107::22',
    '2607:ff68:107::23',
    '2607:ff68:107::24',
    '2607:ff68:107::25',
    '2607:ff68:107::26',
    '2607:ff68:107::27',
    '2607:ff68:107::28',
    '2607:ff68:107::29',
    '2607:ff68:107::30',
    '2607:ff68:107::31',
    '2607:ff68:107::32',
    '2607:ff68:107::33',
    '2607:ff68:107::34',
    '2607:ff68:107::35',
    '2607:ff68:107::36',
    '2607:ff68:107::37',
    '2607:ff68:107::38'
}

CIDR_BLOCK_SAFELIST = {
    '35.190.247.0/24',
    '35.191.0.0/16',
    '64.18.0.0/16',
    '64.233.160.0/19',
    '66.102.0.0/20',
    '66.249.80.0/20',
    '72.14.192.0/18',
    '74.125.0.0/16',
    '108.177.8.0/21',
    '108.177.96.0/19',
    '130.211.0.0/22',
    '172.217.0.0/19',
    '172.217.128.0/19',
    '172.217.160.0/20',
    '172.217.192.0/19',
    '172.217.32.0/20',
    '172.253.112.0/20',
    '172.253.56.0/21',
    '173.194.0.0/16',
    '209.85.128.0/17',
    '216.239.32.0/19',
    '216.58.192.0/19'
}

ORG_SAFELIST = {
    'apple',
    'facebook',
    'google',
    'telegram',
    'microsoft',
    'spotify',
    'stratosphereips',
    'wikipedia'
}

class Blocklists(Enum):
    """
    Default blocklists names
    """
    NEW_BLOCKLIST = "new_blocklist"
    PC_BLOCKLIST = "pc_blocklist"
    PN_BLOCKLIST = "pn_blocklist"
    TRADITIONAL_BLOCKLIST = "trad_blocklist"

class BlocklistConfig(Enum):
    """
    Blocklist configuration keys
    """
    CHOSEN_FUNCTION = "chosen_function"
    CURRENT_TIME = "current_time"
    INPUT_FILEPATH = "absolute_data_filepath"
    OUTPUT_FILEPATH = "blocklist_filepath"
    REFERENCE_DATE = "reference_date"

class BlocklistTypes(Enum):
    """
    Parameterized file paths
    """
    NEW = f"_{Blocklists.NEW_BLOCKLIST.value}.csv"
    PC = f"_{Blocklists.PC_BLOCKLIST.value}.csv"
    PN = f"_{Blocklists.PN_BLOCKLIST.value}.csv"
    TRADITIONAL = f"_{Blocklists.TRADITIONAL_BLOCKLIST.value}.csv"

class Defaults(Enum):
    """
    Default values
    """
    DATE_FORMAT = "%Y-%m-%d"
    FIVE_PERCENTAGE = 0.05
    MINUTES_AN_HOUR = (60**2)
    MINUTES_A_DAY = 24*MINUTES_AN_HOUR
    NEG_INFINITY = - float("inf")
    POS_INFINITY = float("inf")
    SPLUNK_DATE_FORMAT = "%Y/%m/%d %H:%M:%S.%f"
    TEN_PERCENTAGE = 0.10
    TWENTY_PERCENTAGE = 0.20
    UNSEEN_DAYS = 6
    UTF_8 = "utf-8"
    ZERO = 0.0

class DefaultSafelists(Enum):
    """
    Default safelists
    """
    IP = IP_SAFELIST
    NET = CIDR_BLOCK_SAFELIST
    ORG = ORG_SAFELIST

class DirPaths(Enum):
    """
    Parameterized directories paths
    """
    ASN = "core/asn/"
    HISTORICAL_RATINGS = "historical_ratings/"
    INPUT_DATA = "input_data/"
    PRIORITIZE_CONSISTENT = "prioritize_consistent/"
    PRIORITIZE_NEW = "prioritize_new/"
    PRIORITIZE_TODAY_ONLY = "prioritize_today_only/"
    TRADITIONAL = "traditional/"

class EnvVars(Enum):
    """
    Parameterized environment variables
    """
    OUTPUT_FOLDER = "output_folder"
    OUTPUT_DATA_FOLDER = "output_data_folder"
    RESULTS_FILE ="results_file"

class FilePaths(Enum):
    """
    Parameterized file paths
    """
    ASN_DB = "asn.mmdb"
    ABSOLUTE_DATA = 'absolute_data.csv'
    AGING_PC_MODS = 'aging_modifiers_pc.csv'
    AGING_PN_MODS = 'aging_modifiers_pn.csv'
    FP_LOG = 'fp_log_file.csv'
    KNOWN_IPS = 'known_ips.txt'
    PROCESSED_FILES = 'processed_splunk_files.txt'
    SELECTED_MODULES = 'selected_modules.csv'
    TIMES = 'times.csv'

class FlowKeys(Enum):
    """
    Parameterized keys for Flow
    """
    SRC_ADDRESS = "src_address"
    EVENTS = "events"
    DURATION = "duration"
    AVG_DURATION = "avg_duration"
    BYTES = "bytes"
    AVG_BYTES = "avg_bytes"
    PACKETS = "packets"
    AVG_PACKETS = "avg_packets"
    FIRST_EVENT = "first_event"
    LAST_EVENT = "last_event"
    AVG_EVENTS = "avg_events"
    AGED_SCORE = "aged_score"

class Functions(Enum):
    """
    Defaults functions
    """
    PCN = "prioritize_consistent_normalized_ips"
    PCO = "prioritize_consistent_original_ips"
    PNN = "prioritize_new_normalized_ips"
    PNO = "prioritize_new_original_ips"
    POTN = "prioritize_only_normalized_today_ips"
    POT = "prioritize_only_today_ips"

class Normalized(MetricWeights):
    """
    Weights used to ponder normalized data
    """
    def __init__(self):
        self.total_events = Defaults.FIVE_PERCENTAGE.value
        self.average_events = Defaults.TWENTY_PERCENTAGE.value
        self.total_duration = Defaults.FIVE_PERCENTAGE.value
        self.average_duration = Defaults.TWENTY_PERCENTAGE.value
        self.total_bytes = Defaults.FIVE_PERCENTAGE.value
        self.average_bytes = Defaults.TWENTY_PERCENTAGE.value
        self.total_packets = Defaults.FIVE_PERCENTAGE.value
        self.average_packets = Defaults.TWENTY_PERCENTAGE.value

class Original(MetricWeights):
    """
    Weights used to ponder original data
    """
    def __init__(self):
        self.total_events = Defaults.TWENTY_PERCENTAGE.value
        self.average_events = Defaults.TEN_PERCENTAGE.value
        self.total_duration = Defaults.TEN_PERCENTAGE.value
        self.average_duration = Defaults.TEN_PERCENTAGE.value
        self.total_bytes = Defaults.TWENTY_PERCENTAGE.value
        self.average_bytes = Defaults.TEN_PERCENTAGE.value
        self.total_packets = Defaults.TEN_PERCENTAGE.value
        self.average_packets = Defaults.TEN_PERCENTAGE.value

class Weights(Enum):
    """
    Parameterized MetricWeights
    """
    NORMALIZED = Normalized()
    ORIGINAL = Original()
