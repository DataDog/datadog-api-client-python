# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    pass


class SecurityMonitoringDatasetVersionHistoryEntries(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_version_entry import (
            SecurityMonitoringDatasetVersionEntry,
        )

        return (SecurityMonitoringDatasetVersionEntry,)

    def __init__(self_, **kwargs):
        """
        A map from version number (as a string) to the dataset state at that version.
        """
        super().__init__(kwargs)
