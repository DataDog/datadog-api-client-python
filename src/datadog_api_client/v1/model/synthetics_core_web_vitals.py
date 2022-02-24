# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsCoreWebVitals(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "cls": (int,),
            "lcp": (int,),
            "url": (str,),
        }

    attribute_map = {
        "cls": "cls",
        "lcp": "lcp",
        "url": "url",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Core Web Vitals attached to a browser test step.

        :param cls: Cumulative Layout Shift.
        :type cls: int, optional

        :param lcp: Largest Contentful Paint in milliseconds.
        :type lcp: int, optional

        :param url: URL attached to the metrics.
        :type url: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsCoreWebVitals, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
