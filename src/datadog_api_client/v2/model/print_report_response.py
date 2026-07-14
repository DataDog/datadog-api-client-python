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
    from datadog_api_client.v2.model.print_report_response_data import PrintReportResponseData


class PrintReportResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.print_report_response_data import PrintReportResponseData

        return {
            "data": (PrintReportResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: PrintReportResponseData, **kwargs):
        """
        Response containing the initiated print-only report.

        :param data: The JSON:API data object for a print-only report.
        :type data: PrintReportResponseData
        """
        super().__init__(kwargs)

        self_.data = data
