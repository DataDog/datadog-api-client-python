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
    from datadog_api_client.v2.model.bulk_mute_findings_request_properties import BulkMuteFindingsRequestProperties


class BulkMuteFindingsRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.bulk_mute_findings_request_properties import BulkMuteFindingsRequestProperties

        return {
            "mute": (BulkMuteFindingsRequestProperties,),
        }

    attribute_map = {
        "mute": "mute",
    }

    def __init__(self_, mute: BulkMuteFindingsRequestProperties, **kwargs):
        """
        The mute properties to be updated.

        :param mute: Object containing the new mute properties of the findings.
        :type mute: BulkMuteFindingsRequestProperties
        """
        super().__init__(kwargs)

        self_.mute = mute
