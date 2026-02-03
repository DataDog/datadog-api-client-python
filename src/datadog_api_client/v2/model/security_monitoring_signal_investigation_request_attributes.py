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


class SecurityMonitoringSignalInvestigationRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "deployment": (str,),
            "signal_id": (str,),
        }

    attribute_map = {
        "deployment": "deployment",
        "signal_id": "signal_id",
    }

    def __init__(self_, signal_id: str, deployment: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes for creating a signal investigation.

        :param deployment: Optional deployment override for the investigation.
        :type deployment: str, optional

        :param signal_id: The unique ID of the security signal.
        :type signal_id: str
        """
        if deployment is not unset:
            kwargs["deployment"] = deployment
        super().__init__(kwargs)

        self_.signal_id = signal_id
