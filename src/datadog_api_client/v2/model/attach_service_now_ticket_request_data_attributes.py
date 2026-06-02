# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AttachServiceNowTicketRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "servicenow_ticket_url": (str,),
        }

    attribute_map = {
        "servicenow_ticket_url": "servicenow_ticket_url",
    }

    def __init__(self_, servicenow_ticket_url: str, **kwargs):
        """
        Attributes of the ServiceNow ticket to attach security findings to.

        :param servicenow_ticket_url: URL of the ServiceNow incident to attach security findings to. Must be a service-now.com URL pointing to an incident record.
        :type servicenow_ticket_url: str
        """
        super().__init__(kwargs)

        self_.servicenow_ticket_url = servicenow_ticket_url
