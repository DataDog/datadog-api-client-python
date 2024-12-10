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
    from datadog_api_client.v2.model.custom_connection_attributes import CustomConnectionAttributes
    from datadog_api_client.v2.model.custom_connection_type import CustomConnectionType


class CustomConnection(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_connection_attributes import CustomConnectionAttributes
        from datadog_api_client.v2.model.custom_connection_type import CustomConnectionType

        return {
            "attributes": (CustomConnectionAttributes,),
            "id": (str,),
            "type": (CustomConnectionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[CustomConnectionAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[CustomConnectionType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``CustomConnection`` object.

        :param attributes: The definition of ``CustomConnectionAttributes`` object.
        :type attributes: CustomConnectionAttributes, optional

        :param id: The ``CustomConnection`` ``id``.
        :type id: str, optional

        :param type: The definition of ``CustomConnectionType`` object.
        :type type: CustomConnectionType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
