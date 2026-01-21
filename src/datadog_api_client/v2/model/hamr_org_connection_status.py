# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HamrOrgConnectionStatus(ModelSimple):
    """
    Status of the HAMR connection:
        - 0: UNSPECIFIED - Connection status not specified
        - 1: ONBOARDING - Initial setup of HAMR connection
        - 2: PASSIVE - Secondary organization in passive standby mode
        - 3: FAILOVER - Liminal status between PASSIVE and ACTIVE
        - 4: ACTIVE - Organization is an active failover
        - 5: RECOVERY - Recovery operation in progress

    :param value: Must be one of [0, 1, 2, 3, 4, 5].
    :type value: int
    """

    allowed_values = {
        0,
        1,
        2,
        3,
        4,
        5,
    }
    UNSPECIFIED: ClassVar["HamrOrgConnectionStatus"]
    ONBOARDING: ClassVar["HamrOrgConnectionStatus"]
    PASSIVE: ClassVar["HamrOrgConnectionStatus"]
    FAILOVER: ClassVar["HamrOrgConnectionStatus"]
    ACTIVE: ClassVar["HamrOrgConnectionStatus"]
    RECOVERY: ClassVar["HamrOrgConnectionStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (int,),
        }


HamrOrgConnectionStatus.UNSPECIFIED = HamrOrgConnectionStatus(0)
HamrOrgConnectionStatus.ONBOARDING = HamrOrgConnectionStatus(1)
HamrOrgConnectionStatus.PASSIVE = HamrOrgConnectionStatus(2)
HamrOrgConnectionStatus.FAILOVER = HamrOrgConnectionStatus(3)
HamrOrgConnectionStatus.ACTIVE = HamrOrgConnectionStatus(4)
HamrOrgConnectionStatus.RECOVERY = HamrOrgConnectionStatus(5)
