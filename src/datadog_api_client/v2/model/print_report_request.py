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
    from datadog_api_client.v2.model.print_report_request_data import PrintReportRequestData


class PrintReportRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.print_report_request_data import PrintReportRequestData

        return {
            "data": (PrintReportRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: PrintReportRequestData, **kwargs):
        """
        Request body for initiating a print-only report.

        :param data: The JSON:API data object for a print report request.
        :type data: PrintReportRequestData
        """
        super().__init__(kwargs)

        self_.data = data
