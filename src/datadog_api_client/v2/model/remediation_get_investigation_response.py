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
    from datadog_api_client.v2.model.remediation_investigation import RemediationInvestigation


class RemediationGetInvestigationResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.remediation_investigation import RemediationInvestigation

        return {
            "investigation": (RemediationInvestigation,),
        }

    attribute_map = {
        "investigation": "investigation",
    }

    def __init__(self_, investigation: RemediationInvestigation, **kwargs):
        """
        Response payload for getting a single investigation.

        :param investigation: A single ECS remediation investigation: a detected issue together with its proposed plan, history, and ECS workload metadata.
        :type investigation: RemediationInvestigation
        """
        super().__init__(kwargs)

        self_.investigation = investigation
