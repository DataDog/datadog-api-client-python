# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSyslogSourceMode(ModelSimple):
    """
    Protocol used by the syslog source to receive messages.

    :param value: Must be one of ["tcp", "udp"].
    :type value: str
    """

    allowed_values = {
        "tcp",
        "udp",
    }
    TCP: ClassVar["ObservabilityPipelineSyslogSourceMode"]
    UDP: ClassVar["ObservabilityPipelineSyslogSourceMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSyslogSourceMode.TCP = ObservabilityPipelineSyslogSourceMode("tcp")
ObservabilityPipelineSyslogSourceMode.UDP = ObservabilityPipelineSyslogSourceMode("udp")
