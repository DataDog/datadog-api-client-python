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
    from datadog_api_client.v2.model.action_connection_attributes_update import ActionConnectionAttributesUpdate
    from datadog_api_client.v2.model.action_connection_data_type import ActionConnectionDataType


class ActionConnectionDataUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.action_connection_attributes_update import ActionConnectionAttributesUpdate
        from datadog_api_client.v2.model.action_connection_data_type import ActionConnectionDataType

        return {
            "attributes": (ActionConnectionAttributesUpdate,),
            "type": (ActionConnectionDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: ActionConnectionAttributesUpdate, type: ActionConnectionDataType, **kwargs):
        """
        Data related to the connection update.

        :param attributes: The definition of ``ActionConnectionAttributesUpdate`` object.
        :type attributes: ActionConnectionAttributesUpdate

        :param type: The definition of ``ActionConnectionDataType`` object.
        :type type: ActionConnectionDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
