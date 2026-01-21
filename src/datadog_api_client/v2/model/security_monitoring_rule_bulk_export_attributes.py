# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringRuleBulkExportAttributes(ModelNormal):
    validations = {
        "rule_ids": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "rule_ids": ([str],),
        }

    attribute_map = {
        "rule_ids": "ruleIds",
    }

    def __init__(self_, rule_ids: List[str], **kwargs):
        """
        Attributes for bulk exporting security monitoring rules.

        :param rule_ids: List of rule IDs to export. Each rule will be included in the resulting ZIP file
            as a separate JSON file.
        :type rule_ids: [str]
        """
        super().__init__(kwargs)

        self_.rule_ids = rule_ids
