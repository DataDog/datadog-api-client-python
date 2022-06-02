# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class SyntheticsSSLCertificate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_ssl_certificate_issuer import SyntheticsSSLCertificateIssuer
        from datadog_api_client.v1.model.synthetics_ssl_certificate_subject import SyntheticsSSLCertificateSubject

        return {
            "cipher": (str,),
            "exponent": (float,),
            "ext_key_usage": ([str],),
            "fingerprint": (str,),
            "fingerprint256": (str,),
            "issuer": (SyntheticsSSLCertificateIssuer,),
            "modulus": (str,),
            "protocol": (str,),
            "serial_number": (str,),
            "subject": (SyntheticsSSLCertificateSubject,),
            "valid_from": (datetime,),
            "valid_to": (datetime,),
        }

    attribute_map = {
        "cipher": "cipher",
        "exponent": "exponent",
        "ext_key_usage": "extKeyUsage",
        "fingerprint": "fingerprint",
        "fingerprint256": "fingerprint256",
        "issuer": "issuer",
        "modulus": "modulus",
        "protocol": "protocol",
        "serial_number": "serialNumber",
        "subject": "subject",
        "valid_from": "validFrom",
        "valid_to": "validTo",
    }

    def __init__(self, *args, **kwargs):
        """
        Object describing the SSL certificate used for a Synthetic test.

        :param cipher: Cipher used for the connection.
        :type cipher: str, optional

        :param exponent: Exponent associated to the certificate.
        :type exponent: float, optional

        :param ext_key_usage: Array of extensions and details used for the certificate.
        :type ext_key_usage: [str], optional

        :param fingerprint: MD5 digest of the DER-encoded Certificate information.
        :type fingerprint: str, optional

        :param fingerprint256: SHA-1 digest of the DER-encoded Certificate information.
        :type fingerprint256: str, optional

        :param issuer: Object describing the issuer of a SSL certificate.
        :type issuer: SyntheticsSSLCertificateIssuer, optional

        :param modulus: Modulus associated to the SSL certificate private key.
        :type modulus: str, optional

        :param protocol: TLS protocol used for the test.
        :type protocol: str, optional

        :param serial_number: Serial Number assigned by Symantec to the SSL certificate.
        :type serial_number: str, optional

        :param subject: Object describing the SSL certificate used for the test.
        :type subject: SyntheticsSSLCertificateSubject, optional

        :param valid_from: Date from which the SSL certificate is valid.
        :type valid_from: datetime, optional

        :param valid_to: Date until which the SSL certificate is valid.
        :type valid_to: datetime, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsSSLCertificate, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
