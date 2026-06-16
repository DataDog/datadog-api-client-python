# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ownership_evidence_version import OwnershipEvidenceVersion


class OwnershipEvidenceAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ownership_evidence_version import OwnershipEvidenceVersion

        return {
            "evidence_versions": ([OwnershipEvidenceVersion],),
        }

    attribute_map = {
        "evidence_versions": "evidence_versions",
    }

    def __init__(self_, evidence_versions: Union[List[OwnershipEvidenceVersion], none_type], **kwargs):
        """
        The attributes of an ownership evidence response.

        :param evidence_versions: The list of evidence versions associated with an inference.
        :type evidence_versions: [OwnershipEvidenceVersion], none_type
        """
        super().__init__(kwargs)

        self_.evidence_versions = evidence_versions
