# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ReportScheduleDeliveryFormat(ModelSimple):
    """
    How a PDF-export report is delivered. `pdf` attaches a PDF file, `png` embeds
        an inline PNG image, and `pdf_and_png` delivers both.

    :param value: Must be one of ["pdf", "png", "pdf_and_png"].
    :type value: str
    """

    allowed_values = {
        "pdf",
        "png",
        "pdf_and_png",
    }
    PDF: ClassVar["ReportScheduleDeliveryFormat"]
    PNG: ClassVar["ReportScheduleDeliveryFormat"]
    PDF_AND_PNG: ClassVar["ReportScheduleDeliveryFormat"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ReportScheduleDeliveryFormat.PDF = ReportScheduleDeliveryFormat("pdf")
ReportScheduleDeliveryFormat.PNG = ReportScheduleDeliveryFormat("png")
ReportScheduleDeliveryFormat.PDF_AND_PNG = ReportScheduleDeliveryFormat("pdf_and_png")
