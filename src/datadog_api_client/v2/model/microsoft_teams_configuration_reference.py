# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.microsoft_teams_configuration_reference_data import (
        MicrosoftTeamsConfigurationReferenceData,
    )


class MicrosoftTeamsConfigurationReference(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.microsoft_teams_configuration_reference_data import (
            MicrosoftTeamsConfigurationReferenceData,
        )

        return {
            "data": (MicrosoftTeamsConfigurationReferenceData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[MicrosoftTeamsConfigurationReferenceData, none_type], **kwargs):
        """
        A reference to a Microsoft Teams Configuration resource.

        :param data: The Microsoft Teams configuration relationship data object.
        :type data: MicrosoftTeamsConfigurationReferenceData, none_type
        """
        super().__init__(kwargs)

        self_.data = data
