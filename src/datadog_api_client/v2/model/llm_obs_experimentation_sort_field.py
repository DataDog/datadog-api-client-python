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
    from datadog_api_client.v2.model.llm_obs_experimentation_sort_field_direction import (
        LLMObsExperimentationSortFieldDirection,
    )


class LLMObsExperimentationSortField(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experimentation_sort_field_direction import (
            LLMObsExperimentationSortFieldDirection,
        )

        return {
            "direction": (LLMObsExperimentationSortFieldDirection,),
            "field": (str,),
        }

    attribute_map = {
        "direction": "direction",
        "field": "field",
    }

    def __init__(
        self_, field: str, direction: Union[LLMObsExperimentationSortFieldDirection, UnsetType] = unset, **kwargs
    ):
        """
        A field and direction to sort results by.

        :param direction: Sort direction.
        :type direction: LLMObsExperimentationSortFieldDirection, optional

        :param field: The field name to sort on.
        :type field: str
        """
        if direction is not unset:
            kwargs["direction"] = direction
        super().__init__(kwargs)

        self_.field = field
