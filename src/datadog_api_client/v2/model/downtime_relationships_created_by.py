# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.downtime_relationships_created_by_data import DowntimeRelationshipsCreatedByData


class DowntimeRelationshipsCreatedBy(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.downtime_relationships_created_by_data import (
            DowntimeRelationshipsCreatedByData,
        )

        return {
            "data": (DowntimeRelationshipsCreatedByData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[DowntimeRelationshipsCreatedByData, none_type, UnsetType] = unset, **kwargs):
        """
        The user who created the downtime.

        :param data: Data for the user who created the downtime.
        :type data: DowntimeRelationshipsCreatedByData, none_type, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
