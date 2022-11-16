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
    from datadog_api_client.v2.model.dashboard_report_destination_email import DashboardReportDestinationEmail


class DashboardReportDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_report_destination_email import DashboardReportDestinationEmail

        return {
            "email": (DashboardReportDestinationEmail,),
        }

    attribute_map = {
        "email": "email",
    }

    def __init__(self_, email: Union[DashboardReportDestinationEmail, UnsetType] = unset, **kwargs):
        """
        Report destination-specific configuration. This determines how reports are sent. Only email destinations are supported.

        :param email: Email destinations for a report.
        :type email: DashboardReportDestinationEmail, optional
        """
        if email is not unset:
            kwargs["email"] = email
        super().__init__(kwargs)
