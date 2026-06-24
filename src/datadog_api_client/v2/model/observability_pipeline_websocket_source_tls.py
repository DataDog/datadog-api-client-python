# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ObservabilityPipelineWebsocketSourceTls(ModelComposed):
    def __init__(self, **kwargs):
        """
        TLS configuration for the WebSocket source. Use ``enabled`` for standard ``wss://`` connections, or ``with_client_cert`` to present a client certificate for mutual TLS.

        :param mode: TLS mode. Must be `enabled`.
        :type mode: ObservabilityPipelineWebsocketSourceTlsEnabledMode

        :param ca_file: Path to the Certificate Authority (CA) file used to validate the remote server's TLS certificate.
        :type ca_file: str, optional

        :param crt_file: Path to the TLS client certificate file used to identify this source to the remote server.
        :type crt_file: str

        :param key_file: Path to the private key file associated with the client certificate.
        :type key_file: str, optional

        :param key_pass_key: Name of the environment variable or secret that holds the passphrase for the private key file.
        :type key_pass_key: str, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.observability_pipeline_websocket_source_tls_enabled import (
            ObservabilityPipelineWebsocketSourceTlsEnabled,
        )
        from datadog_api_client.v2.model.observability_pipeline_websocket_source_tls_with_client_cert import (
            ObservabilityPipelineWebsocketSourceTlsWithClientCert,
        )

        return {
            "oneOf": [
                ObservabilityPipelineWebsocketSourceTlsEnabled,
                ObservabilityPipelineWebsocketSourceTlsWithClientCert,
            ],
        }
