# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.severity_override_attributes import SeverityOverrideAttributes
    from datadog_api_client.v2.model.severity_override_set import SeverityOverrideSet
    from datadog_api_client.v2.model.severity_override_clear import SeverityOverrideClear


class SeverityOverrideRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.severity_override_attributes import SeverityOverrideAttributes

        return {
            "severity": (SeverityOverrideAttributes,),
        }

    attribute_map = {
        "severity": "severity",
    }

    def __init__(
        self_, severity: Union[SeverityOverrideAttributes, SeverityOverrideSet, SeverityOverrideClear], **kwargs
    ):
        """
        Attributes of the severity override request.

        :param severity: Severity override to apply to the findings.
            Set ``action`` to ``set`` to apply a manual severity override with the given ``value``.
            Set ``action`` to ``clear`` to remove a manual severity override.
        :type severity: SeverityOverrideAttributes
        """
        super().__init__(kwargs)

        self_.severity = severity
