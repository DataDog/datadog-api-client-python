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


class CaseNotificationRuleTriggerData(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "change_type": (str,),
            "field": (str,),
            "from_status": (str,),
            "from_status_name": (str,),
            "to_status": (str,),
            "to_status_name": (str,),
        }

    attribute_map = {
        "change_type": "change_type",
        "field": "field",
        "from_status": "from_status",
        "from_status_name": "from_status_name",
        "to_status": "to_status",
        "to_status_name": "to_status_name",
    }

    def __init__(
        self_,
        change_type: Union[str, UnsetType] = unset,
        field: Union[str, UnsetType] = unset,
        from_status: Union[str, UnsetType] = unset,
        from_status_name: Union[str, UnsetType] = unset,
        to_status: Union[str, UnsetType] = unset,
        to_status_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Trigger data

        :param change_type: Change type (added, removed, changed)
        :type change_type: str, optional

        :param field: Field name for attribute value changed trigger
        :type field: str, optional

        :param from_status: Status ID to transition from
        :type from_status: str, optional

        :param from_status_name: Status name to transition from
        :type from_status_name: str, optional

        :param to_status: Status ID to transition to
        :type to_status: str, optional

        :param to_status_name: Status name to transition to
        :type to_status_name: str, optional
        """
        if change_type is not unset:
            kwargs["change_type"] = change_type
        if field is not unset:
            kwargs["field"] = field
        if from_status is not unset:
            kwargs["from_status"] = from_status
        if from_status_name is not unset:
            kwargs["from_status_name"] = from_status_name
        if to_status is not unset:
            kwargs["to_status"] = to_status
        if to_status_name is not unset:
            kwargs["to_status_name"] = to_status_name
        super().__init__(kwargs)
