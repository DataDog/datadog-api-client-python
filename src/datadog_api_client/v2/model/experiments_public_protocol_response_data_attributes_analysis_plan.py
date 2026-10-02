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


class ExperimentsPublicProtocolResponseDataAttributesAnalysisPlan(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "compute_cuped": (bool,),
            "confidence_interval_method": (str,),
            "confidence_level": (float,),
            "multiple_testing_correction_method": (str,),
        }

    attribute_map = {
        "compute_cuped": "compute_cuped",
        "confidence_interval_method": "confidence_interval_method",
        "confidence_level": "confidence_level",
        "multiple_testing_correction_method": "multiple_testing_correction_method",
    }

    def __init__(
        self_,
        compute_cuped: Union[bool, UnsetType] = unset,
        confidence_interval_method: Union[str, UnsetType] = unset,
        confidence_level: Union[float, UnsetType] = unset,
        multiple_testing_correction_method: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Default statistical settings supplied by the protocol.

        :param compute_cuped: Whether to use pre-experiment data to reduce variance with CUPED.
        :type compute_cuped: bool, optional

        :param confidence_interval_method: Statistical method used to calculate confidence intervals.
        :type confidence_interval_method: str, optional

        :param confidence_level: Confidence level used by the statistical analysis.
        :type confidence_level: float, optional

        :param multiple_testing_correction_method: Method used to adjust for testing multiple metrics.
        :type multiple_testing_correction_method: str, optional
        """
        if compute_cuped is not unset:
            kwargs["compute_cuped"] = compute_cuped
        if confidence_interval_method is not unset:
            kwargs["confidence_interval_method"] = confidence_interval_method
        if confidence_level is not unset:
            kwargs["confidence_level"] = confidence_level
        if multiple_testing_correction_method is not unset:
            kwargs["multiple_testing_correction_method"] = multiple_testing_correction_method
        super().__init__(kwargs)
