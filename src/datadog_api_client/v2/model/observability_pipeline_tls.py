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


class ObservabilityPipelineTls(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "ca_file": (str,),
            "crt_file": (str,),
            "key_file": (str,),
            "key_pass_key": (str,),
        }

    attribute_map = {
        "ca_file": "ca_file",
        "crt_file": "crt_file",
        "key_file": "key_file",
        "key_pass_key": "key_pass_key",
    }

    def __init__(
        self_,
        crt_file: str,
        ca_file: Union[str, UnsetType] = unset,
        key_file: Union[str, UnsetType] = unset,
        key_pass_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration for enabling TLS encryption between the pipeline component and external services.

        :param ca_file: Path to the Certificate Authority (CA) file used to validate the server’s TLS certificate.
        :type ca_file: str, optional

        :param crt_file: Path to the TLS client certificate file used to authenticate the pipeline component with upstream or downstream services.
        :type crt_file: str

        :param key_file: Path to the private key file associated with the TLS client certificate. Used for mutual TLS authentication.
        :type key_file: str, optional

        :param key_pass_key: Name of the environment variable or secret that holds the passphrase for the private key file.
        :type key_pass_key: str, optional
        """
        if ca_file is not unset:
            kwargs["ca_file"] = ca_file
        if key_file is not unset:
            kwargs["key_file"] = key_file
        if key_pass_key is not unset:
            kwargs["key_pass_key"] = key_pass_key
        super().__init__(kwargs)

        self_.crt_file = crt_file
