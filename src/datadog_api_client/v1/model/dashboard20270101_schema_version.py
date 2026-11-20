# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class Dashboard20270101SchemaVersion(ModelSimple):
    """
    Test-only request-body discriminator for the dashboard schema-versioning proof of concept.

    :param value: If omitted defaults to "2027-01-01". Must be one of ["2027-01-01"].
    :type value: str
    """

    allowed_values = {
        "2027-01-01",
    }
    VERSION_2027_01_01: ClassVar["Dashboard20270101SchemaVersion"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


Dashboard20270101SchemaVersion.VERSION_2027_01_01 = Dashboard20270101SchemaVersion("2027-01-01")
