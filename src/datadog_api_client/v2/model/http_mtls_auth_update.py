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
    from datadog_api_client.v2.model.http_mtls_auth_type import HTTPMtlsAuthType


class HTTPMtlsAuthUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.http_mtls_auth_type import HTTPMtlsAuthType

        return {
            "certificate": (str,),
            "private_key": (str,),
            "type": (HTTPMtlsAuthType,),
        }

    attribute_map = {
        "certificate": "certificate",
        "private_key": "private_key",
        "type": "type",
    }

    def __init__(
        self_,
        type: HTTPMtlsAuthType,
        certificate: Union[str, UnsetType] = unset,
        private_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``HTTPMtlsAuth`` object.

        :param certificate: Certificate of authority used to sign the request.
        :type certificate: str, optional

        :param private_key: Private key used for the MTLS handshake
        :type private_key: str, optional

        :param type: The definition of the ``HTTPMtlsAuth`` object.
        :type type: HTTPMtlsAuthType
        """
        if certificate is not unset:
            kwargs["certificate"] = certificate
        if private_key is not unset:
            kwargs["private_key"] = private_key
        super().__init__(kwargs)

        self_.type = type
