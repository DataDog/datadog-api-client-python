# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsSSLCertificateIssuer(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "c": (str,),
            "cn": (str,),
            "l": (str,),
            "o": (str,),
            "ou": (str,),
            "st": (str,),
        }

    attribute_map = {
        "c": "C",
        "cn": "CN",
        "l": "L",
        "o": "O",
        "ou": "OU",
        "st": "ST",
    }

    def __init__(self, *args, **kwargs):
        """
        Object describing the issuer of a SSL certificate.

        :param c: Country Name that issued the certificate.
        :type c: str, optional

        :param cn: Common Name that issued certificate.
        :type cn: str, optional

        :param l: Locality that issued the certificate.
        :type l: str, optional

        :param o: Organization that issued the certificate.
        :type o: str, optional

        :param ou: Organizational Unit that issued the certificate.
        :type ou: str, optional

        :param st: State Or Province Name that issued the certificate.
        :type st: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsSSLCertificateIssuer, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
