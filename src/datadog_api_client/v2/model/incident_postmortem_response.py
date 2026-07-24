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
    from datadog_api_client.v2.model.incident_postmortem_data import IncidentPostmortemData
    from datadog_api_client.v2.model.incident_postmortem_included import IncidentPostmortemIncluded
    from datadog_api_client.v2.model.incident_user_data import IncidentUserData
    from datadog_api_client.v2.model.incident_response_data import IncidentResponseData


class IncidentPostmortemResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_postmortem_data import IncidentPostmortemData
        from datadog_api_client.v2.model.incident_postmortem_included import IncidentPostmortemIncluded

        return {
            "data": (IncidentPostmortemData,),
            "included": ([IncidentPostmortemIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: IncidentPostmortemData,
        included: Union[
            List[Union[IncidentPostmortemIncluded, IncidentUserData, IncidentResponseData]], UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Response with a single incident postmortem.

        :param data: The postmortem resource.
        :type data: IncidentPostmortemData

        :param included: Related objects included in the response.
        :type included: [IncidentPostmortemIncluded], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
