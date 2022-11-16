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
    from datadog_api_client.v2.model.dashboard_report_update_attributes import DashboardReportUpdateAttributes
    from datadog_api_client.v2.model.dashboard_report_type import DashboardReportType


class DashboardReportUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_report_update_attributes import DashboardReportUpdateAttributes
        from datadog_api_client.v2.model.dashboard_report_type import DashboardReportType

        return {
            "attributes": (DashboardReportUpdateAttributes,),
            "id": (str,),
            "type": (DashboardReportType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: DashboardReportType,
        attributes: Union[DashboardReportUpdateAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON:API data key.

        :param attributes: Attributes of a dashboard report that can be updated. Fields that are not to be updated can be omitted, with some exceptions for ``repeat_on_day_of_week`` and ``repeat_on_day_of_month`` , as noted in their respective sections.
        :type attributes: DashboardReportUpdateAttributes, optional

        :param id: ID of the report to update.
        :type id: str

        :param type: JSON:API type of the dashboard report.
        :type type: DashboardReportType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
