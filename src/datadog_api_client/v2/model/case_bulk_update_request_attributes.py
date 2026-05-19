# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.case_bulk_action_type import CaseBulkActionType


class CaseBulkUpdateRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_bulk_action_type import CaseBulkActionType

        return {
            "case_ids": ([str],),
            "payload": ({str: (str,)},),
            "type": (CaseBulkActionType,),
        }

    attribute_map = {
        "case_ids": "case_ids",
        "payload": "payload",
        "type": "type",
    }

    def __init__(
        self_,
        case_ids: List[str],
        type: CaseBulkActionType,
        payload: Union[Dict[str, str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for the bulk update, specifying which cases to update and the action to apply.

        :param case_ids: An array of case identifiers to apply the bulk action to.
        :type case_ids: [str]

        :param payload: A key-value map of action-specific parameters. The required keys depend on the action type (for example, ``priority`` for the priority action, ``assignee_id`` for assign).
        :type payload: {str: (str,)}, optional

        :param type: The type of action to apply in a bulk update. Allowed values are ``priority`` , ``status`` , ``assign`` , ``unassign`` , ``archive`` , ``unarchive`` , ``jira`` , ``servicenow`` , ``linear`` , ``update_project``.
        :type type: CaseBulkActionType
        """
        if payload is not unset:
            kwargs["payload"] = payload
        super().__init__(kwargs)

        self_.case_ids = case_ids
        self_.type = type
