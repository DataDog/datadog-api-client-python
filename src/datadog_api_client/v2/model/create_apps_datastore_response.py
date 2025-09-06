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
    from datadog_api_client.v2.model.create_apps_datastore_response_data import CreateAppsDatastoreResponseData


class CreateAppsDatastoreResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_apps_datastore_response_data import CreateAppsDatastoreResponseData

        return {
            "data": (CreateAppsDatastoreResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[CreateAppsDatastoreResponseData, UnsetType] = unset, **kwargs):
        """
        Response after successfully creating a new datastore, containing the datastore's assigned ID.

        :param data: The newly created datastore's data.
        :type data: CreateAppsDatastoreResponseData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
