# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_test_result_certificate_validity import (
        SyntheticsTestResultCertificateValidity,
    )


class SyntheticsTestResultCertificate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_certificate_validity import (
            SyntheticsTestResultCertificateValidity,
        )

        return {
            "cipher": (str,),
            "exponent": (int,),
            "ext_key_usage": ([str],),
            "fingerprint": (str,),
            "fingerprint256": (str,),
            "issuer": ({str: (str,)},),
            "modulus": (str,),
            "protocol": (str,),
            "serial_number": (str,),
            "subject": ({str: (str,)},),
            "tls_version": (float,),
            "valid": (SyntheticsTestResultCertificateValidity,),
        }

    attribute_map = {
        "cipher": "cipher",
        "exponent": "exponent",
        "ext_key_usage": "ext_key_usage",
        "fingerprint": "fingerprint",
        "fingerprint256": "fingerprint256",
        "issuer": "issuer",
        "modulus": "modulus",
        "protocol": "protocol",
        "serial_number": "serial_number",
        "subject": "subject",
        "tls_version": "tls_version",
        "valid": "valid",
    }

    def __init__(
        self_,
        cipher: Union[str, UnsetType] = unset,
        exponent: Union[int, UnsetType] = unset,
        ext_key_usage: Union[List[str], UnsetType] = unset,
        fingerprint: Union[str, UnsetType] = unset,
        fingerprint256: Union[str, UnsetType] = unset,
        issuer: Union[Dict[str, str], UnsetType] = unset,
        modulus: Union[str, UnsetType] = unset,
        protocol: Union[str, UnsetType] = unset,
        serial_number: Union[str, UnsetType] = unset,
        subject: Union[Dict[str, str], UnsetType] = unset,
        tls_version: Union[float, UnsetType] = unset,
        valid: Union[SyntheticsTestResultCertificateValidity, UnsetType] = unset,
        **kwargs,
    ):
        """
        SSL/TLS certificate information returned from an SSL test.

        :param cipher: Cipher used for the TLS connection.
        :type cipher: str, optional

        :param exponent: RSA exponent of the certificate.
        :type exponent: int, optional

        :param ext_key_usage: Extended key usage extensions for the certificate.
        :type ext_key_usage: [str], optional

        :param fingerprint: SHA-1 fingerprint of the certificate.
        :type fingerprint: str, optional

        :param fingerprint256: SHA-256 fingerprint of the certificate.
        :type fingerprint256: str, optional

        :param issuer: Certificate issuer details.
        :type issuer: {str: (str,)}, optional

        :param modulus: RSA modulus of the certificate.
        :type modulus: str, optional

        :param protocol: TLS protocol used (for example, ``TLSv1.2`` ).
        :type protocol: str, optional

        :param serial_number: Serial number of the certificate.
        :type serial_number: str, optional

        :param subject: Certificate subject details.
        :type subject: {str: (str,)}, optional

        :param tls_version: TLS protocol version.
        :type tls_version: float, optional

        :param valid: Validity window of a certificate.
        :type valid: SyntheticsTestResultCertificateValidity, optional
        """
        if cipher is not unset:
            kwargs["cipher"] = cipher
        if exponent is not unset:
            kwargs["exponent"] = exponent
        if ext_key_usage is not unset:
            kwargs["ext_key_usage"] = ext_key_usage
        if fingerprint is not unset:
            kwargs["fingerprint"] = fingerprint
        if fingerprint256 is not unset:
            kwargs["fingerprint256"] = fingerprint256
        if issuer is not unset:
            kwargs["issuer"] = issuer
        if modulus is not unset:
            kwargs["modulus"] = modulus
        if protocol is not unset:
            kwargs["protocol"] = protocol
        if serial_number is not unset:
            kwargs["serial_number"] = serial_number
        if subject is not unset:
            kwargs["subject"] = subject
        if tls_version is not unset:
            kwargs["tls_version"] = tls_version
        if valid is not unset:
            kwargs["valid"] = valid
        super().__init__(kwargs)
