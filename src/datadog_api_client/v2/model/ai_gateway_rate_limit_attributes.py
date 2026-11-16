# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_rate_limit_mode import AiGatewayRateLimitMode
    from datadog_api_client.v2.model.ai_gateway_rate_limit_selector_entry import AiGatewayRateLimitSelectorEntry


class AiGatewayRateLimitAttributes(ModelNormal):
    validations = {
        "cost_microcents_per_minute": {
            "inclusive_maximum": 10000000000000,
            "inclusive_minimum": 1,
        },
        "input_tokens_per_minute": {
            "inclusive_maximum": 100000000000,
            "inclusive_minimum": 1,
        },
        "output_tokens_per_minute": {
            "inclusive_maximum": 100000000000,
            "inclusive_minimum": 1,
        },
        "requests_per_minute": {
            "inclusive_maximum": 10000000,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_rate_limit_mode import AiGatewayRateLimitMode
        from datadog_api_client.v2.model.ai_gateway_rate_limit_selector_entry import AiGatewayRateLimitSelectorEntry

        return {
            "cost_microcents_per_minute": (int, none_type),
            "created_at": (datetime,),
            "created_by": (str,),
            "enabled": (bool,),
            "input_tokens_per_minute": (int, none_type),
            "is_template": (bool,),
            "mode": (AiGatewayRateLimitMode,),
            "monitor_id": (int, none_type),
            "name": (str,),
            "output_tokens_per_minute": (int, none_type),
            "requests_per_minute": (int, none_type),
            "revision": (int,),
            "scope_restricted": (bool,),
            "selector": ([AiGatewayRateLimitSelectorEntry],),
            "tags": ({str: (str,)},),
            "team_id": (UUID, none_type),
            "template_split_dims": ([str],),
            "updated_at": (datetime,),
            "updated_by": (str,),
            "user_id": (UUID, none_type),
        }

    attribute_map = {
        "cost_microcents_per_minute": "cost_microcents_per_minute",
        "created_at": "created_at",
        "created_by": "created_by",
        "enabled": "enabled",
        "input_tokens_per_minute": "input_tokens_per_minute",
        "is_template": "is_template",
        "mode": "mode",
        "monitor_id": "monitor_id",
        "name": "name",
        "output_tokens_per_minute": "output_tokens_per_minute",
        "requests_per_minute": "requests_per_minute",
        "revision": "revision",
        "scope_restricted": "scope_restricted",
        "selector": "selector",
        "tags": "tags",
        "team_id": "team_id",
        "template_split_dims": "template_split_dims",
        "updated_at": "updated_at",
        "updated_by": "updated_by",
        "user_id": "user_id",
    }

    def __init__(
        self_,
        created_at: datetime,
        created_by: str,
        enabled: bool,
        is_template: bool,
        mode: AiGatewayRateLimitMode,
        name: str,
        revision: int,
        scope_restricted: bool,
        tags: Dict[str, str],
        template_split_dims: List[str],
        updated_at: datetime,
        updated_by: str,
        cost_microcents_per_minute: Union[int, none_type, UnsetType] = unset,
        input_tokens_per_minute: Union[int, none_type, UnsetType] = unset,
        monitor_id: Union[int, none_type, UnsetType] = unset,
        output_tokens_per_minute: Union[int, none_type, UnsetType] = unset,
        requests_per_minute: Union[int, none_type, UnsetType] = unset,
        selector: Union[List[AiGatewayRateLimitSelectorEntry], none_type, UnsetType] = unset,
        team_id: Union[UUID, none_type, UnsetType] = unset,
        user_id: Union[UUID, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an AI Gateway rate limit.

        :param cost_microcents_per_minute: Maximum priced spend per rolling minute, in microcents of 1e-8 USD each, shared by all matching traffic, or per counter for a template rate limit. Null when this rule does not limit cost.
        :type cost_microcents_per_minute: int, none_type, optional

        :param created_at: Creation timestamp.
        :type created_at: datetime

        :param created_by: Email of the user who created this rate limit.
        :type created_by: str

        :param enabled: Whether this rate limit is active.
        :type enabled: bool

        :param input_tokens_per_minute: Maximum input tokens per rolling minute shared by all matching traffic, or per counter for a template rate limit. Null when this rule does not limit input tokens.
        :type input_tokens_per_minute: int, none_type, optional

        :param is_template: Whether the selector gives each matching value its own allowance, that is, whether it has at least one per_value entry. Returned even when scope_restricted hides the selector.
        :type is_template: bool

        :param mode: Action taken when request rate exceeds the limit.
        :type mode: AiGatewayRateLimitMode

        :param monitor_id: Datadog monitor that alerts on this rule. Null until one is provisioned.
        :type monitor_id: int, none_type, optional

        :param name: Rate limit name.
        :type name: str

        :param output_tokens_per_minute: Maximum output tokens per rolling minute shared by all matching traffic, or per counter for a template rate limit. Null when this rule does not limit output tokens.
        :type output_tokens_per_minute: int, none_type, optional

        :param requests_per_minute: Maximum requests per rolling minute shared by all matching traffic, or per counter for a template rate limit. Null when this rule does not limit requests.
        :type requests_per_minute: int, none_type, optional

        :param revision: Increases on every change to the definition.
        :type revision: int

        :param scope_restricted: Whether provider or model scope metadata was withheld. Omit unchanged scope fields on an unrelated update to preserve their saved values.
        :type scope_restricted: bool

        :param selector: Dimension rules for a template rate limit, which gives each matched user, Team, or value its own allowance with the rule's limits. Can't be combined with user_id, team_id, or tags, and can't be changed after creation. Omit for a rule with one shared allowance.
        :type selector: [AiGatewayRateLimitSelectorEntry], none_type, optional

        :param tags: Optional scope tags, such as provider, model, ml_app, or custom dimensions. A request matches when it has all of these tags.
        :type tags: {str: (str,)}

        :param team_id: Optional Team UUID. Count only requests attributed to this Datadog Team.
        :type team_id: UUID, none_type, optional

        :param template_split_dims: Dimensions of the selector's per_value entries, such as user_id or tag:env, each matching value of which gets its own allowance. Empty unless is_template is true. Returned even when scope_restricted hides the selector.
        :type template_split_dims: [str]

        :param updated_at: Last modification timestamp.
        :type updated_at: datetime

        :param updated_by: Email of the user who last modified this rate limit.
        :type updated_by: str

        :param user_id: Optional user UUID. Count only this user's requests.
        :type user_id: UUID, none_type, optional
        """
        if cost_microcents_per_minute is not unset:
            kwargs["cost_microcents_per_minute"] = cost_microcents_per_minute
        if input_tokens_per_minute is not unset:
            kwargs["input_tokens_per_minute"] = input_tokens_per_minute
        if monitor_id is not unset:
            kwargs["monitor_id"] = monitor_id
        if output_tokens_per_minute is not unset:
            kwargs["output_tokens_per_minute"] = output_tokens_per_minute
        if requests_per_minute is not unset:
            kwargs["requests_per_minute"] = requests_per_minute
        if selector is not unset:
            kwargs["selector"] = selector
        if team_id is not unset:
            kwargs["team_id"] = team_id
        if user_id is not unset:
            kwargs["user_id"] = user_id
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.enabled = enabled
        self_.is_template = is_template
        self_.mode = mode
        self_.name = name
        self_.revision = revision
        self_.scope_restricted = scope_restricted
        self_.tags = tags
        self_.template_split_dims = template_split_dims
        self_.updated_at = updated_at
        self_.updated_by = updated_by
