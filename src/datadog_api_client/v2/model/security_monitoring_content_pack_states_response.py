# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_content_pack_state_data import (
        SecurityMonitoringContentPackStateData,
    )
    from datadog_api_client.v2.model.security_monitoring_content_pack_state_meta import (
        SecurityMonitoringContentPackStateMeta,
    )


class SecurityMonitoringContentPackStatesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_content_pack_state_data import (
            SecurityMonitoringContentPackStateData,
        )
        from datadog_api_client.v2.model.security_monitoring_content_pack_state_meta import (
            SecurityMonitoringContentPackStateMeta,
        )

        return {
            "data": ([SecurityMonitoringContentPackStateData],),
            "meta": (SecurityMonitoringContentPackStateMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[SecurityMonitoringContentPackStateData],
        meta: SecurityMonitoringContentPackStateMeta,
        **kwargs,
    ):
        """
        Response containing content pack states.

        :param data: Array of content pack states.
        :type data: [SecurityMonitoringContentPackStateData]

        :param meta: Metadata for content pack states
        :type meta: SecurityMonitoringContentPackStateMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
