# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class SyntheticsAPIStepSubtype(StringEnum):
    """
    The subtype of the Synthetic multistep API test step, currently only supporting `http`.

    :param value: If omitted defaults to "http". Must be one of ["http"].
    :type value: str
    """

    allowed_values = {
        "http",
    }
    HTTP: ClassVar["SyntheticsAPIStepSubtype"]


SyntheticsAPIStepSubtype.HTTP = SyntheticsAPIStepSubtype("http")
