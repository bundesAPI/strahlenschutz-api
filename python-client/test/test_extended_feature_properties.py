"""
    ODL-Info API

    Daten zur radioaktiven Belastung in Deutschland. Weitere Informationen unter https://odlinfo.bfs.de/ODL/DE/service/datenschnittstelle/datenschnittstelle_node.html.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.strahlenschutz.model.normal_feature_properties import (
    NormalFeatureProperties,
)

from deutschland import strahlenschutz

globals()["NormalFeatureProperties"] = NormalFeatureProperties
from deutschland.strahlenschutz.model.extended_feature_properties import (
    ExtendedFeatureProperties,
)


class TestExtendedFeatureProperties(unittest.TestCase):
    """ExtendedFeatureProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testExtendedFeatureProperties(self):
        """Test ExtendedFeatureProperties"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ExtendedFeatureProperties()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
