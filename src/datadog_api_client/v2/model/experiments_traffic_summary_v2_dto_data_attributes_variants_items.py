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


class ExperimentsTrafficSummaryV2DTODataAttributesVariantsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "exposure_count": (int,),
            "variant_key": (str,),
            "variant_name": (str,),
        }

    attribute_map = {
        "exposure_count": "exposure_count",
        "variant_key": "variant_key",
        "variant_name": "variant_name",
    }

    def __init__(
        self_,
        exposure_count: Union[int, UnsetType] = unset,
        variant_key: Union[str, UnsetType] = unset,
        variant_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Exposure count and identity of one experiment variant.

        :param exposure_count: Number of recorded exposures for this variant.
        :type exposure_count: int, optional

        :param variant_key: Key that identifies the experiment variant.
        :type variant_key: str, optional

        :param variant_name: Display name of the experiment variant.
        :type variant_name: str, optional
        """
        if exposure_count is not unset:
            kwargs["exposure_count"] = exposure_count
        if variant_key is not unset:
            kwargs["variant_key"] = variant_key
        if variant_name is not unset:
            kwargs["variant_name"] = variant_name
        super().__init__(kwargs)
