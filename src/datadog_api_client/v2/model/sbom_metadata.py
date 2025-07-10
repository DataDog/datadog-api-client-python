# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.sbom_metadata_author import SBOMMetadataAuthor
    from datadog_api_client.v2.model.sbom_metadata_component import SBOMMetadataComponent


class SBOMMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sbom_metadata_author import SBOMMetadataAuthor
        from datadog_api_client.v2.model.sbom_metadata_component import SBOMMetadataComponent

        return {
            "authors": ([SBOMMetadataAuthor],),
            "component": (SBOMMetadataComponent,),
            "timestamp": (str,),
        }

    attribute_map = {
        "authors": "authors",
        "component": "component",
        "timestamp": "timestamp",
    }

    def __init__(
        self_,
        authors: Union[List[SBOMMetadataAuthor], UnsetType] = unset,
        component: Union[SBOMMetadataComponent, UnsetType] = unset,
        timestamp: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Provides additional information about a BOM.

        :param authors: List of authors of the SBOM.
        :type authors: [SBOMMetadataAuthor], optional

        :param component: The component that the BOM describes.
        :type component: SBOMMetadataComponent, optional

        :param timestamp: The timestamp of the SBOM creation.
        :type timestamp: str, optional
        """
        if authors is not unset:
            kwargs["authors"] = authors
        if component is not unset:
            kwargs["component"] = component
        if timestamp is not unset:
            kwargs["timestamp"] = timestamp
        super().__init__(kwargs)
