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
    from datadog_api_client.v2.model.slo_report_post_request_attributes import SloReportPostRequestAttributes


class SLOReportPostRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.slo_report_post_request_attributes import SloReportPostRequestAttributes

        return {
            "attributes": (SloReportPostRequestAttributes,),
        }

    attribute_map = {
        "attributes": "attributes",
    }

    def __init__(self_, attributes: SloReportPostRequestAttributes, **kwargs):
        """
        The data portion of the SLO report request.

        :param attributes: The attributes portion of the SLO report request.
        :type attributes: SloReportPostRequestAttributes
        """
        super().__init__(kwargs)

        self_.attributes = attributes
