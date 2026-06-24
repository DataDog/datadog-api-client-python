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
    from datadog_api_client.v2.model.observability_pipeline_websocket_source_tls_enabled_mode import (
        ObservabilityPipelineWebsocketSourceTlsEnabledMode,
    )


class ObservabilityPipelineWebsocketSourceTlsEnabled(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_websocket_source_tls_enabled_mode import (
            ObservabilityPipelineWebsocketSourceTlsEnabledMode,
        )

        return {
            "mode": (ObservabilityPipelineWebsocketSourceTlsEnabledMode,),
        }

    attribute_map = {
        "mode": "mode",
    }

    def __init__(self_, mode: ObservabilityPipelineWebsocketSourceTlsEnabledMode, **kwargs):
        """
        TLS configuration that enables encryption without a client certificate. Use this for standard ``wss://`` connections that do not require mutual TLS.

        :param mode: TLS mode. Must be ``enabled``.
        :type mode: ObservabilityPipelineWebsocketSourceTlsEnabledMode
        """
        super().__init__(kwargs)

        self_.mode = mode
