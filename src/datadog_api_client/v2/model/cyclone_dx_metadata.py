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
    from datadog_api_client.v2.model.cyclone_dx_metadata_component import CycloneDXMetadataComponent
    from datadog_api_client.v2.model.cyclone_dx_metadata_tools import CycloneDXMetadataTools


class CycloneDXMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cyclone_dx_metadata_component import CycloneDXMetadataComponent
        from datadog_api_client.v2.model.cyclone_dx_metadata_tools import CycloneDXMetadataTools

        return {
            "component": (CycloneDXMetadataComponent,),
            "tools": (CycloneDXMetadataTools,),
        }

    attribute_map = {
        "component": "component",
        "tools": "tools",
    }

    def __init__(self_, component: CycloneDXMetadataComponent, tools: CycloneDXMetadataTools, **kwargs):
        """
        Metadata about the BOM, including the scanned asset and the scanner tool.

        :param component: The asset that was scanned (for example, a host or container image).
        :type component: CycloneDXMetadataComponent

        :param tools: Information about the scanner tool that produced this BOM.
        :type tools: CycloneDXMetadataTools
        """
        super().__init__(kwargs)

        self_.component = component
        self_.tools = tools
