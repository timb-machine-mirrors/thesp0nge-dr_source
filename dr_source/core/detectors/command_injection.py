# dr_source/core/detectors/command_injection.py
import re
import logging
from dr_source.core.detectors.base import BaseDetector

logger = logging.getLogger(__name__)


class CommandInjectionDetector(BaseDetector):
    REGEX_PATTERNS = [
        re.compile(
            r"(?i)Runtime\.getRuntime\(\)\.exec\s*\(.*request\.getParameter.*\)",
            re.DOTALL,
        ),
        re.compile(r"(?i)ProcessBuilder\s*\(.*request\.getParameter.*\)", re.DOTALL),
        re.compile(r"(?i)exec\s*\(.*(?:;|\||&).*request\.getParameter.*\)", re.DOTALL),
    ]

    def detect(self, file_object):
        results = []
        logger.debug(
            "Scanning file '%s' for Command Injection vulnerabilities.",
            file_object.path,
        )
        for regex in self.REGEX_PATTERNS:
            for match in regex.finditer(file_object.content):
                line = file_object.content.count("\n", 0, match.start()) + 1
                logger.debug(
                    "Command Injection vulnerability found in '%s' at line %s: %s",
                    file_object.path,
                    line,
                    match.group(),
                )
                results.append(
                    {
                        "file": file_object.path,
                        "vuln_type": "Command Injection",
                        "match": match.group(),
                        "line": line,
                    }
                )
        return results
