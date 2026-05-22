# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ObservabilityPipelineMtlsServerTls(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "ca_file": (str,),
            "crt_file": (str,),
            "key_file": (str,),
            "key_pass_key": (str,),
            "verify_certificate": (bool,),
        }

    attribute_map = {
        "ca_file": "ca_file",
        "crt_file": "crt_file",
        "key_file": "key_file",
        "key_pass_key": "key_pass_key",
        "verify_certificate": "verify_certificate",
    }

    def __init__(
        self_,
        crt_file: str,
        ca_file: Union[str, UnsetType] = unset,
        key_file: Union[str, UnsetType] = unset,
        key_pass_key: Union[str, UnsetType] = unset,
        verify_certificate: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration for enabling TLS encryption between the pipeline component and external connecting clients.

        :param ca_file: Path to the Certificate Authority (CA) file used to validate connecting clients' TLS certificates.
        :type ca_file: str, optional

        :param crt_file: Path to the TLS server certificate file used to used to identify the pipeline component to connecting clients.
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
        if key_file is not unset:
            kwargs["key_file"] = key_file
        if key_pass_key is not unset:
            kwargs["key_pass_key"] = key_pass_key
        if verify_certificate is not unset:
            kwargs["verify_certificate"] = verify_certificate
        super().__init__(kwargs)

        self_.crt_file = crt_file
