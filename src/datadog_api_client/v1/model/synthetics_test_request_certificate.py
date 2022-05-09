# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_test_request_certificate_item import (
        SyntheticsTestRequestCertificateItem,
    )

    globals()["SyntheticsTestRequestCertificateItem"] = SyntheticsTestRequestCertificateItem


class SyntheticsTestRequestCertificate(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "cert": (SyntheticsTestRequestCertificateItem,),
            "key": (SyntheticsTestRequestCertificateItem,),
        }

    attribute_map = {
        "cert": "cert",
        "key": "key",
    }

    def __init__(self, *args, **kwargs):
        """
        Client certificate to use when performing the test request.

        :param cert: Define a request certificate.
        :type cert: SyntheticsTestRequestCertificateItem, optional

        :param key: Define a request certificate.
        :type key: SyntheticsTestRequestCertificateItem, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsTestRequestCertificate, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
