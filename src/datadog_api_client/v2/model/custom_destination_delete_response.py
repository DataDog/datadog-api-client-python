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
    from datadog_api_client.v2.model.custom_destination_metadata import CustomDestinationMetadata


class CustomDestinationDeleteResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_destination_metadata import CustomDestinationMetadata

        return {
            "meta": (CustomDestinationMetadata,),
        }

    attribute_map = {
        "meta": "meta",
    }

    def __init__(self_, meta: Union[CustomDestinationMetadata, UnsetType] = unset, **kwargs):
        """
        Response containing metadata about a deleted custom destination.

        :param meta: The metadata relevant to your configuration or recent request.
        :type meta: CustomDestinationMetadata, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
