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
    from datadog_api_client.v2.model.finding_service_now_ticket_result import FindingServiceNowTicketResult


class FindingServiceNowTicket(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.finding_service_now_ticket_result import FindingServiceNowTicketResult

        return {
            "result": (FindingServiceNowTicketResult,),
            "status": (str,),
        }

    attribute_map = {
        "result": "result",
        "status": "status",
    }

    def __init__(
        self_,
        result: Union[FindingServiceNowTicketResult, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        ServiceNow ticket associated with the case.

        :param result: Result of the ServiceNow ticket creation or attachment.
        :type result: FindingServiceNowTicketResult, optional

        :param status: Status of the ServiceNow ticket operation. Can be "COMPLETED" if successful, or "FAILED" if the operation failed.
        :type status: str, optional
        """
        if result is not unset:
            kwargs["result"] = result
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
