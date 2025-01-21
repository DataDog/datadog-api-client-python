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
    from datadog_api_client.v2.model.action_connection_attributes import ActionConnectionAttributes
    from datadog_api_client.v2.model.action_connection_data_type import ActionConnectionDataType


class ActionConnectionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.action_connection_attributes import ActionConnectionAttributes
        from datadog_api_client.v2.model.action_connection_data_type import ActionConnectionDataType

        return {
            "attributes": (ActionConnectionAttributes,),
            "id": (str,),
            "type": (ActionConnectionDataType,),
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
        attributes: ActionConnectionAttributes,
        type: ActionConnectionDataType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data related to the connection.

        :param attributes: The definition of ``ActionConnectionAttributes`` object.
        :type attributes: ActionConnectionAttributes

        :param id: The connection identifier
        :type id: str, optional

        :param type: The definition of ``ActionConnectionDataType`` object.
        :type type: ActionConnectionDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
