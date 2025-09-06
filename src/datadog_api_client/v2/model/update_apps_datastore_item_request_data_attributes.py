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
    from datadog_api_client.v2.model.update_apps_datastore_item_request_data_attributes_item_changes import (
        UpdateAppsDatastoreItemRequestDataAttributesItemChanges,
    )


class UpdateAppsDatastoreItemRequestDataAttributes(ModelNormal):
    validations = {
        "item_key": {
            "max_length": 256,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_apps_datastore_item_request_data_attributes_item_changes import (
            UpdateAppsDatastoreItemRequestDataAttributesItemChanges,
        )

        return {
            "id": (str,),
            "item_changes": (UpdateAppsDatastoreItemRequestDataAttributesItemChanges,),
            "item_key": (str,),
        }

    attribute_map = {
        "id": "id",
        "item_changes": "item_changes",
        "item_key": "item_key",
    }

    def __init__(
        self_,
        item_changes: UpdateAppsDatastoreItemRequestDataAttributesItemChanges,
        item_key: str,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating a datastore item, including the item key and changes to apply.

        :param id: The unique identifier of the item being updated.
        :type id: str, optional

        :param item_changes: Changes to apply to a datastore item using set operations.
        :type item_changes: UpdateAppsDatastoreItemRequestDataAttributesItemChanges

        :param item_key: The primary key that identifies the item to update. Cannot exceed 256 characters.
        :type item_key: str
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.item_changes = item_changes
        self_.item_key = item_key
