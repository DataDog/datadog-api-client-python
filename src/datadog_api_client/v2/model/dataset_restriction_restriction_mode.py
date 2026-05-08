# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DatasetRestrictionRestrictionMode(ModelSimple):
    """
    Controls the default data visibility for the product type. `standard` makes data visible
        to all users with appropriate product access. `default_hide` hides data by default and
        requires explicit grants for each dataset.

    :param value: Must be one of ["standard", "default_hide"].
    :type value: str
    """

    allowed_values = {
        "standard",
        "default_hide",
    }
    STANDARD: ClassVar["DatasetRestrictionRestrictionMode"]
    DEFAULT_HIDE: ClassVar["DatasetRestrictionRestrictionMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DatasetRestrictionRestrictionMode.STANDARD = DatasetRestrictionRestrictionMode("standard")
DatasetRestrictionRestrictionMode.DEFAULT_HIDE = DatasetRestrictionRestrictionMode("default_hide")
