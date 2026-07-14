# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.print_report_response_attributes import PrintReportResponseAttributes
    from datadog_api_client.v2.model.print_report_type import PrintReportType


class PrintReportResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.print_report_response_attributes import PrintReportResponseAttributes
        from datadog_api_client.v2.model.print_report_type import PrintReportType

        return {
            "attributes": (PrintReportResponseAttributes,),
            "id": (UUID,),
            "type": (PrintReportType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: PrintReportResponseAttributes, id: UUID, type: PrintReportType, **kwargs):
        """
        The JSON:API data object for a print-only report.

        :param attributes: The configuration and download URL for the initiated print-only report.
        :type attributes: PrintReportResponseAttributes

        :param id: The unique identifier of the report.
        :type id: UUID

        :param type: JSON:API resource type for a print-only report.
        :type type: PrintReportType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
