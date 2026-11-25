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
    from datadog_api_client.v2.model.observability_pipeline_client_identity_rule import (
        ObservabilityPipelineClientIdentityRule,
    )


class ObservabilityPipelineClientIdentityAllowlist(ModelNormal):
    validations = {
        "rules": {
            "max_items": 1000,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_client_identity_rule import (
            ObservabilityPipelineClientIdentityRule,
        )

        return {
            "rules": ([ObservabilityPipelineClientIdentityRule],),
        }

    attribute_map = {
        "rules": "rules",
    }

    def __init__(self_, rules: List[ObservabilityPipelineClientIdentityRule], **kwargs):
        """
        An allowlist of client identities. A client is allowed when any rule matches.

        :param rules: Rules, evaluated in order. The first matching rule is the one reported in metrics.
        :type rules: [ObservabilityPipelineClientIdentityRule]
        """
        super().__init__(kwargs)

        self_.rules = rules
