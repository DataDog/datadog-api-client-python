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
    from datadog_api_client.v2.model.update_apps_datastore_request_data_attributes import (
        UpdateAppsDatastoreRequestDataAttributes,
    )
    from datadog_api_client.v2.model.datastore_data_type import DatastoreDataType


class UpdateAppsDatastoreRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_apps_datastore_request_data_attributes import (
            UpdateAppsDatastoreRequestDataAttributes,
        )
        from datadog_api_client.v2.model.datastore_data_type import DatastoreDataType

        return {
            "attributes": (UpdateAppsDatastoreRequestDataAttributes,),
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
        attributes: Union[UpdateAppsDatastoreRequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data wrapper containing the datastore identifier and the attributes to update.

        :param attributes: Attributes that can be updated on a datastore.
        :type attributes: UpdateAppsDatastoreRequestDataAttributes, optional

        :param id: The unique identifier of the datastore to update.
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
