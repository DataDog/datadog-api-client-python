# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RUMPermanentRetentionFilterID(ModelSimple):
    """
    The identifier of a permanent RUM retention filter.

    :param value: Must be one of ["rum_apm_flat_sampling", "synthetics_sessions", "forced_replay_sessions"].
    :type value: str
    """

    allowed_values = {
        "rum_apm_flat_sampling",
        "synthetics_sessions",
        "forced_replay_sessions",
    }
    RUM_APM_FLAT_SAMPLING: ClassVar["RUMPermanentRetentionFilterID"]
    SYNTHETICS_SESSIONS: ClassVar["RUMPermanentRetentionFilterID"]
    FORCED_REPLAY_SESSIONS: ClassVar["RUMPermanentRetentionFilterID"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RUMPermanentRetentionFilterID.RUM_APM_FLAT_SAMPLING = RUMPermanentRetentionFilterID("rum_apm_flat_sampling")
RUMPermanentRetentionFilterID.SYNTHETICS_SESSIONS = RUMPermanentRetentionFilterID("synthetics_sessions")
RUMPermanentRetentionFilterID.FORCED_REPLAY_SESSIONS = RUMPermanentRetentionFilterID("forced_replay_sessions")
