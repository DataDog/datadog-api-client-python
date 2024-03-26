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
    from datadog_api_client.v2.model.slo_report_status import SLOReportStatus


class SLOReportStatusGetResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.slo_report_status import SLOReportStatus

        return {
            "status": (SLOReportStatus,),
        }

    attribute_map = {
        "status": "status",
    }

    def __init__(self_, status: Union[SLOReportStatus, UnsetType] = unset, **kwargs):
        """
        The attributes portion of the SLO report status response.

        :param status: The status of the SLO report job.
        :type status: SLOReportStatus, optional
        """
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
