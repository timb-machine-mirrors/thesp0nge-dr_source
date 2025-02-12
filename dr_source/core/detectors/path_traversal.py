# dr_source/core/detectors/path_traversal.py
import re
import logging
from dr_source.core.detectors.base import BaseDetector

logger = logging.getLogger(__name__)


class PathTraversalDetector(BaseDetector):
    REGEX_PATTERNS = [
        re.compile(r"(?i)new\s+File\s*\(\s*.*request\.getParameter.*\)", re.DOTALL),
        re.compile(
            r"(?i)(FileInputStream|FileOutputStream|FileReader|FileWriter)\s*\(.*request\.getParameter.*\)",
            re.DOTALL,
        ),
        re.compile(r"(?i)(\.\./)+", re.DOTALL),
    ]

    def detect(self, file_object):
        results = []
        logger.debug(
            "Scanning file '%s' for Path Traversal vulnerabilities.", file_object.path
        )
        for regex in self.REGEX_PATTERNS:
            for match in regex.finditer(file_object.content):
                line = file_object.content.count("\n", 0, match.start()) + 1
                logger.info(
                    "Path Traversal vulnerability found in '%s' at line %s: %s",
                    file_object.path,
                    line,
                    match.group(),
                )
                results.append(
                    {
                        "file": file_object.path,
                        "vuln_type": "Path Traversal",
                        "match": match.group(),
                        "line": line,
                    }
                )
        return results
