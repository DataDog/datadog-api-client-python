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
    from datadog_api_client.v2.model.custom_destination_without_id import CustomDestinationWithoutId


class CustomDestinationCreatePayload(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_destination_without_id import CustomDestinationWithoutId

        return {
            "data": (CustomDestinationWithoutId,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CustomDestinationWithoutId, **kwargs):
        """
        Payload containing information about a single custom destination to be created.

        :param data: The custom destination object without an assigned ID.
        :type data: CustomDestinationWithoutId
        """
        super().__init__(kwargs)

        self_.data = data
