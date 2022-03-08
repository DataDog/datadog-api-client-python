# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsTestRequestCertificateItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "content": (str,),
            "filename": (str,),
            "updated_at": (str,),
        }

    attribute_map = {
        "content": "content",
        "filename": "filename",
        "updated_at": "updatedAt",
    }

    def __init__(self, *args, **kwargs):
        """
        Define a request certificate.

        :param content: Content of the certificate or key.
        :type content: str, optional

        :param filename: File name for the certificate or key.
        :type filename: str, optional

        :param updated_at: Date of update of the certificate or key, ISO format.
        :type updated_at: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsTestRequestCertificateItem, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
