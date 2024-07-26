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
    from datadog_api_client.v2.model.custom_costs_file_metadata_with_content import CustomCostsFileMetadataWithContent


class CustomCostsFileMetadataWithContentHighLevel(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_costs_file_metadata_with_content import (
            CustomCostsFileMetadataWithContent,
        )

        return {
            "attributes": (CustomCostsFileMetadataWithContent,),
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[CustomCostsFileMetadataWithContent, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON API format of for a Custom Costs file with content.

        :param attributes: Schema of a cost file's metadata.
        :type attributes: CustomCostsFileMetadataWithContent, optional

        :param id: ID of the Custom Costs metadata.
        :type id: str, optional

        :param type: Type of the Custom Costs file metadata.
        :type type: str, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
