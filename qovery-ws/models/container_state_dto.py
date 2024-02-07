# coding: utf-8

"""
    websocket-gateway

    Describe the weboscket endpoints

    The version of the OpenAPI document: 0.1.0
    Contact: erebe@erebe.eu
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from qovery-ws.models.service_state_dto import ServiceStateDto
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ContainerStateDto(BaseModel):
    """
    ContainerStateDto
    """ # noqa: E501
    started_at: Optional[StrictInt] = Field(default=None, description="Unix timestamp with millisecond precision")
    state: ServiceStateDto
    state_message: Optional[StrictStr] = None
    state_reason: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["started_at", "state", "state_message", "state_reason"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ContainerStateDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if started_at (nullable) is None
        # and model_fields_set contains the field
        if self.started_at is None and "started_at" in self.model_fields_set:
            _dict['started_at'] = None

        # set to None if state_message (nullable) is None
        # and model_fields_set contains the field
        if self.state_message is None and "state_message" in self.model_fields_set:
            _dict['state_message'] = None

        # set to None if state_reason (nullable) is None
        # and model_fields_set contains the field
        if self.state_reason is None and "state_reason" in self.model_fields_set:
            _dict['state_reason'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ContainerStateDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "started_at": obj.get("started_at"),
            "state": obj.get("state"),
            "state_message": obj.get("state_message"),
            "state_reason": obj.get("state_reason")
        })
        return _obj


