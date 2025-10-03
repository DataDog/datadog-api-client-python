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
    from datadog_api_client.v2.model.bulk_delete_apps_datastore_items_request_data_attributes import (
        BulkDeleteAppsDatastoreItemsRequestDataAttributes,
    )
    from datadog_api_client.v2.model.bulk_delete_apps_datastore_items_request_data_type import (
        BulkDeleteAppsDatastoreItemsRequestDataType,
    )


class BulkDeleteAppsDatastoreItemsRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.bulk_delete_apps_datastore_items_request_data_attributes import (
            BulkDeleteAppsDatastoreItemsRequestDataAttributes,
        )
        from datadog_api_client.v2.model.bulk_delete_apps_datastore_items_request_data_type import (
            BulkDeleteAppsDatastoreItemsRequestDataType,
        )

        return {
            "attributes": (BulkDeleteAppsDatastoreItemsRequestDataAttributes,),
            "id": (str,),
            "type": (BulkDeleteAppsDatastoreItemsRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: BulkDeleteAppsDatastoreItemsRequestDataType,
        attributes: Union[BulkDeleteAppsDatastoreItemsRequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data wrapper containing the data needed to delete items from a datastore.

        :param attributes: Attributes of request data to delete items from a datastore.
        :type attributes: BulkDeleteAppsDatastoreItemsRequestDataAttributes, optional

        :param id: ID for the datastore of the items to delete.
        :type id: str, optional

        :param type: Items resource type.
        :type type: BulkDeleteAppsDatastoreItemsRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
