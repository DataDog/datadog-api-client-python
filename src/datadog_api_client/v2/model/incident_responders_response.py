# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_responder_data_response import IncidentResponderDataResponse
    from datadog_api_client.v2.model.incident_responder_included_item import IncidentResponderIncludedItem
    from datadog_api_client.v2.model.incident_responders_response_meta import IncidentRespondersResponseMeta
    from datadog_api_client.v2.model.incident_user_data import IncidentUserData
    from datadog_api_client.v2.model.incident_role_assignment_data_response import IncidentRoleAssignmentDataResponse


class IncidentRespondersResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_responder_data_response import IncidentResponderDataResponse
        from datadog_api_client.v2.model.incident_responder_included_item import IncidentResponderIncludedItem
        from datadog_api_client.v2.model.incident_responders_response_meta import IncidentRespondersResponseMeta

        return {
            "data": ([IncidentResponderDataResponse],),
            "included": ([IncidentResponderIncludedItem],),
            "links": ({str: (str,)},),
            "meta": (IncidentRespondersResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "links": "links",
        "meta": "meta",
    }
    read_only_vars = {
        "included",
    }

    def __init__(
        self_,
        data: List[IncidentResponderDataResponse],
        included: Union[
            List[Union[IncidentResponderIncludedItem, IncidentUserData, IncidentRoleAssignmentDataResponse]], UnsetType
        ] = unset,
        links: Union[Dict[str, str], UnsetType] = unset,
        meta: Union[IncidentRespondersResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response with a list of incident responders.

        :param data: List of incident responders.
        :type data: [IncidentResponderDataResponse]

        :param included: Included related resources.
        :type included: [IncidentResponderIncludedItem], optional

        :param links: Links to pages of incident responders.
        :type links: {str: (str,)}, optional

        :param meta: Pagination metadata for the responder list.
        :type meta: IncidentRespondersResponseMeta, optional
        """
        if included is not unset:
            kwargs["included"] = included
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
