# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_finding_type import SecurityFindingType


class AutomationRuleScope(ModelNormal):
    validations = {
        "finding_types": {
            "min_items": 1,
        },
        "query": {
            "max_length": 30000,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_finding_type import SecurityFindingType

        return {
            "finding_types": ([SecurityFindingType],),
            "query": (str,),
        }

    attribute_map = {
        "finding_types": "finding_types",
        "query": "query",
    }

    def __init__(self_, finding_types: List[SecurityFindingType], query: Union[str, UnsetType] = unset, **kwargs):
        """
        Defines the scope of findings to which the automation rule applies.

        :param finding_types: The list of security finding types that the automation rule applies to.
        :type finding_types: [SecurityFindingType]

        :param query: A search query to further filter the findings matched by this rule. The ``@workflow.*`` namespace and ``@status`` fields are not permitted. For a reference of available fields, see the `Security Findings schema documentation <https://docs.datadoghq.com/security/guide/findings-schema/>`_.
        :type query: str, optional
        """
        if query is not unset:
            kwargs["query"] = query
        super().__init__(kwargs)

        self_.finding_types = finding_types
