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
    from datadog_api_client.v2.model.update_apps_datastore_item_request_data_attributes import (
        UpdateAppsDatastoreItemRequestDataAttributes,
    )
    from datadog_api_client.v2.model.update_apps_datastore_item_request_data_type import (
        UpdateAppsDatastoreItemRequestDataType,
    )


class UpdateAppsDatastoreItemRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_apps_datastore_item_request_data_attributes import (
            UpdateAppsDatastoreItemRequestDataAttributes,
        )
        from datadog_api_client.v2.model.update_apps_datastore_item_request_data_type import (
            UpdateAppsDatastoreItemRequestDataType,
        )

        return {
            "attributes": (UpdateAppsDatastoreItemRequestDataAttributes,),
            "id": (str,),
            "type": (UpdateAppsDatastoreItemRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: UpdateAppsDatastoreItemRequestDataType,
        attributes: Union[UpdateAppsDatastoreItemRequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data wrapper containing the item identifier and the changes to apply during the update operation.

        :param attributes: Attributes for updating a datastore item, including the item key and changes to apply.
        :type attributes: UpdateAppsDatastoreItemRequestDataAttributes, optional

        :param id: The unique identifier of the datastore item.
        :type id: str, optional

        :param type: The resource type for datastore items.
        :type type: UpdateAppsDatastoreItemRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
