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
    from datadog_api_client.v2.model.incident_handle_data_response import IncidentHandleDataResponse
    from datadog_api_client.v2.model.incident_handle_included_item_response import IncidentHandleIncludedItemResponse
    from datadog_api_client.v2.model.incident_user_data import IncidentUserData
    from datadog_api_client.v2.model.incident_type_object import IncidentTypeObject


class IncidentHandleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_handle_data_response import IncidentHandleDataResponse
        from datadog_api_client.v2.model.incident_handle_included_item_response import (
            IncidentHandleIncludedItemResponse,
        )

        return {
            "data": (IncidentHandleDataResponse,),
            "included": ([IncidentHandleIncludedItemResponse],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: IncidentHandleDataResponse,
        included: Union[
            List[Union[IncidentHandleIncludedItemResponse, IncidentUserData, IncidentTypeObject]], UnsetType
        ] = unset,
        **kwargs,
    ):
        """


        :param data:
        :type data: IncidentHandleDataResponse

        :param included: Included related resources
        :type included: [IncidentHandleIncludedItemResponse], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
