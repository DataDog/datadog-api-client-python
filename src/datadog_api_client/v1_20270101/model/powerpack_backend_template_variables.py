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
    from datadog_api_client.v1_20270101.model.powerpack_backend_template_variable import (
        PowerpackBackendTemplateVariable,
    )


class PowerpackBackendTemplateVariables(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.powerpack_backend_template_variable import (
            PowerpackBackendTemplateVariable,
        )

        return {
            "controlled_by_powerpack": ([PowerpackBackendTemplateVariable],),
            "controlled_externally": ([PowerpackBackendTemplateVariable],),
        }

    attribute_map = {
        "controlled_by_powerpack": "controlled_by_powerpack",
        "controlled_externally": "controlled_externally",
    }

    def __init__(
        self_,
        controlled_by_powerpack: List[PowerpackBackendTemplateVariable],
        controlled_externally: List[PowerpackBackendTemplateVariable],
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param controlled_by_powerpack: Test-only generated schema for the dashboard versioning proof of concept.
        :type controlled_by_powerpack: [PowerpackBackendTemplateVariable]

        :param controlled_externally: Test-only generated schema for the dashboard versioning proof of concept.
        :type controlled_externally: [PowerpackBackendTemplateVariable]
        """
        super().__init__(kwargs)

        self_.controlled_by_powerpack = controlled_by_powerpack
        self_.controlled_externally = controlled_externally
