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
    from datadog_api_client.v2.model.observability_pipeline_client_identity import ObservabilityPipelineClientIdentity


class ObservabilityPipelineMtlsServerTlsWithClientIdentity(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_client_identity import (
            ObservabilityPipelineClientIdentity,
        )

        return {
            "ca_file": (str,),
            "client_identity": (ObservabilityPipelineClientIdentity,),
            "crt_file": (str,),
            "key_file": (str,),
            "key_pass_key": (str,),
            "verify_certificate": (bool,),
        }

    attribute_map = {
        "ca_file": "ca_file",
        "client_identity": "client_identity",
        "crt_file": "crt_file",
        "key_file": "key_file",
        "key_pass_key": "key_pass_key",
        "verify_certificate": "verify_certificate",
    }

    def __init__(
        self_,
        crt_file: str,
        ca_file: Union[str, UnsetType] = unset,
        client_identity: Union[ObservabilityPipelineClientIdentity, UnsetType] = unset,
        key_file: Union[str, UnsetType] = unset,
        key_pass_key: Union[str, UnsetType] = unset,
        verify_certificate: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration for enabling TLS encryption between the pipeline component and external connecting clients, or mutual TLS when ``verify_certificate`` is ``true``. Mutual TLS also enables an optional allowlist of client certificate identities.

        :param ca_file: Path to the Certificate Authority (CA) file used to validate connecting clients' TLS certificates.
        :type ca_file: str, optional

        :param client_identity: Restricts which clients may connect, based on the identities in their TLS certificate. Checks run during the TLS handshake, after the client certificate chain is validated against ``ca_file`` , and never relax that validation.
            Requires ``verify_certificate: true`` and ``ca_file``. Set exactly one of ``allowlist_file`` or ``allowlist``.
            When set, connections are closed after a maximum age of 300 seconds so that clients removed from the allowlist are disconnected.
            Requires Observability Pipelines Worker 2.27 or later.
        :type client_identity: ObservabilityPipelineClientIdentity, optional

        :param crt_file: Path to the TLS server certificate file used to identify the pipeline component to connecting clients.
        :type crt_file: str

        :param key_file: Path to the private key file associated with the TLS server certificate.
        :type key_file: str, optional

        :param key_pass_key: Name of the environment variable or secret that holds the passphrase for the private key file.
        :type key_pass_key: str, optional

        :param verify_certificate: When ``true`` , requires client connections to present a valid certificate, enabling mutual TLS authentication.
        :type verify_certificate: bool, optional
        """
        if ca_file is not unset:
            kwargs["ca_file"] = ca_file
        if client_identity is not unset:
            kwargs["client_identity"] = client_identity
        if key_file is not unset:
            kwargs["key_file"] = key_file
        if key_pass_key is not unset:
            kwargs["key_pass_key"] = key_pass_key
        if verify_certificate is not unset:
            kwargs["verify_certificate"] = verify_certificate
        super().__init__(kwargs)

        self_.crt_file = crt_file
