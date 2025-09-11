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
    from datadog_api_client.v2.model.update_apps_datastore_request_data import UpdateAppsDatastoreRequestData


class UpdateAppsDatastoreRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_apps_datastore_request_data import UpdateAppsDatastoreRequestData

        return {
            "data": (UpdateAppsDatastoreRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[UpdateAppsDatastoreRequestData, UnsetType] = unset, **kwargs):
        """
        Request to update a datastore's configuration such as its name or description.

        :param data: Data wrapper containing the datastore identifier and the attributes to update.
        :type data: UpdateAppsDatastoreRequestData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
