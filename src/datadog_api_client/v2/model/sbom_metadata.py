# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.sbom_metadata_component import SBOMMetadataComponent


class SBOMMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sbom_metadata_component import SBOMMetadataComponent

        return {
            "component": (SBOMMetadataComponent,),
        }

    attribute_map = {
        "component": "component",
    }

    def __init__(self_, component: Union[SBOMMetadataComponent, UnsetType] = unset, **kwargs):
        """
        Provides additional information about a BOM.

        :param component: The component that the BOM describes.
        :type component: SBOMMetadataComponent, optional
        """
        if component is not unset:
            kwargs["component"] = component
        super().__init__(kwargs)
