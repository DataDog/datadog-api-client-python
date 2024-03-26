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
    from datadog_api_client.v2.model.slo_report_post_request_data import SLOReportPostRequestData


class SLOReportPostRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.slo_report_post_request_data import SLOReportPostRequestData

        return {
            "data": (SLOReportPostRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SLOReportPostRequestData, **kwargs):
        """
        The SLO report request body.

        :param data: The data portion of the SLO report request.
        :type data: SLOReportPostRequestData
        """
        super().__init__(kwargs)

        self_.data = data
