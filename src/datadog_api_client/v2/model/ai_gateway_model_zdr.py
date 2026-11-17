# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_model_zdr_coverage import AiGatewayModelZdrCoverage


class AiGatewayModelZdr(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_zdr_coverage import AiGatewayModelZdrCoverage

        return {
            "coverage": (AiGatewayModelZdrCoverage,),
            "covered_operations": ([str],),
            "uncovered_operations": ([str],),
        }

    attribute_map = {
        "coverage": "coverage",
        "covered_operations": "covered_operations",
        "uncovered_operations": "uncovered_operations",
    }

    def __init__(
        self_,
        coverage: AiGatewayModelZdrCoverage,
        covered_operations: Union[List[str], UnsetType] = unset,
        uncovered_operations: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The Datadog side of a model's zero data retention eligibility. The customer side is the provider's
        ``zdr_eligible`` setting.

        :param coverage: Datadog's coverage of the model's operations under zero data retention. A model is eligible when
            coverage is ``full`` and its provider's ``zdr_eligible`` is ``true``. ``partial`` means only the
            ``covered_operations`` can be served: requests on other operations are not dispatched to it.
        :type coverage: AiGatewayModelZdrCoverage

        :param covered_operations: Operations covered by zero data retention.
        :type covered_operations: [str], optional

        :param uncovered_operations: Operations not covered by zero data retention.
        :type uncovered_operations: [str], optional
        """
        if covered_operations is not unset:
            kwargs["covered_operations"] = covered_operations
        if uncovered_operations is not unset:
            kwargs["uncovered_operations"] = uncovered_operations
        super().__init__(kwargs)

        self_.coverage = coverage
