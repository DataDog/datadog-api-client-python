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


class FunnelRequestDataAttributesSearchStepsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "facet": (str,),
            "step_filter": (str,),
            "value": (str,),
        }

    attribute_map = {
        "facet": "facet",
        "step_filter": "step_filter",
        "value": "value",
    }

    def __init__(
        self_,
        facet: Union[str, UnsetType] = unset,
        step_filter: Union[str, UnsetType] = unset,
        value: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param facet:
        :type facet: str, optional

        :param step_filter:
        :type step_filter: str, optional

        :param value:
        :type value: str, optional
        """
        if facet is not unset:
            kwargs["facet"] = facet
        if step_filter is not unset:
            kwargs["step_filter"] = step_filter
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
