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
    from datadog_api_client.v2.model.degradation_update_data_relationships_status_page_data import (
        DegradationUpdateDataRelationshipsStatusPageData,
    )


class DegradationUpdateDataRelationshipsStatusPage(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.degradation_update_data_relationships_status_page_data import (
            DegradationUpdateDataRelationshipsStatusPageData,
        )

        return {
            "data": (DegradationUpdateDataRelationshipsStatusPageData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: DegradationUpdateDataRelationshipsStatusPageData, **kwargs):
        """
        The status page relationship of a degradation update.

        :param data: The status page linked to a degradation update.
        :type data: DegradationUpdateDataRelationshipsStatusPageData
        """
        super().__init__(kwargs)

        self_.data = data
