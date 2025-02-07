# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.step_display_bounds import StepDisplayBounds


class StepDisplay(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.step_display_bounds import StepDisplayBounds

        return {
            "bounds": (StepDisplayBounds,),
        }

    attribute_map = {
        "bounds": "bounds",
    }

    def __init__(self_, bounds: Union[StepDisplayBounds, UnsetType] = unset, **kwargs):
        """
        The definition of ``StepDisplay`` object.

        :param bounds: The definition of ``StepDisplayBounds`` object.
        :type bounds: StepDisplayBounds, optional
        """
        if bounds is not unset:
            kwargs["bounds"] = bounds
        super().__init__(kwargs)
