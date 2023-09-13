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
    from datadog_api_client.v2.model.custom_destination import CustomDestination
    from datadog_api_client.v2.model.custom_destination_metadata import CustomDestinationMetadata


class CustomDestinationListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_destination import CustomDestination
        from datadog_api_client.v2.model.custom_destination_metadata import CustomDestinationMetadata

        return {
            "data": ([CustomDestination],),
            "meta": (CustomDestinationMetadata,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_, data: List[CustomDestination], meta: Union[CustomDestinationMetadata, UnsetType] = unset, **kwargs
    ):
        """
        Response containing information about multiple custom destinations.

        :param data: Array of returned custom destinations.
        :type data: [CustomDestination]

        :param meta: The metadata relevant to your configuration or recent request.
        :type meta: CustomDestinationMetadata, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
