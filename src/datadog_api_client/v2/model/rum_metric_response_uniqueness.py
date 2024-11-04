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
    from datadog_api_client.v2.model.rum_metric_uniqueness_when import RumMetricUniquenessWhen


class RumMetricResponseUniqueness(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_metric_uniqueness_when import RumMetricUniquenessWhen

        return {
            "when": (RumMetricUniquenessWhen,),
        }

    attribute_map = {
        "when": "when",
    }

    def __init__(self_, when: Union[RumMetricUniquenessWhen, UnsetType] = unset, **kwargs):
        """
        The rule to count updatable events. Is only set if ``event_type`` is ``session`` or ``view``.

        :param when: When to count updatable events. ``match`` when the event is first seen, or ``end`` when the event is complete.
        :type when: RumMetricUniquenessWhen, optional
        """
        if when is not unset:
            kwargs["when"] = when
        super().__init__(kwargs)
