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
    from datadog_api_client.v2.model.rum_sdk_config_match_option import RumSdkConfigMatchOption
    from datadog_api_client.v2.model.rum_sdk_config_tracing_url_propagator_type import (
        RumSdkConfigTracingUrlPropagatorType,
    )


class RumSdkConfigTracingUrlConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_sdk_config_match_option import RumSdkConfigMatchOption
        from datadog_api_client.v2.model.rum_sdk_config_tracing_url_propagator_type import (
            RumSdkConfigTracingUrlPropagatorType,
        )

        return {
            "match": (RumSdkConfigMatchOption,),
            "propagator_types": ([RumSdkConfigTracingUrlPropagatorType],),
        }

    attribute_map = {
        "match": "match",
        "propagator_types": "propagator_types",
    }

    def __init__(
        self_, match: RumSdkConfigMatchOption, propagator_types: List[RumSdkConfigTracingUrlPropagatorType], **kwargs
    ):
        """
        Configuration for a URL that should have distributed tracing enabled.

        :param match: A match option used for URL or origin pattern matching.
        :type match: RumSdkConfigMatchOption

        :param propagator_types: The list of trace propagator types to use for this URL.
        :type propagator_types: [RumSdkConfigTracingUrlPropagatorType]
        """
        super().__init__(kwargs)

        self_.match = match
        self_.propagator_types = propagator_types
