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
    from datadog_api_client.v2.model.connection_group_data_attributes_request import (
        ConnectionGroupDataAttributesRequest,
    )
    from datadog_api_client.v2.model.connection_group_type import ConnectionGroupType


class ConnectionGroupDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.connection_group_data_attributes_request import (
            ConnectionGroupDataAttributesRequest,
        )
        from datadog_api_client.v2.model.connection_group_type import ConnectionGroupType

        return {
            "attributes": (ConnectionGroupDataAttributesRequest,),
            "type": (ConnectionGroupType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: ConnectionGroupType,
        attributes: Union[ConnectionGroupDataAttributesRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for updating a connection group.

        :param attributes: Attributes for updating a connection group.
        :type attributes: ConnectionGroupDataAttributesRequest, optional

        :param type: The definition of ``ConnectionGroupType`` object.
        :type type: ConnectionGroupType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
