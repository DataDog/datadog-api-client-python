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


class SecurityMonitoringRuleBulkDeleteResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "deleted_rules": ([str],),
            "failed_rules": ([str],),
        }

    attribute_map = {
        "deleted_rules": "deletedRules",
        "failed_rules": "failedRules",
    }

    def __init__(
        self_,
        deleted_rules: Union[List[str], UnsetType] = unset,
        failed_rules: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Response for bulk deleting security monitoring rules.

        :param deleted_rules: List of successfully deleted rule IDs.
        :type deleted_rules: [str], optional

        :param failed_rules: List of rule IDs that could not be deleted.
        :type failed_rules: [str], optional
        """
        if deleted_rules is not unset:
            kwargs["deleted_rules"] = deleted_rules
        if failed_rules is not unset:
            kwargs["failed_rules"] = failed_rules
        super().__init__(kwargs)
