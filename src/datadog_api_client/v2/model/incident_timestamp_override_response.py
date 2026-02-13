# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_timestamp_override_data import IncidentTimestampOverrideData
    from datadog_api_client.v2.model.user_included import UserIncluded


class IncidentTimestampOverrideResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_timestamp_override_data import IncidentTimestampOverrideData
        from datadog_api_client.v2.model.user_included import UserIncluded

        return {
            "data": (IncidentTimestampOverrideData,),
            "included": ([UserIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_, data: IncidentTimestampOverrideData, included: Union[List[UserIncluded], UnsetType] = unset, **kwargs
    ):
        """
        Response containing a single incident timestamp override.

        :param data: Data for a single incident timestamp override.
        :type data: IncidentTimestampOverrideData

        :param included: Included related resources.
        :type included: [UserIncluded], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
