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
    from datadog_api_client.v2.model.downtime_relationships_created_by import DowntimeRelationshipsCreatedBy
    from datadog_api_client.v2.model.downtime_relationships_monitor import DowntimeRelationshipsMonitor


class DowntimeRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.downtime_relationships_created_by import DowntimeRelationshipsCreatedBy
        from datadog_api_client.v2.model.downtime_relationships_monitor import DowntimeRelationshipsMonitor

        return {
            "created_by": (DowntimeRelationshipsCreatedBy,),
            "monitor": (DowntimeRelationshipsMonitor,),
        }

    attribute_map = {
        "created_by": "created_by",
        "monitor": "monitor",
    }

    def __init__(
        self_,
        created_by: Union[DowntimeRelationshipsCreatedBy, UnsetType] = unset,
        monitor: Union[DowntimeRelationshipsMonitor, UnsetType] = unset,
        **kwargs,
    ):
        """
        All relationships associated with downtime.

        :param created_by: The user who created the downtime.
        :type created_by: DowntimeRelationshipsCreatedBy, optional

        :param monitor: The monitor identified by the downtime.
        :type monitor: DowntimeRelationshipsMonitor, optional
        """
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if monitor is not unset:
            kwargs["monitor"] = monitor
        super().__init__(kwargs)
