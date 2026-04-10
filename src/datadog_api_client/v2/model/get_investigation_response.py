# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.get_investigation_response_data import GetInvestigationResponseData
    from datadog_api_client.v2.model.get_investigation_response_links import GetInvestigationResponseLinks


class GetInvestigationResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_investigation_response_data import GetInvestigationResponseData
        from datadog_api_client.v2.model.get_investigation_response_links import GetInvestigationResponseLinks

        return {
            "data": (GetInvestigationResponseData,),
            "links": (GetInvestigationResponseLinks,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
    }

    def __init__(self_, data: GetInvestigationResponseData, links: GetInvestigationResponseLinks, **kwargs):
        """
        Response for a single Bits AI investigation.

        :param data: Data for the get investigation response.
        :type data: GetInvestigationResponseData

        :param links: Links related to the investigation.
        :type links: GetInvestigationResponseLinks
        """
        super().__init__(kwargs)

        self_.data = data
        self_.links = links
