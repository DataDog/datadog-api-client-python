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
    from datadog_api_client.v2.model.create_apps_datastore_request_data_attributes import (
        CreateAppsDatastoreRequestDataAttributes,
    )
    from datadog_api_client.v2.model.datastore_data_type import DatastoreDataType


class CreateAppsDatastoreRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_apps_datastore_request_data_attributes import (
            CreateAppsDatastoreRequestDataAttributes,
        )
        from datadog_api_client.v2.model.datastore_data_type import DatastoreDataType

        return {
            "attributes": (CreateAppsDatastoreRequestDataAttributes,),
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
        attributes: Union[CreateAppsDatastoreRequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data wrapper containing the configuration needed to create a new datastore.

        :param attributes: Configuration and metadata to create a new datastore.
        :type attributes: CreateAppsDatastoreRequestDataAttributes, optional

        :param id: Optional ID for the new datastore. If not provided, one will be generated automatically.
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
