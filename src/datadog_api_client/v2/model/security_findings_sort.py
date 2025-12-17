# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityFindingsSort(ModelSimple):
    """
    The sort parameters when querying security findings.

    :param value: If omitted defaults to "-@detection_changed_at". Must be one of ["@detection_changed_at", "-@detection_changed_at"].
    :type value: str
    """

    allowed_values = {
        "@detection_changed_at",
        "-@detection_changed_at",
    }
    DETECTION_CHANGED_AT_ASC: ClassVar["SecurityFindingsSort"]
    DETECTION_CHANGED_AT_DESC: ClassVar["SecurityFindingsSort"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityFindingsSort.DETECTION_CHANGED_AT_ASC = SecurityFindingsSort("@detection_changed_at")
SecurityFindingsSort.DETECTION_CHANGED_AT_DESC = SecurityFindingsSort("-@detection_changed_at")
