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
    from datadog_api_client.v2.model.update_apps_datastore_item_request_data_attributes_item_changes import (
        UpdateAppsDatastoreItemRequestDataAttributesItemChanges,
    )


class UpdateAppsDatastoreItemRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_apps_datastore_item_request_data_attributes_item_changes import (
            UpdateAppsDatastoreItemRequestDataAttributesItemChanges,
        )

        return {
            "item_changes": (UpdateAppsDatastoreItemRequestDataAttributesItemChanges,),
            "item_key": (str,),
        }

    attribute_map = {
        "item_changes": "item_changes",
        "item_key": "item_key",
    }

    def __init__(self_, item_changes: UpdateAppsDatastoreItemRequestDataAttributesItemChanges, item_key: str, **kwargs):
        """
        The definition of ``UpdateAppsDatastoreItemRequestDataAttributes`` object.

        :param item_changes: The definition of ``UpdateAppsDatastoreItemRequestDataAttributesItemChanges`` object.
        :type item_changes: UpdateAppsDatastoreItemRequestDataAttributesItemChanges

        :param item_key: The ``attributes`` ``item_key``.
        :type item_key: str
        """
        super().__init__(kwargs)

        self_.item_changes = item_changes
        self_.item_key = item_key
