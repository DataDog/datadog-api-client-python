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
    from datadog_api_client.v2.model.update_outcomes_async_attributes import UpdateOutcomesAsyncAttributes
    from datadog_api_client.v2.model.update_outcomes_async_type import UpdateOutcomesAsyncType


class UpdateOutcomesAsyncRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_outcomes_async_attributes import UpdateOutcomesAsyncAttributes
        from datadog_api_client.v2.model.update_outcomes_async_type import UpdateOutcomesAsyncType

        return {
            "attributes": (UpdateOutcomesAsyncAttributes,),
            "type": (UpdateOutcomesAsyncType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[UpdateOutcomesAsyncAttributes, UnsetType] = unset,
        type: Union[UpdateOutcomesAsyncType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Scorecard outcomes batch request data.

        :param attributes: The JSON:API attributes for a batched set of scorecard outcomes.
        :type attributes: UpdateOutcomesAsyncAttributes, optional

        :param type: The JSON:API type for scorecard outcomes.
        :type type: UpdateOutcomesAsyncType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
