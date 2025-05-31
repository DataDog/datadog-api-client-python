# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSyslogNgSourceType(ModelSimple):
    """
    The source type. The value should always be `syslog_ng`.

    :param value: If omitted defaults to "syslog_ng". Must be one of ["syslog_ng"].
    :type value: str
    """

    allowed_values = {
        "syslog_ng",
    }
    SYSLOG_NG: ClassVar["ObservabilityPipelineSyslogNgSourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSyslogNgSourceType.SYSLOG_NG = ObservabilityPipelineSyslogNgSourceType("syslog_ng")
