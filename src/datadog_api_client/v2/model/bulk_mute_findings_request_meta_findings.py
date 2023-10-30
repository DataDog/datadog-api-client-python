# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class BulkMuteFindingsRequestMetaFindings(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "finding_id": (str,),
        }

    attribute_map = {
        "finding_id": "finding_id",
    }

    def __init__(self_, finding_id: Union[str, UnsetType] = unset, **kwargs):
        """
        Finding object containing the finding information.

        :param finding_id: The unique ID for this finding.
        :type finding_id: str, optional
        """
        if finding_id is not unset:
            kwargs["finding_id"] = finding_id
        super().__init__(kwargs)
