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
    from datadog_api_client.v2.model.version_history_update import VersionHistoryUpdate
    from datadog_api_client.v2.model.security_monitoring_suppression_attributes import (
        SecurityMonitoringSuppressionAttributes,
    )


class SuppressionVersions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.version_history_update import VersionHistoryUpdate
        from datadog_api_client.v2.model.security_monitoring_suppression_attributes import (
            SecurityMonitoringSuppressionAttributes,
        )

        return {
            "changes": ([VersionHistoryUpdate],),
            "suppression": (SecurityMonitoringSuppressionAttributes,),
        }

    attribute_map = {
        "changes": "changes",
        "suppression": "suppression",
    }

    def __init__(
        self_,
        changes: Union[List[VersionHistoryUpdate], UnsetType] = unset,
        suppression: Union[SecurityMonitoringSuppressionAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        A suppression version with a list of updates.

        :param changes: A list of changes.
        :type changes: [VersionHistoryUpdate], optional

        :param suppression: The attributes of the suppression rule.
        :type suppression: SecurityMonitoringSuppressionAttributes, optional
        """
        if changes is not unset:
            kwargs["changes"] = changes
        if suppression is not unset:
            kwargs["suppression"] = suppression
        super().__init__(kwargs)
