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
    from datadog_api_client.v2.model.rule_version_update_type import RuleVersionUpdateType


class RuleVersionUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rule_version_update_type import RuleVersionUpdateType

        return {
            "change": (str,),
            "field": (str,),
            "type": (RuleVersionUpdateType,),
        }

    attribute_map = {
        "change": "change",
        "field": "field",
        "type": "type",
    }

    def __init__(
        self_,
        change: Union[str, UnsetType] = unset,
        field: Union[str, UnsetType] = unset,
        type: Union[RuleVersionUpdateType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A change in a rule version.

        :param change: The new value of the field.
        :type change: str, optional

        :param field: The field that was changed.
        :type field: str, optional

        :param type: The type of change.
        :type type: RuleVersionUpdateType, optional
        """
        if change is not unset:
            kwargs["change"] = change
        if field is not unset:
            kwargs["field"] = field
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
