# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.sbom_component_license_license import SBOMComponentLicenseLicense


class SBOMComponentLicense(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sbom_component_license_license import SBOMComponentLicenseLicense

        return {
            "license": (SBOMComponentLicenseLicense,),
        }

    attribute_map = {
        "license": "license",
    }

    def __init__(self_, license: SBOMComponentLicenseLicense, **kwargs):
        """
        The software license of the component of the SBOM.

        :param license: The software license of the component of the SBOM.
        :type license: SBOMComponentLicenseLicense
        """
        super().__init__(kwargs)

        self_.license = license
