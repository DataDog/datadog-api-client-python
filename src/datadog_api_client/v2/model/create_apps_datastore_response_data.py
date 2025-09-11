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
    from datadog_api_client.v2.model.datastore_data_type import DatastoreDataType


class CreateAppsDatastoreResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.datastore_data_type import DatastoreDataType

        return {
            "id": (str,),
            "type": (DatastoreDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, type: DatastoreDataType, id: Union[str, UnsetType] = unset, **kwargs):
        """
        The newly created datastore's data.

        :param id: The unique identifier assigned to the newly created datastore.
        :type id: str, optional

        :param type: The resource type for datastores.
        :type type: DatastoreDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
