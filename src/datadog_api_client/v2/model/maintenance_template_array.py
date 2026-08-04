# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.maintenance_template_data import MaintenanceTemplateData
    from datadog_api_client.v2.model.degradation_included import DegradationIncluded
    from datadog_api_client.v2.model.status_pages_user import StatusPagesUser
    from datadog_api_client.v2.model.status_page_as_included import StatusPageAsIncluded


class MaintenanceTemplateArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.maintenance_template_data import MaintenanceTemplateData
        from datadog_api_client.v2.model.degradation_included import DegradationIncluded

        return {
            "data": ([MaintenanceTemplateData],),
            "included": ([DegradationIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: List[MaintenanceTemplateData],
        included: Union[List[Union[DegradationIncluded, StatusPagesUser, StatusPageAsIncluded]], UnsetType] = unset,
        **kwargs,
    ):
        """
        Response object for a list of maintenance templates.

        :param data: A list of maintenance template data objects.
        :type data: [MaintenanceTemplateData]

        :param included: The included related resources of a maintenance template. Client must explicitly request these resources by name in the ``include`` query parameter.
        :type included: [DegradationIncluded], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
