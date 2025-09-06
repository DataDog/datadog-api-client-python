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
    from datadog_api_client.v2.model.delete_apps_datastore_item_request_data_attributes import (
        DeleteAppsDatastoreItemRequestDataAttributes,
    )
    from datadog_api_client.v2.model.datastore_items_data_type import DatastoreItemsDataType


class DeleteAppsDatastoreItemRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.delete_apps_datastore_item_request_data_attributes import (
            DeleteAppsDatastoreItemRequestDataAttributes,
        )
        from datadog_api_client.v2.model.datastore_items_data_type import DatastoreItemsDataType

        return {
            "attributes": (DeleteAppsDatastoreItemRequestDataAttributes,),
            "type": (DatastoreItemsDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: DatastoreItemsDataType,
        attributes: Union[DeleteAppsDatastoreItemRequestDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data wrapper containing the information needed to identify and delete a specific datastore item.

        :param attributes: Attributes specifying which datastore item to delete by its primary key.
        :type attributes: DeleteAppsDatastoreItemRequestDataAttributes, optional

        :param type: The resource type for datastore items.
        :type type: DatastoreItemsDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
