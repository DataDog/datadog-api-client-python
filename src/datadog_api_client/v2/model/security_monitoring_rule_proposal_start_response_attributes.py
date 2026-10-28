# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringRuleProposalStartResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "status": (str,),
        }

    attribute_map = {
        "status": "status",
    }

    def __init__(self_, status: str, **kwargs):
        """
        Attributes of the started rule proposal.

        :param status: The status of the rule proposal, one of ``pending`` , ``in_progress`` , ``completed`` , or
            ``failed``. For a newly started rule proposal, the status is ``pending``.
        :type status: str
        """
        super().__init__(kwargs)

        self_.status = status
