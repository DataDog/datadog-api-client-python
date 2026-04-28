# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.mute_findings_mute_attributes import MuteFindingsMuteAttributes


class MuteFindingsRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.mute_findings_mute_attributes import MuteFindingsMuteAttributes

        return {
            "mute": (MuteFindingsMuteAttributes,),
        }

    attribute_map = {
        "mute": "mute",
    }

    def __init__(self_, mute: MuteFindingsMuteAttributes, **kwargs):
        """
        Attributes of the mute request.

        :param mute: Mute properties to apply to the findings.
        :type mute: MuteFindingsMuteAttributes
        """
        super().__init__(kwargs)

        self_.mute = mute
