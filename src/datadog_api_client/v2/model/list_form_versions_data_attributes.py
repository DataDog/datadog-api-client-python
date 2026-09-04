# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.form_version_attributes import FormVersionAttributes


class ListFormVersionsDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.form_version_attributes import FormVersionAttributes

        return {
            "versions": ([FormVersionAttributes],),
        }

    attribute_map = {
        "versions": "versions",
    }

    def __init__(self_, versions: List[FormVersionAttributes], **kwargs):
        """
        The attributes for a list of form versions.

        :param versions: The list of versions for the form.
        :type versions: [FormVersionAttributes]
        """
        super().__init__(kwargs)

        self_.versions = versions
