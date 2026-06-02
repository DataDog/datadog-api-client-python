# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_service_now_ticket_request_data import CreateServiceNowTicketRequestData


class CreateServiceNowTicketRequestArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_service_now_ticket_request_data import CreateServiceNowTicketRequestData

        return {
            "data": ([CreateServiceNowTicketRequestData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[CreateServiceNowTicketRequestData], **kwargs):
        """
        List of requests to create ServiceNow tickets for security findings.

        :param data: Array of ServiceNow ticket creation request data objects.
        :type data: [CreateServiceNowTicketRequestData]
        """
        super().__init__(kwargs)

        self_.data = data
