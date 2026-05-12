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
    from datadog_api_client.v2.model.create_backfilled_maintenance_request_data import (
        CreateBackfilledMaintenanceRequestData,
    )


class CreateBackfilledMaintenanceRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_backfilled_maintenance_request_data import (
            CreateBackfilledMaintenanceRequestData,
        )

        return {
            "data": (CreateBackfilledMaintenanceRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[CreateBackfilledMaintenanceRequestData, UnsetType] = unset, **kwargs):
        """
        Request object for creating a backfilled maintenance.

        :param data: The data object for creating a backfilled maintenance.
        :type data: CreateBackfilledMaintenanceRequestData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
