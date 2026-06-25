# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.report_schedule_resource_type import ReportScheduleResourceType
    from datadog_api_client.v2.model.report_schedule_index_template_variable import ReportScheduleIndexTemplateVariable


class ReportScheduleResourceAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.report_schedule_resource_type import ReportScheduleResourceType
        from datadog_api_client.v2.model.report_schedule_index_template_variable import (
            ReportScheduleIndexTemplateVariable,
        )

        return {
            "resource_type": (ReportScheduleResourceType,),
            "template_variables": ([ReportScheduleIndexTemplateVariable], none_type),
            "title": (str, none_type),
        }

    attribute_map = {
        "resource_type": "resource_type",
        "template_variables": "template_variables",
        "title": "title",
    }

    def __init__(
        self_,
        resource_type: ReportScheduleResourceType,
        template_variables: Union[List[ReportScheduleIndexTemplateVariable], none_type, UnsetType] = unset,
        title: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an included report target resource.

        :param resource_type: The type of dashboard resource the report schedule targets.
        :type resource_type: ReportScheduleResourceType

        :param template_variables: Template variable metadata from the dashboard resource, when available.
        :type template_variables: [ReportScheduleIndexTemplateVariable], none_type, optional

        :param title: The title of the dashboard or integration dashboard resource, when available.
        :type title: str, none_type, optional
        """
        if template_variables is not unset:
            kwargs["template_variables"] = template_variables
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)

        self_.resource_type = resource_type
