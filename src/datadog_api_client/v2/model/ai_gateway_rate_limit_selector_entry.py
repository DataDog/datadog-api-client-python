# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class AiGatewayRateLimitSelectorEntry(ModelNormal):
    validations = {
        "values": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "dim": (str,),
            "per_value": (bool,),
            "values": ([str],),
        }

    attribute_map = {
        "dim": "dim",
        "per_value": "per_value",
        "values": "values",
    }

    def __init__(self_, dim: str, values: Union[List[str], UnsetType] = unset, **kwargs):
        """
        One dimension rule in a template rate limit selector.

        :param dim: . role:: raw-html-m2r(raw)
               :format: html

            Dimension to match: user_id, team_id, model, provider, or tag: :raw-html-m2r:`<key>`. Reserved metadata tag keys are rejected.
        :type dim: str

        :param per_value: Give each matched value its own allowance when true. Otherwise, matched values share the allowance within the other separated dimensions.
        :type per_value: bool

        :param values: Allowed dimension values. Omit to match any value; with per_value true, a request must still carry the dimension to match. An explicit list must contain at least one value. Listed team_id values must be existing Teams without open membership.
        :type values: [str], optional
        """
        if values is not unset:
            kwargs["values"] = values
        super().__init__(kwargs)
        per_value = kwargs.get("per_value", False)

        self_.dim = dim
        self_.per_value = per_value
