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
    from datadog_api_client.v2.model.attach_service_now_ticket_request_data import AttachServiceNowTicketRequestData


class AttachServiceNowTicketRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.attach_service_now_ticket_request_data import AttachServiceNowTicketRequestData

        return {
            "data": (AttachServiceNowTicketRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AttachServiceNowTicketRequestData, **kwargs):
        """
        Request for attaching security findings to a ServiceNow ticket.

        :param data: Data of the ServiceNow ticket to attach security findings to.
        :type data: AttachServiceNowTicketRequestData
        """
        super().__init__(kwargs)

        self_.data = data
