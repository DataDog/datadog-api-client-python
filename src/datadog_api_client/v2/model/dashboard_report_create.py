# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dashboard_report_create_attributes import DashboardReportCreateAttributes
    from datadog_api_client.v2.model.dashboard_report_type import DashboardReportType


class DashboardReportCreate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_report_create_attributes import DashboardReportCreateAttributes
        from datadog_api_client.v2.model.dashboard_report_type import DashboardReportType

        return {
            "attributes": (DashboardReportCreateAttributes,),
            "type": (DashboardReportType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: DashboardReportType,
        attributes: Union[DashboardReportCreateAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Schema for request body to create a dashboard report.

        :param attributes: Attributes for the dashboard report schema used to create a dashboard report.
        :type attributes: DashboardReportCreateAttributes, optional

        :param type: JSON:API type of the dashboard report.
        :type type: DashboardReportType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
