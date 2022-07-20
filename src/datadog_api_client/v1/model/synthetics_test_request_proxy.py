# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsTestRequestProxy(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_test_headers import SyntheticsTestHeaders

        return {
            "headers": (SyntheticsTestHeaders,),
            "url": (str,),
        }

    attribute_map = {
        "headers": "headers",
        "url": "url",
    }

    def __init__(self, url, *args, **kwargs):
        """
        The proxy to perform the test.

        :param headers: Headers to include when performing the test.
        :type headers: SyntheticsTestHeaders, optional

        :param url: URL of the proxy to perform the test.
        :type url: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.url = url

    @classmethod
    def _from_openapi_data(cls, url, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsTestRequestProxy, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.url = url
        return self
