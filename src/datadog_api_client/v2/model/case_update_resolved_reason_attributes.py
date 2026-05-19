# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CaseUpdateResolvedReasonAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "security_resolved_reason": (str,),
        }

    attribute_map = {
        "security_resolved_reason": "security_resolved_reason",
    }

    def __init__(self_, security_resolved_reason: str, **kwargs):
        """
        Attributes for setting the resolution reason on a security case.

        :param security_resolved_reason: The reason the security case was resolved (for example, ``FALSE_POSITIVE`` , ``TRUE_POSITIVE`` , ``BENIGN_POSITIVE`` ).
        :type security_resolved_reason: str
        """
        super().__init__(kwargs)

        self_.security_resolved_reason = security_resolved_reason
