# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SBOMComponentLicenseType(ModelSimple):
    """
    The SBOM component license type.

    :param value: Must be one of ["network_strong_copyleft", "non_standard_copyleft", "other_non_free", "other_non_standard", "permissive", "public_domain", "strong_copyleft", "weak_copyleft"].
    :type value: str
    """

    allowed_values = {
        "network_strong_copyleft",
        "non_standard_copyleft",
        "other_non_free",
        "other_non_standard",
        "permissive",
        "public_domain",
        "strong_copyleft",
        "weak_copyleft",
    }
    NETWORK_STRONG_COPYLEFT: ClassVar["SBOMComponentLicenseType"]
    NON_STANDARD_COPYLEFT: ClassVar["SBOMComponentLicenseType"]
    OTHER_NON_FREE: ClassVar["SBOMComponentLicenseType"]
    OTHER_NON_STANDARD: ClassVar["SBOMComponentLicenseType"]
    PERMISSIVE: ClassVar["SBOMComponentLicenseType"]
    PUBLIC_DOMAIN: ClassVar["SBOMComponentLicenseType"]
    STRONG_COPYLEFT: ClassVar["SBOMComponentLicenseType"]
    WEAK_COPYLEFT: ClassVar["SBOMComponentLicenseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SBOMComponentLicenseType.NETWORK_STRONG_COPYLEFT = SBOMComponentLicenseType("network_strong_copyleft")
SBOMComponentLicenseType.NON_STANDARD_COPYLEFT = SBOMComponentLicenseType("non_standard_copyleft")
SBOMComponentLicenseType.OTHER_NON_FREE = SBOMComponentLicenseType("other_non_free")
SBOMComponentLicenseType.OTHER_NON_STANDARD = SBOMComponentLicenseType("other_non_standard")
SBOMComponentLicenseType.PERMISSIVE = SBOMComponentLicenseType("permissive")
SBOMComponentLicenseType.PUBLIC_DOMAIN = SBOMComponentLicenseType("public_domain")
SBOMComponentLicenseType.STRONG_COPYLEFT = SBOMComponentLicenseType("strong_copyleft")
SBOMComponentLicenseType.WEAK_COPYLEFT = SBOMComponentLicenseType("weak_copyleft")
