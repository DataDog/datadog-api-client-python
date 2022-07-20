# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsCoreWebVitals(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "_cls": (float,),
            "lcp": (float,),
            "url": (str,),
        }

    attribute_map = {
        "_cls": "cls",
        "lcp": "lcp",
        "url": "url",
    }

    def __init__(self, *args, **kwargs):
        """
        Core Web Vitals attached to a browser test step.

        :param _cls: Cumulative Layout Shift.
        :type _cls: float, optional

        :param lcp: Largest Contentful Paint in milliseconds.
        :type lcp: float, optional

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
