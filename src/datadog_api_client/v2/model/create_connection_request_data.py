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
    from datadog_api_client.v2.model.create_connection_request_data_attributes import (
        CreateConnectionRequestDataAttributes,
    )
    from datadog_api_client.v2.model.update_connection_request_data_type import UpdateConnectionRequestDataType


class CreateConnectionRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_connection_request_data_attributes import (
            CreateConnectionRequestDataAttributes,
        )
        from datadog_api_client.v2.model.update_connection_request_data_type import UpdateConnectionRequestDataType

        return {
            "attributes": (CreateConnectionRequestDataAttributes,),
            "id": (str,),
            "type": (UpdateConnectionRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: UpdateConnectionRequestDataType,
        attributes: Union[CreateConnectionRequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object containing the resource type and attributes for creating a new connection.

        :param attributes: Attributes defining the data source connection, including join configuration and custom fields.
        :type attributes: CreateConnectionRequestDataAttributes, optional

        :param id: Unique identifier for the new connection resource.
        :type id: str, optional

        :param type: Connection id resource type.
        :type type: UpdateConnectionRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
