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


class AutomationRuleTriggerData(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "approval_type": (str,),
            "change_type": (str,),
            "field": (str,),
            "from_status_name": (str,),
            "to_status_name": (str,),
        }

    attribute_map = {
        "approval_type": "approval_type",
        "change_type": "change_type",
        "field": "field",
        "from_status_name": "from_status_name",
        "to_status_name": "to_status_name",
    }

    def __init__(
        self_,
        approval_type: Union[str, UnsetType] = unset,
        change_type: Union[str, UnsetType] = unset,
        field: Union[str, UnsetType] = unset,
        from_status_name: Union[str, UnsetType] = unset,
        to_status_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Additional configuration for the trigger, dependent on the trigger type. For ``status_transitioned`` triggers, specify ``from_status_name`` and ``to_status_name``. For ``attribute_value_changed`` triggers, specify ``field`` and ``change_type``.

        :param approval_type: The approval outcome to match. Used with ``case_review_approved`` triggers.
        :type approval_type: str, optional

        :param change_type: The kind of attribute change to match. Allowed values: ``VALUE_ADDED`` , ``VALUE_DELETED`` , ``ANY_CHANGES``. Used with ``attribute_value_changed`` triggers.
        :type change_type: str, optional

        :param field: The case attribute field name to monitor for changes. Used with ``attribute_value_changed`` triggers.
        :type field: str, optional

        :param from_status_name: The originating status name. Used with ``status_transitioned`` triggers to match transitions from this status.
        :type from_status_name: str, optional

        :param to_status_name: The destination status name. Used with ``status_transitioned`` triggers to match transitions to this status.
        :type to_status_name: str, optional
        """
        if approval_type is not unset:
            kwargs["approval_type"] = approval_type
        if change_type is not unset:
            kwargs["change_type"] = change_type
        if field is not unset:
            kwargs["field"] = field
        if from_status_name is not unset:
            kwargs["from_status_name"] = from_status_name
        if to_status_name is not unset:
            kwargs["to_status_name"] = to_status_name
        super().__init__(kwargs)
