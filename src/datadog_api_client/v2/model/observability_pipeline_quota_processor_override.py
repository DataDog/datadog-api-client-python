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
    from datadog_api_client.v2.model.observability_pipeline_field_value import ObservabilityPipelineFieldValue
    from datadog_api_client.v2.model.observability_pipeline_quota_processor_limit import (
        ObservabilityPipelineQuotaProcessorLimit,
    )


class ObservabilityPipelineQuotaProcessorOverride(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_field_value import ObservabilityPipelineFieldValue
        from datadog_api_client.v2.model.observability_pipeline_quota_processor_limit import (
            ObservabilityPipelineQuotaProcessorLimit,
        )

        return {
            "fields": ([ObservabilityPipelineFieldValue],),
            "limit": (ObservabilityPipelineQuotaProcessorLimit,),
        }

    attribute_map = {
        "fields": "fields",
        "limit": "limit",
    }

    def __init__(
        self_, fields: List[ObservabilityPipelineFieldValue], limit: ObservabilityPipelineQuotaProcessorLimit, **kwargs
    ):
        """
        Defines a custom quota limit that applies to specific log events based on matching field values.

        :param fields: A list of field matchers used to apply a specific override. If an event matches all listed key-value pairs, the corresponding override limit is enforced.
        :type fields: [ObservabilityPipelineFieldValue]

        :param limit: The maximum amount of data or number of events allowed before the quota is enforced. Can be specified in bytes or events.
        :type limit: ObservabilityPipelineQuotaProcessorLimit
        """
        super().__init__(kwargs)

        self_.fields = fields
        self_.limit = limit
