# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.custom_rule_revision import CustomRuleRevision


class CustomRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_rule_revision import CustomRuleRevision

        return {
            "created_at": (datetime,),
            "created_by": (str,),
            "last_revision": (CustomRuleRevision,),
            "name": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "last_revision": "last_revision",
        "name": "name",
    }

    def __init__(self_, created_at: datetime, created_by: str, last_revision: CustomRuleRevision, name: str, **kwargs):
        """


        :param created_at: Creation timestamp
        :type created_at: datetime

        :param created_by: Creator identifier
        :type created_by: str

        :param last_revision:
        :type last_revision: CustomRuleRevision

        :param name: Rule name
        :type name: str
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.last_revision = last_revision
        self_.name = name
