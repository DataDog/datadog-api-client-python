# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_websocket_source_tls_with_client_cert_mode import (
        ObservabilityPipelineWebsocketSourceTlsWithClientCertMode,
    )


class ObservabilityPipelineWebsocketSourceTlsWithClientCert(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_websocket_source_tls_with_client_cert_mode import (
            ObservabilityPipelineWebsocketSourceTlsWithClientCertMode,
        )

        return {
            "ca_file": (str,),
            "crt_file": (str,),
            "key_file": (str,),
            "key_pass_key": (str,),
            "mode": (ObservabilityPipelineWebsocketSourceTlsWithClientCertMode,),
        }

    attribute_map = {
        "ca_file": "ca_file",
        "crt_file": "crt_file",
        "key_file": "key_file",
        "key_pass_key": "key_pass_key",
        "mode": "mode",
    }

    def __init__(
        self_,
        crt_file: str,
        mode: ObservabilityPipelineWebsocketSourceTlsWithClientCertMode,
        ca_file: Union[str, UnsetType] = unset,
        key_file: Union[str, UnsetType] = unset,
        key_pass_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        TLS configuration that enables encryption and presents a client certificate for mutual TLS authentication.

        :param ca_file: Path to the Certificate Authority (CA) file used to validate the remote server's TLS certificate.
        :type ca_file: str, optional

        :param crt_file: Path to the TLS client certificate file used to identify this source to the remote server.
        :type crt_file: str

        :param key_file: Path to the private key file associated with the client certificate.
        :type key_file: str, optional

        :param key_pass_key: Name of the environment variable or secret that holds the passphrase for the private key file.
        :type key_pass_key: str, optional

        :param mode: TLS mode. Must be ``with_client_cert``.
        :type mode: ObservabilityPipelineWebsocketSourceTlsWithClientCertMode
        """
        if ca_file is not unset:
            kwargs["ca_file"] = ca_file
        if key_file is not unset:
            kwargs["key_file"] = key_file
        if key_pass_key is not unset:
            kwargs["key_pass_key"] = key_pass_key
        super().__init__(kwargs)

        self_.crt_file = crt_file
        self_.mode = mode
