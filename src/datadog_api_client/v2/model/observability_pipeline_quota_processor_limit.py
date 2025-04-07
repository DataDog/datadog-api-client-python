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
    from datadog_api_client.v2.model.observability_pipeline_quota_processor_limit_enforce_type import (
        ObservabilityPipelineQuotaProcessorLimitEnforceType,
    )


class ObservabilityPipelineQuotaProcessorLimit(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_quota_processor_limit_enforce_type import (
            ObservabilityPipelineQuotaProcessorLimitEnforceType,
        )

        return {
            "enforce": (ObservabilityPipelineQuotaProcessorLimitEnforceType,),
            "limit": (int,),
        }

    attribute_map = {
        "enforce": "enforce",
        "limit": "limit",
    }

    def __init__(self_, enforce: ObservabilityPipelineQuotaProcessorLimitEnforceType, limit: int, **kwargs):
        """
        The maximum amount of data or number of events allowed before the quota is enforced. Can be specified in bytes or events.

        :param enforce: Unit for quota enforcement in bytes for data size or events for count.
        :type enforce: ObservabilityPipelineQuotaProcessorLimitEnforceType

        :param limit: The limit for quota enforcement.
        :type limit: int
        """
        super().__init__(kwargs)

        self_.enforce = enforce
        self_.limit = limit
