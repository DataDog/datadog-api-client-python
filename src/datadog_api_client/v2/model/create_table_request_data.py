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
    from datadog_api_client.v2.model.create_table_request_data_attributes import CreateTableRequestDataAttributes
    from datadog_api_client.v2.model.create_table_request_data_type import CreateTableRequestDataType


class CreateTableRequestData(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_table_request_data_attributes import CreateTableRequestDataAttributes
        from datadog_api_client.v2.model.create_table_request_data_type import CreateTableRequestDataType

        return {
            "attributes": (CreateTableRequestDataAttributes,),
            "type": (CreateTableRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: CreateTableRequestDataType,
        attributes: Union[CreateTableRequestDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object containing the table definition.

        :param attributes: Attributes that define the reference table's configuration and properties.
        :type attributes: CreateTableRequestDataAttributes, optional

        :param type: Reference table resource type.
        :type type: CreateTableRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
