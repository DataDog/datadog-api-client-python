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
    from datadog_api_client.v2.model.experiments_stop_bandit_v2_request_data_attributes import (
        ExperimentsStopBanditV2RequestDataAttributes,
    )
    from datadog_api_client.v2.model.experiments_stop_bandit_v2_request_data_type import (
        ExperimentsStopBanditV2RequestDataType,
    )


class ExperimentsStopBanditV2RequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_stop_bandit_v2_request_data_attributes import (
            ExperimentsStopBanditV2RequestDataAttributes,
        )
        from datadog_api_client.v2.model.experiments_stop_bandit_v2_request_data_type import (
            ExperimentsStopBanditV2RequestDataType,
        )

        return {
            "attributes": (ExperimentsStopBanditV2RequestDataAttributes,),
            "type": (ExperimentsStopBanditV2RequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ExperimentsStopBanditV2RequestDataAttributes,
        type: ExperimentsStopBanditV2RequestDataType,
        **kwargs,
    ):
        """
        The variant to serve once the bandit stops.

        :param attributes: The variant to serve once the bandit stops.
        :type attributes: ExperimentsStopBanditV2RequestDataAttributes

        :param type: Stop bandit request resource type.
        :type type: ExperimentsStopBanditV2RequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
