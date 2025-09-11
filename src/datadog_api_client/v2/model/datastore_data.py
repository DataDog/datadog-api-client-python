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
    from datadog_api_client.v2.model.datastore_data_attributes import DatastoreDataAttributes
    from datadog_api_client.v2.model.datastore_data_type import DatastoreDataType


class DatastoreData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.datastore_data_attributes import DatastoreDataAttributes
        from datadog_api_client.v2.model.datastore_data_type import DatastoreDataType

        return {
            "attributes": (DatastoreDataAttributes,),
            "id": (str,),
            "type": (DatastoreDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: DatastoreDataType,
        attributes: Union[DatastoreDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Core information about a datastore, including its unique identifier and attributes.

        :param attributes: Detailed information about a datastore.
        :type attributes: DatastoreDataAttributes, optional

        :param id: The unique identifier of the datastore.
        :type id: str, optional

        :param type: The resource type for datastores.
        :type type: DatastoreDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
