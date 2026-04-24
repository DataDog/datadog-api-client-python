# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SyntheticsTestResultVitalsMetrics(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "_cls": (float,),
            "fcp": (float,),
            "inp": (float,),
            "lcp": (float,),
            "ttfb": (float,),
            "url": (str,),
        }

    attribute_map = {
        "_cls": "cls",
        "fcp": "fcp",
        "inp": "inp",
        "lcp": "lcp",
        "ttfb": "ttfb",
        "url": "url",
    }

    def __init__(
        self_,
        _cls: Union[float, UnsetType] = unset,
        fcp: Union[float, UnsetType] = unset,
        inp: Union[float, UnsetType] = unset,
        lcp: Union[float, UnsetType] = unset,
        ttfb: Union[float, UnsetType] = unset,
        url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Web vitals metrics captured during a browser test step.

        :param _cls: Cumulative Layout Shift score.
        :type _cls: float, optional

        :param fcp: First Contentful Paint in milliseconds.
        :type fcp: float, optional

        :param inp: Interaction to Next Paint in milliseconds.
        :type inp: float, optional

        :param lcp: Largest Contentful Paint in milliseconds.
        :type lcp: float, optional

        :param ttfb: Time To First Byte in milliseconds.
        :type ttfb: float, optional

        :param url: URL that produced the metrics.
        :type url: str, optional
        """
        if _cls is not unset:
            kwargs["_cls"] = _cls
        if fcp is not unset:
            kwargs["fcp"] = fcp
        if inp is not unset:
            kwargs["inp"] = inp
        if lcp is not unset:
            kwargs["lcp"] = lcp
        if ttfb is not unset:
            kwargs["ttfb"] = ttfb
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)
