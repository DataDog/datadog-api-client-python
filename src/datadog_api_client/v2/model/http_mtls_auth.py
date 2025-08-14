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
    from datadog_api_client.v2.model.http_mtls_auth_type import HTTPMtlsAuthType


class HTTPMtlsAuth(ModelNormal):
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

    def __init__(self_, certificate: str, private_key: str, type: HTTPMtlsAuthType, **kwargs):
        """
        The definition of the ``HTTPMtlsAuth`` object.

        :param certificate: Certificate of authority used to sign the request.
        :type certificate: str

        :param private_key: Private key used for the MTLS handshake
        :type private_key: str

        :param type: The definition of the ``HTTPMtlsAuth`` object.
        :type type: HTTPMtlsAuthType
        """
        super().__init__(kwargs)

        self_.certificate = certificate
        self_.private_key = private_key
        self_.type = type
