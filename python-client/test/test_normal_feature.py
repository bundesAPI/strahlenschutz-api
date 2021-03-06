"""
    ODL-Info API

    Daten zur radioaktiven Belastung in Deutschland. Weitere Informationen unter https://odlinfo.bfs.de/ODL/DE/service/datenschnittstelle/datenschnittstelle_node.html.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.strahlenschutz.model.base_feature import BaseFeature
from deutschland.strahlenschutz.model.geometry_point import GeometryPoint
from deutschland.strahlenschutz.model.normal_feature_properties import (
    NormalFeatureProperties,
)

from deutschland import strahlenschutz

globals()["BaseFeature"] = BaseFeature
globals()["GeometryPoint"] = GeometryPoint
globals()["NormalFeatureProperties"] = NormalFeatureProperties
from deutschland.strahlenschutz.model.normal_feature import NormalFeature


class TestNormalFeature(unittest.TestCase):
    """NormalFeature unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNormalFeature(self):
        """Test NormalFeature"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NormalFeature()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
