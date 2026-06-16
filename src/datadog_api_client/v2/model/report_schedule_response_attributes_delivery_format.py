# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ReportScheduleResponseAttributesDeliveryFormat(ModelSimple):
    """
    The delivery format for dashboard report schedules, or `null` if not set.

    :param value: Must be one of ["pdf", "png", "pdf_and_png"].
    :type value: str
    """

    allowed_values = {
        "pdf",
        "png",
        "pdf_and_png",
    }
    PDF: ClassVar["ReportScheduleResponseAttributesDeliveryFormat"]
    PNG: ClassVar["ReportScheduleResponseAttributesDeliveryFormat"]
    PDF_AND_PNG: ClassVar["ReportScheduleResponseAttributesDeliveryFormat"]

    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ReportScheduleResponseAttributesDeliveryFormat.PDF = ReportScheduleResponseAttributesDeliveryFormat("pdf")
ReportScheduleResponseAttributesDeliveryFormat.PNG = ReportScheduleResponseAttributesDeliveryFormat("png")
ReportScheduleResponseAttributesDeliveryFormat.PDF_AND_PNG = ReportScheduleResponseAttributesDeliveryFormat(
    "pdf_and_png"
)
