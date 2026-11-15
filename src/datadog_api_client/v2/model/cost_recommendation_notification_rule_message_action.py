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


class CostRecommendationNotificationRuleMessageAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "bulk": (bool,),
            "per_rec": (bool,),
        }

    attribute_map = {
        "bulk": "bulk",
        "per_rec": "per_rec",
    }

    def __init__(self_, bulk: Union[bool, UnsetType] = unset, per_rec: Union[bool, UnsetType] = unset, **kwargs):
        """
        Where a message action appears.

        :param bulk: Whether the action appears once for the whole digest.
        :type bulk: bool, optional

        :param per_rec: Whether the action appears on each recommendation.
        :type per_rec: bool, optional
        """
        if bulk is not unset:
            kwargs["bulk"] = bulk
        if per_rec is not unset:
            kwargs["per_rec"] = per_rec
        super().__init__(kwargs)
