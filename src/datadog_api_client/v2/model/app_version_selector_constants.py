# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AppVersionSelectorConstants(ModelSimple):
    """
    Constants that always select a particular version of an app.

    :param value: Must be one of ["latest", "deployed"].
    :type value: str
    """

    allowed_values = {
        "latest",
        "deployed",
    }
    LATEST: ClassVar["AppVersionSelectorConstants"]
    DEPLOYED: ClassVar["AppVersionSelectorConstants"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AppVersionSelectorConstants.LATEST = AppVersionSelectorConstants("latest")
AppVersionSelectorConstants.DEPLOYED = AppVersionSelectorConstants("deployed")
