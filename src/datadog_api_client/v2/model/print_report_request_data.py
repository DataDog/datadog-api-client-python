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
    from datadog_api_client.v2.model.print_report_request_attributes import PrintReportRequestAttributes
    from datadog_api_client.v2.model.print_report_type import PrintReportType


class PrintReportRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.print_report_request_attributes import PrintReportRequestAttributes
        from datadog_api_client.v2.model.print_report_type import PrintReportType

        return {
            "attributes": (PrintReportRequestAttributes,),
            "type": (PrintReportType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: PrintReportRequestAttributes, type: PrintReportType, **kwargs):
        """
        The JSON:API data object for a print report request.

        :param attributes: The configuration for a print-only report. Specify exactly one of ``timeframe`` (for a
            relative time window) or both ``from_ts`` and ``to_ts`` (for an absolute time range).
        :type attributes: PrintReportRequestAttributes

        :param type: JSON:API resource type for a print-only report.
        :type type: PrintReportType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
