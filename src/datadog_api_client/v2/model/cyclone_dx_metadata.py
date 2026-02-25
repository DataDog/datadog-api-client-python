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
    from datadog_api_client.v2.model.cyclone_dx_asset_component import CycloneDXAssetComponent
    from datadog_api_client.v2.model.cyclone_dx_tools import CycloneDXTools


class CycloneDXMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cyclone_dx_asset_component import CycloneDXAssetComponent
        from datadog_api_client.v2.model.cyclone_dx_tools import CycloneDXTools

        return {
            "component": (CycloneDXAssetComponent,),
            "tools": (CycloneDXTools,),
        }

    attribute_map = {
        "component": "component",
        "tools": "tools",
    }

    def __init__(self_, component: CycloneDXAssetComponent, tools: CycloneDXTools, **kwargs):
        """
        Metadata for the CycloneDX BOM.

        :param component: The asset component represents the system or host being scanned.
        :type component: CycloneDXAssetComponent

        :param tools: Tools used to generate the BOM.
        :type tools: CycloneDXTools
        """
        super().__init__(kwargs)

        self_.component = component
        self_.tools = tools
