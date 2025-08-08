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
    from datadog_api_client.v2.model.create_apps_datastore_response_data_type import CreateAppsDatastoreResponseDataType


class CreateAppsDatastoreResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_apps_datastore_response_data_type import (
            CreateAppsDatastoreResponseDataType,
        )

        return {
            "id": (str,),
            "type": (CreateAppsDatastoreResponseDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, type: CreateAppsDatastoreResponseDataType, id: Union[str, UnsetType] = unset, **kwargs):
        """
        The definition of ``CreateAppsDatastoreResponseData`` object.

        :param id: The ``CreateAppsDatastoreResponseData`` ``id``.
        :type id: str, optional

        :param type: Datastores resource type.
        :type type: CreateAppsDatastoreResponseDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
