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
    from datadog_api_client.v2.model.delete_apps_datastore_response_data_type import DeleteAppsDatastoreResponseDataType


class DeleteAppsDatastoreResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.delete_apps_datastore_response_data_type import (
            DeleteAppsDatastoreResponseDataType,
        )

        return {
            "id": (str,),
            "type": (DeleteAppsDatastoreResponseDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, type: DeleteAppsDatastoreResponseDataType, id: Union[str, UnsetType] = unset, **kwargs):
        """
        The definition of ``DeleteAppsDatastoreResponseData`` object.

        :param id: The ``DeleteAppsDatastoreResponseData`` ``id``.
        :type id: str, optional

        :param type: Datastores resource type.
        :type type: DeleteAppsDatastoreResponseDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
