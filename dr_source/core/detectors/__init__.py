# dr_source/core/detectors/__init__.py

from dr_source.core.detectors.sql_injection import SQLInjectionDetector
from dr_source.core.detectors.xss import XSSDetector
from dr_source.core.detectors.path_traversal import PathTraversalDetector
from dr_source.core.detectors.command_injection import CommandInjectionDetector
from dr_source.core.detectors.serialization import SerializationDetector
from dr_source.core.detectors.ldap_injection import LDAPInjectionDetector
from dr_source.core.detectors.xxe import XXEDetector
from dr_source.core.detectors.ssrf import SSRFDetector

DETECTORS = [
    SQLInjectionDetector,
    XSSDetector,
    PathTraversalDetector,
    CommandInjectionDetector,
    SerializationDetector,
    LDAPInjectionDetector,
    XXEDetector,
    SSRFDetector,
]


__all__ = ["DETECTORS"]
