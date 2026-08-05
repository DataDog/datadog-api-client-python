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
    from datadog_api_client.v2.model.maintenance_template_data_relationships_status_page_data import (
        MaintenanceTemplateDataRelationshipsStatusPageData,
    )


class MaintenanceTemplateDataRelationshipsStatusPage(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.maintenance_template_data_relationships_status_page_data import (
            MaintenanceTemplateDataRelationshipsStatusPageData,
        )

        return {
            "data": (MaintenanceTemplateDataRelationshipsStatusPageData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: MaintenanceTemplateDataRelationshipsStatusPageData, **kwargs):
        """
        The status page the maintenance template belongs to.

        :param data: The data object identifying the status page associated with a maintenance template.
        :type data: MaintenanceTemplateDataRelationshipsStatusPageData
        """
        super().__init__(kwargs)

        self_.data = data
