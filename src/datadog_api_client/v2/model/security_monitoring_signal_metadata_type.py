# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class SecurityMonitoringSignalMetadataType(StringEnum):
    """
    The type of event.

    :param value: If omitted defaults to "signal_metadata". Must be one of ["signal_metadata"].
    :type value: str
    """

    allowed_values = {
        "signal_metadata",
    }
    SIGNAL_METADATA: ClassVar["SecurityMonitoringSignalMetadataType"]


SecurityMonitoringSignalMetadataType.SIGNAL_METADATA = SecurityMonitoringSignalMetadataType("signal_metadata")
