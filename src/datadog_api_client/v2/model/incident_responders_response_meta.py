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
    from datadog_api_client.v2.model.incident_responders_response_meta_page import IncidentRespondersResponseMetaPage
    from datadog_api_client.v2.model.incident_responders_pagination import IncidentRespondersPagination


class IncidentRespondersResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_responders_response_meta_page import (
            IncidentRespondersResponseMetaPage,
        )
        from datadog_api_client.v2.model.incident_responders_pagination import IncidentRespondersPagination

        return {
            "page": (IncidentRespondersResponseMetaPage,),
            "pagination": (IncidentRespondersPagination,),
        }

    attribute_map = {
        "page": "page",
        "pagination": "pagination",
    }

    def __init__(
        self_,
        page: Union[IncidentRespondersResponseMetaPage, UnsetType] = unset,
        pagination: Union[IncidentRespondersPagination, UnsetType] = unset,
        **kwargs,
    ):
        """
        Pagination metadata for the responder list.

        :param page: Total count for the responder list.
        :type page: IncidentRespondersResponseMetaPage, optional

        :param pagination: Offset-based pagination for incident responders.
        :type pagination: IncidentRespondersPagination, optional
        """
        if page is not unset:
            kwargs["page"] = page
        if pagination is not unset:
            kwargs["pagination"] = pagination
        super().__init__(kwargs)
