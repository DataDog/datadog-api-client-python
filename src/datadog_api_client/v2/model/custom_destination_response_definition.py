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
    from datadog_api_client.v2.model.custom_destination_response_attributes import CustomDestinationResponseAttributes
    from datadog_api_client.v2.model.custom_destination_type import CustomDestinationType


class CustomDestinationResponseDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_destination_response_attributes import (
            CustomDestinationResponseAttributes,
        )
        from datadog_api_client.v2.model.custom_destination_type import CustomDestinationType

        return {
            "attributes": (CustomDestinationResponseAttributes,),
            "id": (str,),
            "type": (CustomDestinationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    read_only_vars = {
        "id",
    }

    def __init__(
        self_,
        attributes: Union[CustomDestinationResponseAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[CustomDestinationType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of a custom destination.

        :param attributes: The attributes associated with the custom destination.
        :type attributes: CustomDestinationResponseAttributes, optional

        :param id: The custom destination ID.
        :type id: str, optional

        :param type: The type of the resource. The value should always be ``custom_destination``.
        :type type: CustomDestinationType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
