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
    from datadog_api_client.v2.model.dashboard_report_attributes import DashboardReportAttributes
    from datadog_api_client.v2.model.dashboard_report_relationships import DashboardReportRelationships
    from datadog_api_client.v2.model.dashboard_report_type import DashboardReportType


class DashboardReport(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_report_attributes import DashboardReportAttributes
        from datadog_api_client.v2.model.dashboard_report_relationships import DashboardReportRelationships
        from datadog_api_client.v2.model.dashboard_report_type import DashboardReportType

        return {
            "attributes": (DashboardReportAttributes,),
            "id": (str,),
            "relationships": (DashboardReportRelationships,),
            "type": (DashboardReportType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: DashboardReportType,
        attributes: Union[DashboardReportAttributes, UnsetType] = unset,
        relationships: Union[DashboardReportRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Dashboard report schema.

        :param attributes: Attributes for the dashboard report schema.
        :type attributes: DashboardReportAttributes, optional

        :param id: ID of the dashboard report.
        :type id: str

        :param relationships: Relationships of a dashboard report.
        :type relationships: DashboardReportRelationships, optional

        :param type: JSON:API type of the dashboard report.
        :type type: DashboardReportType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
